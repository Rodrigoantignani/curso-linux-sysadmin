# Bancada comum do M20

Use as VMs existentes `201` (`rocky-lab`) e `202` (`debian-lab`), com `student` e sudo. Crie somente a `240`, `ns8-1`, para o NS8. A `241`, `ns8-2`, entra apenas na 20.7, para praticar Move. O curso termina no M20.

Não é preciso ter feito o M19. Cada nó NS8 tem somente `net0` em `vmbr0`, endereço de gestão estático reservado, gateway e DNS externo reais do lab. Use a rede de gestão que já permite acessar a 201/202; não crie uma rede adicional nem altere o computador pessoal.

## 1 · Inventário editável

Preencha as variáveis com os IPv4 reais reservados no seu inventário. Os campos vazios são intencionais: não são endereços de exemplo para executar. Repita os mesmos valores quando mudar de terminal. Na bancada inicial, deixe o segundo IP vazio.

```bash
NS8_IP=''
CLIENT_IP=''
NS8_2_IP=''
NS8_FQDN=ns8-1.lab.test
NS8_2_FQDN=ns8-2.lab.test
WIKI_FQDN=wiki.lab.test
WIKI_IP=''
M20_VMID=240
```

`NS8_IP` pertence à 240; `CLIENT_IP`, à 202; `NS8_2_IP`, à futura 241. O nome curto do primeiro nó é `ns8-1`, e seu FQDN é `ns8-1.lab.test`; o segundo usa `ns8-2` e `ns8-2.lab.test`. Compare `hostname -s` com o nome curto.

## 2 · Nomes privados sem servidor DNS novo

Aplique o bloco abaixo na 202 e no NS8, após `sudo -i`, com as variáveis preenchidas. Ele mantém uma cópia anterior e substitui apenas o bloco M20. Se já houver nomes do lab fora desse bloco, pare e reconcilie esses registros antes de continuar.

```bash
m20_hosts() {
  case "$(hostname -s)" in debian-lab|ns8-1|ns8-2) ;; *) printf '%s\n' 'Pare: terminal fora da bancada.'; return 1 ;; esac
  if [ "$(id -u)" -ne 0 ] || [ -z "$NS8_IP" ] || [ -z "$CLIENT_IP" ]; then
    printf '%s\n' 'Pare: use root e preencha os IPs reais.'; return 1
  fi
  local candidate
  candidate=$(mktemp /etc/hosts.m20.XXXXXX) || return 1
  awk '/^# BEGIN M20$/{skip=1;next} /^# END M20$/{skip=0;next} !skip' /etc/hosts > "$candidate"
  if grep -Eq '(^|[[:space:]])(ns8-1|ns8-2|wiki)\.lab\.test([[:space:]]|$)' "$candidate"; then
    printf '%s\n' 'Pare: nomes existentes fora do bloco M20.'; rm -f -- "$candidate"; return 1
  fi
  printf '\n# BEGIN M20\n%s %s ns8-1\n%s %s\n' "$NS8_IP" "$NS8_FQDN" "${WIKI_IP:-$NS8_IP}" "$WIKI_FQDN" >> "$candidate"
  if [ -n "$NS8_2_IP" ]; then printf '%s %s ns8-2\n' "$NS8_2_IP" "$NS8_2_FQDN" >> "$candidate"; fi
  printf '# END M20\n' >> "$candidate"
  cp -an /etc/hosts /etc/hosts.before-m20
  install -m 0644 -o root -g root "$candidate" /etc/hosts && rm -f -- "$candidate"
}
m20_hosts
getent ahostsv4 "$NS8_FQDN"
getent ahostsv4 "$WIKI_FQDN"
```

Esse arquivo atende somente o resolvedor local do sistema. Ele não fornece DNS aos contêineres nem a outros clientes. O NS8 core não é apresentado como servidor DNS. Preserve o DNS externo usado para a Internet; se um serviço exigir resolução dentro de contêiner, forneça DNS de lab já autorizado ou limite a atividade à prova local indicada.

## 3 · Navegador e confiança inicial

Abra `https://IP-DE-GESTAO/cluster-admin/` no navegador da estação de lab que já alcança a gestão. Substitua o IP pelo valor real. Antes da exceção inicial de certificado, compare a impressão SHA-256 pelo console independente do nó:

```bash
openssl s_client -connect 127.0.0.1:443 -servername ns8-1.lab.test </dev/null 2>/dev/null | openssl x509 -noout -subject -fingerprint -sha256
```

A 20.4 estabelece a CA do próprio M20 e o acesso pelo nome. Uma conexão pelo IP pode continuar mostrando erro de nome: os certificados do exercício cobrem FQDNs, não o IP. Não desligue a verificação TLS para contornar isso.

Use o navegador da própria 202: ele lê os nomes do hosts e permite selecionar os arquivos TLS locais para upload. Se a 202 já tem interface gráfica, preserve sua sessão. Se é mínima, prepare o ambiente leve abaixo somente nela, como `student`. A guarda impede sobrescrever uma configuração gráfica existente.

```bash
m20_navegador() {
  if [ "$(hostname -s)" != debian-lab ] || [ "$(id -un)" != student ]; then
    printf '%s\n' 'Pare: use student na 202.'; return 1
  fi
  if [ -e "$HOME/.xinitrc" ]; then printf '%s\n' 'Preserve o ambiente gráfico existente; não sobrescreva .xinitrc.'; return 1; fi
  sudo apt update && sudo apt install -y xserver-xorg xinit openbox xterm firefox-esr || return 1
  printf '#!/bin/sh\nxterm &\nexec openbox-session\n' > "$HOME/.xinitrc"
  chmod 0700 "$HOME/.xinitrc"
}
m20_navegador
```

Abra o console local da 202 no Proxmox, entre como `student` e rode `startx`; não inicie X por SSH nem como root. No xterm, abra `firefox-esr`. Use o FQDN da Wiki e o painel pelo nome ou IP. Os testes de terminal continuam disponíveis com `curl --resolve`, preservando Host e SNI.

## 4 · Retomar uma aula

| Aula | Estado de entrada | Snapshot-base a preparar uma vez |
| --- | --- | --- |
| 20.2 | Cluster de um nó pronto | `m20a1-cluster`, na 240 |
| 20.3 / 20.4 | Wiki instalada | `m20a2-wiki`, na 240 |
| 20.5 / 20.6 | TLS e CA do M20 prontos | `m20a4-tls` na 240 e `m20a4-cliente202` na 202 |
| 20.7 | Backup da Wiki conferido | `m20a6-backup`, na 240 e na 202 |

Snapshots não aparecem sozinhos: prepare a base do M20 uma vez, registre os estados ao fim das aulas indicadas e confira o inventário antes de restaurar. Não restaure um único nó para um estado anterior depois de ingressar o segundo; rollback unilateral pode quebrar a coerência do cluster.

A 20.6 cria o compartilhamento de backup na própria 202, com o usuário `student`; nenhuma configuração Samba de outro módulo é pré-requisito. Esse destino no mesmo Ceph não protege contra a perda do Ceph.

Nenhum comando foi executado nas VMs durante a elaboração. Confira rede, tarefas e respostas na sua bancada real antes de considerar uma etapa aprovada.

