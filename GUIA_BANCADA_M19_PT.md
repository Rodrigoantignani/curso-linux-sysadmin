# Bancada comum do M19

Nomes do módulo: VM 201 e hostname rocky-lab; VM 202 e hostname debian-lab; VM 204 e hostname srv-deb; cliente temporário 212 e hostname m19-client. Nome Proxmox e hostname do convidado são configurações distintas: confira ambos antes das guardas. Os aliases DNS web, mail e proxy não renomeiam a máquina.

Antes da 19.4, a VM 204 precisa estar sem instalações anteriores de nginx e Apache. As guardas que encontram pacotes ou configurações existentes devem interromper o roteiro: não os remova automaticamente. Use a VM nova da 19.1 ou reconcilie serviço, dados e dependências com o inventário antes de retomar.

Depois da 19.1 e antes da 19.2, execute as seções 1–3 nas VMs 201 e 202. Depois da 19.3 e antes da 19.4, execute a seção 4 nas VMs 201, 202 e 204. Os serviços ficam nas aulas. Nenhum comando deste material foi executado nas VMs durante a elaboração.

A rede didática é a mesma da 17.5: `192.0.2.0/24`, exclusivamente em `vmbr17`, sem porta física, IP do host, gateway ou NAT. Trata-se de um bloco reservado a documentação, usado aqui apenas na bancada isolada. Não o implante numa rede roteada.

Antes de atribuir endereços, confronte inventário, rotas, VPNs e redes de gestão. Se há sobreposição, pare e reprojete coerentemente todas as referências do M19; não misture duas redes no mesmo roteiro.

| Máquina | Endereço isolado | Papel |
| --- | --- | --- |
| 204 · srv-deb | `192.0.2.204/24` | Servidor criado na 19.1 |
| 201 · rocky-lab | `192.0.2.201/24` | Serviço Podman do M18 |
| 202 · debian-lab | `192.0.2.202/24` | Cliente de testes; DHCP temporário na 19.3 |
| 212 · m19-client | DHCP entre `.100` e `.149` | VM nova somente no desafio 19.9 |

O domínio é `lab.test`. DNS, web, mail, proxy e Samba apontam para a VM 204; `app.lab.test` aponta para a VM 201. Uma zona de laboratório não precisa nem pode reivindicar um domínio público de outra pessoa.

## Preparação da bridge depois do M17

Se a limpeza da 17.7 retirou `vmbr17`, recrie-a no host autorizado antes dos blocos de rede deste guia. O comando abaixo é executado no console root do Proxmox e alcança somente a bridge do exercício; não recarrega toda a rede. Se a inclusão de `interfaces.d` tiver outro padrão, pare e confira a preparação do host. Uma bridge já existente será apenas conferida pelos blocos seguintes.

As VMs 201, 202 e 204 precisam estar no **mesmo host físico** durante o M19: bridges sem uplink com nomes iguais em hosts diferentes não conectam a LAN isolada. Confira os proprietários no inventário antes de atribuir endereços; não migre cargas por tentativa.

```bash
m19_bridge_local() {
  [ -d /sys/class/net/vmbr17/bridge ] && return 0
  [ ! -e /etc/network/interfaces.d/m17-lab ] || return 1
  grep -Eq '^[[:space:]]*source(-directory)?[[:space:]]+/etc/network/interfaces.d' /etc/network/interfaces || return 1
  cat > /etc/network/interfaces.d/m17-lab <<'EOF'
auto vmbr17
iface vmbr17 inet manual
    bridge-ports none
    bridge-stp off
    bridge-fd 0
    post-up sysctl -w net.ipv6.conf.vmbr17.disable_ipv6=1
EOF
  ifquery vmbr17 && ifup vmbr17
}
m19_bridge_local
ip -br link show vmbr17
```

## 1 · Conferir o host e acrescentar uma placa desligada

No Proxmox autorizado, localize o nó proprietário no inventário. Repita o bloco para uma VM de cada vez no seu nó; não aplique comandos destinados às VMs dentro do hipervisor.

