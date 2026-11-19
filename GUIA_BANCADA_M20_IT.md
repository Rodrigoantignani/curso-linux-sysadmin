# Laboratorio comune del M20

Usa le VM esistenti `201` (`rocky-lab`) e `202` (`debian-lab`), con `student` e sudo. Crea soltanto la `240`, `ns8-1`, per NS8. La `241`, `ns8-2`, entra soltanto nella 20.7, per esercitarti con Move. Il corso termina con M20.

Non occorre aver svolto M19. Ogni nodo NS8 ha soltanto `net0` su `vmbr0`, indirizzo di gestione statico riservato, gateway e DNS esterno reali del lab. Usa la rete di gestione che permette già di raggiungere la 201/202; non creare un’altra rete e non modificare il computer personale.

## 1 · Inventario modificabile

Compila le variabili con gli IPv4 reali riservati nel tuo inventario. I campi vuoti sono intenzionali: non sono indirizzi di esempio da eseguire. Ripeti gli stessi valori quando cambi terminale. Nel laboratorio iniziale, lascia vuoto il secondo IP.

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

`NS8_IP` appartiene alla 240; `CLIENT_IP`, alla 202; `NS8_2_IP`, alla futura 241. Il nome breve del primo nodo è `ns8-1`, e il suo FQDN è `ns8-1.lab.test`; il secondo usa `ns8-2` e `ns8-2.lab.test`. Confronta `hostname -s` con il nome breve.

## 2 · Nomi privati senza un nuovo server DNS

Applica il blocco seguente sulla 202 e su NS8, dopo `sudo -i`, con le variabili compilate. Conserva una copia precedente e sostituisce soltanto il blocco M20. Se i nomi del lab esistono già fuori da quel blocco, fermati e riconcilia quei record prima di continuare.

```bash
m20_hosts() {
  case "$(hostname -s)" in debian-lab|ns8-1|ns8-2) ;; *) printf '%s\n' 'Fermati: terminale fuori dal laboratorio.'; return 1 ;; esac
  if [ "$(id -u)" -ne 0 ] || [ -z "$NS8_IP" ] || [ -z "$CLIENT_IP" ]; then
    printf '%s\n' 'Fermati: usa root e compila gli IP reali.'; return 1
  fi
  local candidate
  candidate=$(mktemp /etc/hosts.m20.XXXXXX) || return 1
  awk '/^# BEGIN M20$/{skip=1;next} /^# END M20$/{skip=0;next} !skip' /etc/hosts > "$candidate"
  if grep -Eq '(^|[[:space:]])(ns8-1|ns8-2|wiki)\.lab\.test([[:space:]]|$)' "$candidate"; then
    printf '%s\n' 'Fermati: nomi esistenti fuori dal blocco M20.'; rm -f -- "$candidate"; return 1
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

Questo file serve soltanto al resolver locale del sistema. Non fornisce DNS ai container né ad altri client. NS8 core non viene presentato come server DNS. Conserva il DNS esterno usato per Internet; se un servizio richiede risoluzione nei container, usa DNS di lab già autorizzato oppure limita l’attività alla verifica locale indicata.

## 3 · Browser e fiducia iniziale

Apri `https://IP-DE-GESTAO/cluster-admin/` nel browser della postazione di lab che raggiunge già la gestione. Sostituisci l’IP con il valore reale. Prima dell’eccezione iniziale del certificato, confronta l’impronta SHA-256 dalla console indipendente del nodo:

```bash
openssl s_client -connect 127.0.0.1:443 -servername ns8-1.lab.test </dev/null 2>/dev/null | openssl x509 -noout -subject -fingerprint -sha256
```

La 20.4 prepara la CA dello stesso M20 e l’accesso tramite nome. Una connessione tramite IP può continuare a mostrare un errore di nome: i certificati dell’esercizio coprono FQDN, non l’IP. Non disattivare la verifica TLS per aggirarlo.

Usa il browser della stessa 202: legge i nomi da hosts e permette di selezionare i file TLS locali da caricare. Se la 202 ha già un’interfaccia grafica, conserva la sua sessione. Se è minimale, prepara l’ambiente leggero seguente soltanto su di essa, come `student`. Il controllo impedisce di sovrascrivere una configurazione grafica esistente.

```bash
m20_navegador() {
  if [ "$(hostname -s)" != debian-lab ] || [ "$(id -un)" != student ]; then
    printf '%s\n' 'Fermati: usa student sulla 202.'; return 1
  fi
  if [ -e "$HOME/.xinitrc" ]; then printf '%s\n' 'Conserva l’ambiente grafico esistente; non sovrascrivere .xinitrc.'; return 1; fi
  sudo apt update && sudo apt install -y xserver-xorg xinit openbox xterm firefox-esr || return 1
  printf '#!/bin/sh\nxterm &\nexec openbox-session\n' > "$HOME/.xinitrc"
  chmod 0700 "$HOME/.xinitrc"
}
m20_navegador
```

Apri la console locale della 202 in Proxmox, accedi come `student` ed esegui `startx`; non avviare X tramite SSH né come root. Nell’xterm, apri `firefox-esr`. Usa il FQDN della Wiki e il pannello tramite nome o IP. Le verifiche da terminale restano disponibili con `curl --resolve`, conservando Host e SNI.

## 4 · Riprendere una lezione

| Lezione | Stato iniziale | Snapshot di base da preparare una volta |
| --- | --- | --- |
| 20.2 | Cluster con un nodo pronto | `m20a1-cluster`, sulla 240 |
| 20.3 / 20.4 | Wiki installata | `m20a2-wiki`, sulla 240 |
| 20.5 / 20.6 | TLS e CA di M20 pronti | `m20a4-tls` sulla 240 e `m20a4-cliente202` sulla 202 |
| 20.7 | Backup della Wiki verificato | `m20a6-backup`, sulla 240 e sulla 202 |

Gli snapshot non compaiono da soli: prepara una volta la base di M20, registra gli stati alla fine delle lezioni indicate e verifica l’inventario prima del ripristino. Non ripristinare un solo nodo a uno stato precedente dopo aver aggiunto il secondo; un rollback unilaterale può compromettere la coerenza del cluster.

La 20.6 crea la condivisione di backup sulla stessa 202, con l’utente `student`; nessuna configurazione Samba di un altro modulo è un prerequisito. Questa destinazione sullo stesso Ceph non protegge dalla perdita di Ceph.

Nessun comando è stato eseguito nelle VM durante la preparazione. Verifica rete, attività e risposte nel tuo laboratorio reale prima di considerare approvato un passaggio.

