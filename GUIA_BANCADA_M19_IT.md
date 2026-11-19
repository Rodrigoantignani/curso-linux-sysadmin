# Laboratorio comune del M19

Nomi del modulo: VM 201 e hostname rocky-lab; VM 202 e hostname debian-lab; VM 204 e hostname srv-deb; client temporaneo 212 e hostname m19-client. Nome Proxmox e hostname del guest sono impostazioni distinte: confrontali prima delle guardie. Gli alias DNS web, mail e proxy non rinominano la macchina.

Prima della 19.4, la VM 204 deve essere libera da installazioni precedenti di nginx e Apache. Le guardie che trovano pacchetti o configurazioni esistenti devono fermare il percorso: non rimuoverli automaticamente. Usa la VM nuova della 19.1 o riconcilia servizio, dati e dipendenze con l’inventario prima di riprendere.

Dopo la 19.1 e prima della 19.2, esegui le sezioni 1–3 sulle VM 201 e 202. Dopo la 19.3 e prima della 19.4, esegui la sezione 4 sulle VM 201, 202 e 204. I servizi restano nelle lezioni. Nessun comando di questo materiale è stato eseguito nelle VM durante la preparazione.

La rete didattica è la stessa della 17.5: `192.0.2.0/24`, esclusivamente su `vmbr17`, senza porta fisica, IP dell’host, gateway o NAT. È un blocco riservato alla documentazione, usato qui soltanto nel laboratorio isolato. Non distribuirlo in una rete instradata.

Prima di assegnare indirizzi, confronta inventario, rotte, VPN e reti di gestione. Se c’è una sovrapposizione, fermati e riprogetta coerentemente tutti i riferimenti del M19; non mescolare due reti nello stesso percorso.

| Macchina | Indirizzo isolato | Ruolo |
| --- | --- | --- |
| 204 · srv-deb | `192.0.2.204/24` | Server creato nella 19.1 |
| 201 · rocky-lab | `192.0.2.201/24` | Servizio Podman del M18 |
| 202 · debian-lab | `192.0.2.202/24` | Client di test; DHCP temporaneo nella 19.3 |
| 212 · m19-client | DHCP tra `.100` e `.149` | VM nuova soltanto nella sfida 19.9 |

Il dominio è `lab.test`. DNS, web, mail, proxy e Samba puntano alla VM 204; `app.lab.test` punta alla VM 201. Una zona di laboratorio non deve rivendicare il dominio pubblico di un’altra persona.

## Preparazione della bridge dopo M17

Se la pulizia della 17.7 ha rimosso `vmbr17`, ricreala sull’host autorizzato prima dei blocchi di rete di questa guida. Il comando qui sotto si esegue nella console root di Proxmox e riguarda soltanto la bridge dell’esercizio; non ricarica tutta la rete. Se l’inclusione di `interfaces.d` usa un altro schema, fermati e controlla la preparazione dell’host. Una bridge già esistente sarà solo controllata dai blocchi successivi.

Le VM 201, 202 e 204 devono trovarsi sullo **stesso host fisico** durante M19: bridge senza uplink con nomi uguali su host diversi non collegano la LAN isolata. Controlla i proprietari nell’inventario prima di assegnare indirizzi; non migrare carichi per tentativi.

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

## 1 · Controllare l’host e aggiungere una scheda scollegata

Nel Proxmox autorizzato, individua il nodo proprietario nell’inventario. Ripeti il blocco per una VM alla volta sul suo nodo; non applicare comandi destinati alle VM dentro l’hypervisor.

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

Il bridge deve esistere su questo nodo e non può avere uplink fisico né indirizzo dell’host. Se una scheda o un profilo esiste già, conservalo e riesamina lo stato; questa guida non autorizza la sostituzione di una risorsa esistente. Lo snapshot protegge la VM, non la configurazione dell’host.

Copia il MAC di `net1` e conserva la cartella dei riscontri fuori dalla VM. La nuova scheda deve apparire nel guest; se la versione o l’hardware richiede un avvio a freddo, spegni e accendi soltanto la VM identificata dopo aver concordato la finestra, conservando la gestione.

## 2 · Preparare il profilo dentro la VM

Dentro la VM scelta, entra come `student`. Controlla hostname, indirizzo di gestione e rotta predefinita prima di modificare la nuova scheda. L’interfaccia si identifica tramite il MAC, mai dalla posizione in un elenco.

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

Il file contiene soltanto valori prodotti da te, senza password. Non caricare file ricevuti da una rete come script d’ambiente. La configurazione non aggiunge gateway né DNS alla scheda isolata; le prime query usano esplicitamente il server DNS.

## 3 · Collegare soltanto il cavo della nuova scheda

Torna nello stesso terminale Proxmox, con le variabili controllate. Non ricostruire la scheda omettendo MAC o bridge; conserva tutte le proprietà e cambia soltanto il link.