```bash
pvesh get /cluster/resources --type vm --output-format json-pretty || exit 1
ip -d link show vmbr17 || exit 1
bridge link show master vmbr17 || exit 1
ip -br address show vmbr17 || exit 1
test -z "$(ip -o address show dev vmbr17)" || exit 1
for M19_PORT in /sys/class/net/vmbr17/brif/*; do
  test -e "$M19_PORT" || continue
  M19_LINK=$(basename "$M19_PORT") || exit 1
  case "$M19_LINK" in tap*|fwpr*) ;; *) exit 1 ;; esac
  test ! -e "/sys/class/net/$M19_LINK/device" || exit 1
done
read -r -p 'VMID 201 ou 202 no no proprietario: ' M19_ID
case "$M19_ID" in 201) M19_NAME=rocky-lab ;; 202) M19_NAME=debian-lab ;; *) exit 1 ;; esac
M19_CONF=$(qm config "$M19_ID") || exit 1
test "$(printf '%s\n' "$M19_CONF" | sed -n 's/^name: //p')" = "$M19_NAME" || exit 1
if printf '%s\n' "$M19_CONF" | grep -q '^net1:'; then exit 1; fi
M19_EVID=$(mktemp -d /root/m19-rede.XXXXXX) || exit 1
printf '%s\n' "$M19_CONF" > "$M19_EVID/config-antes.txt"
qm snapshot "$M19_ID" m19-rede-inicio || exit 1
qm set "$M19_ID" --net1 virtio,bridge=vmbr17,link_down=1 || exit 1
qm config "$M19_ID" > "$M19_EVID/config-depois.txt" || exit 1
diff <(grep '^net0:' "$M19_EVID/config-antes.txt") <(grep '^net0:' "$M19_EVID/config-depois.txt") || exit 1
grep '^net1:' "$M19_EVID/config-depois.txt"
printf '%s\n' "$M19_EVID"
```

A bridge precisa existir neste nó e não pode ter uplink físico nem endereço do host. Se qualquer placa ou perfil já existe, preserve-o e reveja o estado; este guia não autoriza substituir um recurso existente. O snapshot protege a VM, não a configuração do host.

Copie a MAC de `net1` e guarde a pasta de evidências fora da VM. A nova placa deve aparecer no convidado; se a versão ou o hardware exigir inicialização a frio, desligue e ligue somente a VM identificada após combinar a janela, preservando a gestão.

## 2 · Preparar o perfil dentro da VM

Dentro da VM escolhida, entre como `student`. Confira hostname, endereço de gestão e rota padrão antes de alterar a placa nova. A interface é identificada pela MAC, nunca pela posição numa lista.

Os blocos usam `nmcli` nas VMs 201 e 202. A Debian 202 vem com ifupdown: se `nmcli` não existir, tire um snapshot e instale `sudo apt install network-manager`. Interfaces já declaradas em `/etc/network/interfaces`, como a gestão, continuam `unmanaged` e fora do NetworkManager; confira com `nmcli device` antes de seguir. Para as consultas DNS das aulas, instale também `dnsutils` na 202 e `bind-utils` na 201.

```bash
test "$(id -un)" = student || exit 1
case "$(hostname -s)" in rocky-lab) LAB_ADDR=192.0.2.201/24 ;; debian-lab) LAB_ADDR=192.0.2.202/24 ;; *) exit 1 ;; esac
ip -br address
ip route
nmcli -f GENERAL.DEVICE,GENERAL.HWADDR,GENERAL.CONNECTION device show
read -r -p 'MAC exata da net1 no Proxmox: ' LAB_MAC
read -r -p 'Interface com essa MAC dentro da VM: ' LAB_IF
test -n "$LAB_MAC" && test -n "$LAB_IF" || exit 1
test "$(cat "/sys/class/net/$LAB_IF/address")" = "$(printf '%s' "$LAB_MAC" | tr 'A-F' 'a-f')" || exit 1
M19_ACTIVE=$(nmcli -g GENERAL.CONNECTION device show "$LAB_IF") || exit 1
test -z "$(printf '%s\n' "$M19_ACTIVE" | sed '/^--$/d')" || exit 1
M19_PROFILES=$(nmcli -g NAME connection show) || exit 1
if printf '%s\n' "$M19_PROFILES" | grep -qx m19-isolada; then exit 1; fi
install -d -m 0700 "$HOME/m19-lab" || exit 1
ip -4 route show default > "$HOME/m19-lab/default-before.txt"
nmcli -f NAME,UUID,TYPE,DEVICE connection show > "$HOME/m19-lab/profiles-before.txt"
sudo nmcli connection add type ethernet ifname "$LAB_IF" con-name m19-isolada \
  802-3-ethernet.mac-address "$LAB_MAC" ipv4.method manual \
  ipv4.addresses "$LAB_ADDR" ipv4.never-default yes ipv4.ignore-auto-dns yes \
  ipv6.method disabled connection.autoconnect yes || exit 1
LAB_UUID=$(nmcli -g connection.uuid connection show m19-isolada) || exit 1
test -n "$LAB_UUID" || exit 1
printf 'LAB_IF=%q\nLAB_UUID=%q\nLAB_ADDR=%q\n' "$LAB_IF" "$LAB_UUID" "$LAB_ADDR" > "$HOME/m19-lab/client.env"
chmod 0600 "$HOME/m19-lab/client.env"
```

O arquivo contém somente valores produzidos por você, sem senha. Não carregue arquivos recebidos de uma rede como scripts de ambiente. A configuração não acrescenta gateway nem DNS à placa isolada; as primeiras consultas usam o servidor DNS explicitamente.

## 3 · Ligar somente o cabo da placa nova

Volte ao mesmo terminal do Proxmox, com as variáveis conferidas. Não reconstrua a placa omitindo MAC ou bridge; preserve todas as propriedades e mude apenas o link.

```bash
test "$(qm config "$M19_ID" | sed -n 's/^name: //p')" = "$M19_NAME" || exit 1
M19_NET1=$(qm config "$M19_ID" | sed -n 's/^net1: //p') || exit 1
case ",$M19_NET1," in *,bridge=vmbr17,*) ;; *) exit 1 ;; esac
case ",$M19_NET1," in *,link_down=1,*) ;; *) exit 1 ;; esac
M19_NET1=$(printf '%s' "$M19_NET1" | sed -E 's/,link_down=1//g')
qm set "$M19_ID" --net1 "$M19_NET1,link_down=0" || exit 1
qm config "$M19_ID"
```

Dentro da VM, use a sessão e o perfil que acabou de criar.

```bash
sudo nmcli connection up uuid "$LAB_UUID" || exit 1
ip -br address show dev "$LAB_IF"
ip -4 route show default > "$HOME/m19-lab/default-after.txt"
cmp "$HOME/m19-lab/default-before.txt" "$HOME/m19-lab/default-after.txt" || exit 1
ip route get 192.0.2.204
ping -c 3 192.0.2.204
nmcli -f connection.uuid,connection.interface-name,ipv4.addresses,ipv4.gateway,ipv4.never-default connection show uuid "$LAB_UUID"
```

O endereço isolado deve corresponder à VM e o caminho para a VM 204 deve usar essa placa. A rota padrão permanece igual. Falha de ping não autoriza desabilitar o firewall: confira endereço, cabo e política com as evidências reais.

## 4 · Preparar nomes estáticos antes da 19.4

Execute esta seção uma vez em cada VM 201, 202 e 204, depois de conferir a identidade no inventário do Proxmox e o endereço isolado dentro do convidado. Ela não altera o DNS da gestão nem exige substituir o resolvedor do sistema. Não a execute no host Proxmox, no Windows ou no cliente novo 212.

A seção acrescenta somente os nomes de serviço do lab a `/etc/hosts`, com bloco marcado e cópia anterior privada. Qualquer nome de destino já presente faz a preparação parar, mesmo que a entrada pareça correta: reveja sua origem antes de continuar.

O nome `srv-deb.lab.test` fica de fora: a instalação pode já associá-lo ao loopback `127.0.1.1`. Preservar essa entrada evita mudar a identidade local do servidor para resolver apenas nomes de serviço.