```bash
test "$(qm config "$M19_ID" | sed -n 's/^name: //p')" = "$M19_NAME" || exit 1
M19_NET1=$(qm config "$M19_ID" | sed -n 's/^net1: //p') || exit 1
case ",$M19_NET1," in *,bridge=vmbr17,*) ;; *) exit 1 ;; esac
case ",$M19_NET1," in *,link_down=1,*) ;; *) exit 1 ;; esac
M19_NET1=$(printf '%s' "$M19_NET1" | sed -E 's/,link_down=1//g')
qm set "$M19_ID" --net1 "$M19_NET1,link_down=0" || exit 1
qm config "$M19_ID"
```

Dentro la VM usa la sessione e il profilo appena creato.

```bash
sudo nmcli connection up uuid "$LAB_UUID" || exit 1
ip -br address show dev "$LAB_IF"
ip -4 route show default > "$HOME/m19-lab/default-after.txt"
cmp "$HOME/m19-lab/default-before.txt" "$HOME/m19-lab/default-after.txt" || exit 1
ip route get 192.0.2.204
ping -c 3 192.0.2.204
nmcli -f connection.uuid,connection.interface-name,ipv4.addresses,ipv4.gateway,ipv4.never-default connection show uuid "$LAB_UUID"
```

L’indirizzo isolato deve corrispondere alla VM e il percorso verso la VM 204 deve usare quella scheda. La rotta predefinita resta uguale. Un ping fallito non autorizza a disabilitare il firewall: controlla indirizzo, cavo e politica con i riscontri reali.

## 4 · Preparare i nomi statici prima della 19.4

Esegui questa sezione una volta su ciascuna VM 201, 202 e 204, dopo aver verificato l’identità nell’inventario Proxmox e l’indirizzo isolato nel guest. Non modifica il DNS della gestione né richiede di sostituire il resolver di sistema. Non eseguirla sull’host Proxmox, su Windows o sul nuovo client 212.

La sezione aggiunge soltanto i nomi di servizio del lab a `/etc/hosts`, con un blocco marcato e una copia precedente privata. Qualsiasi nome di destinazione già presente interrompe la preparazione, anche se la voce sembra corretta: riesaminane l’origine prima di continuare.

Il nome `srv-deb.lab.test` resta escluso: l’installazione può averlo già associato al loopback `127.0.1.1`. Conservare quella voce evita di modificare l’identità locale del server per risolvere soltanto nomi di servizio.

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

Se un controllo interrompe il lavoro, non eliminare il file e non ignorare la condizione. La copia viene creata soltanto dopo aver controllato tutti i nomi. Se la verifica finale fallisce, controlla NSS e il blocco aggiunto; un ripristino richiede di confrontare le modifiche successive prima di rimettere l’intera copia.

`getent` consulta la risoluzione del sistema, che ora può rispondere tramite un file locale. Questo non dimostra che il DNS della lezione sia corretto. Continua a interrogare esplicitamente il server DNS e confronta il risultato con il record previsto.

```bash
dig @192.0.2.204 web.lab.test A +short
dig @192.0.2.204 mail.lab.test A +short
dig @192.0.2.204 proxy.lab.test A +short
dig @192.0.2.204 app.lab.test A +short
getent ahostsv4 web.lab.test
getent ahostsv4 app.lab.test
```

La risoluzione statica rende le lezioni 19.4–19.9 indipendenti dal DNS globale della gestione sulle VM di lavoro. Il client 212 non riceve questo blocco: la sfida richiede che DHCP fornisca il DNS del lab e che la vera risoluzione DNS funzioni.

## 5 · Continuità e limiti

Ripeti separatamente la preparazione sull’altra VM. Conserva entrambe le interfacce per il M19; non rimuovere il bridge. Nella 19.3 soltanto la VM 202 prova DHCP sulla scheda isolata e poi torna all’UUID statico registrato. La gestione non diventa mai client del DHCP dell’esercizio.

La VM 204 è stata preparata dalla 19.1 con ifupdown e un file dedicato; non installare NetworkManager su quella VM per copiare questo blocco. Il suo file `/etc/m19-lab.env` contiene interfaccia e indirizzo del server, senza credenziali.

Il client Windows 11, quando usato, deve essere già autorizzato e collegato a questo segmento. Se non è disponibile, registra il ramo Windows non eseguito; non modificare un’altra VM o una scheda della rete reale per improvvisare l’accesso.

Il nuovo client 212 sarà creato soltanto nella sfida 19.9, con installazione indipendente e identità nuova. Un ID occupato non autorizza la distruzione della risorsa esistente. Il DHCP non offre uscita verso Internet; mantieni disponibile il DVD ufficiale per i pacchetti offline.