```bash
read -r -p 'VMID conferido no inventario: ' M19_GUEST_ID
case "$M19_GUEST_ID" in
  201) M19_GUEST_NAME=rocky-lab; M19_GUEST_IP=192.0.2.201 ;;
  202) M19_GUEST_NAME=debian-lab; M19_GUEST_IP=192.0.2.202 ;;
  204) M19_GUEST_NAME=srv-deb; M19_GUEST_IP=192.0.2.204 ;;
  *) exit 1 ;;
esac
test "$(hostname -s)" = "$M19_GUEST_NAME" || exit 1
ip -4 -o address show | awk -v ip="$M19_GUEST_IP/24" '$4 == ip {found=1} END {exit !found}' || exit 1
sudo bash -s -- "$M19_GUEST_ID" "$M19_GUEST_NAME" "$M19_GUEST_IP" <<'ROOT'
set -eu
case "$1:$2:$3" in
  201:rocky-lab:192.0.2.201|202:debian-lab:192.0.2.202|204:srv-deb:192.0.2.204) ;;
  *) exit 1 ;;
esac
test "$(hostname -s)" = "$2"
ip -4 -o address show | awk -v ip="$3/24" '$4 == ip {found=1} END {exit !found}'
test -f /etc/hosts
test ! -L /etc/hosts
test "$(stat -c '%u:%g:%a' /etc/hosts)" = 0:0:644
test ! -e /root/m19-hosts.before
test ! -L /root/m19-hosts.before
if grep -q '^# BEGIN M19 SERVICE NAMES$' /etc/hosts; then exit 1; fi
if awk '
  BEGIN {
    split("web.lab.test www.lab.test mail.lab.test proxy.lab.test smb.lab.test ns.lab.test app.lab.test", names, " ")
    for (n in names) target[names[n]]=1
  }
  {sub(/#.*/, ""); for (i=2; i<=NF; i++) if (target[tolower($i)]) found=1}
  END {exit !found}
' /etc/hosts; then
  printf '%s\n' 'STOP: a lab service name already exists in /etc/hosts' >&2
  exit 1
fi
cp -a /etc/hosts /root/m19-hosts.before
cat >> /etc/hosts <<'HOSTS'

# BEGIN M19 SERVICE NAMES
192.0.2.204 web.lab.test www.lab.test mail.lab.test proxy.lab.test smb.lab.test ns.lab.test
192.0.2.201 app.lab.test
# END M19 SERVICE NAMES
HOSTS
test "$(stat -c '%u:%g:%a' /etc/hosts)" = 0:0:644
for name in web.lab.test www.lab.test mail.lab.test proxy.lab.test smb.lab.test ns.lab.test; do
  test "$(getent ahostsv4 "$name" | awk '{print $1}' | sort -u)" = 192.0.2.204
done
test "$(getent ahostsv4 app.lab.test | awk '{print $1}' | sort -u)" = 192.0.2.201
diff -u /root/m19-hosts.before /etc/hosts || test "$?" -eq 1
ROOT
```

Se uma guarda interromper, não apague o arquivo nem ignore a condição. A cópia só é criada depois de conferir todos os nomes. Se a verificação final falhar, confira NSS e o bloco acrescentado; uma restauração exige comparar as mudanças posteriores antes de repor a cópia inteira.

`getent` consulta a resolução do sistema, que agora pode responder por arquivo local. Isso não comprova que o DNS da aula está correto. Continue consultando explicitamente o servidor DNS e compare o resultado com o registro planejado.

```bash
dig @192.0.2.204 web.lab.test A +short
dig @192.0.2.204 mail.lab.test A +short
dig @192.0.2.204 proxy.lab.test A +short
dig @192.0.2.204 app.lab.test A +short
getent ahostsv4 web.lab.test
getent ahostsv4 app.lab.test
```

A resolução estática mantém as aulas 19.4–19.9 independentes do DNS global da gestão nas VMs de trabalho. O cliente 212 não recebe esse bloco: o desafio exige que DHCP forneça o DNS do lab e que a resolução DNS real funcione.

## 5 · Continuidade e limites

Repita a preparação separadamente na outra VM. Preserve as duas interfaces para o M19; não remova a bridge. Na 19.3, apenas a VM 202 ensaia DHCP na placa isolada e depois retorna ao UUID estático registrado. A gestão nunca é cliente do DHCP de exercício.

A VM 204 foi preparada pela 19.1 com ifupdown e arquivo próprio; não instale NetworkManager nela para copiar este bloco. Seu arquivo `/etc/m19-lab.env` contém a interface e o endereço do servidor, sem credenciais.

O cliente Windows 11, quando usado, precisa estar previamente autorizado e conectado a esse segmento. Se não está disponível, registre o ramo Windows não realizado; não altere outra VM ou uma placa da rede real para improvisar esse acesso.

O novo cliente 212 será criado somente no desafio 19.9, com instalação independente e identidade nova. ID ocupado não é autorização para destruir o recurso existente. O DHCP não oferece saída para a Internet; mantenha o DVD oficial disponível para pacotes offline.

