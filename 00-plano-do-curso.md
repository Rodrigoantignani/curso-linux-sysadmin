# Curso Linux Sysadmin

Oct 30, 2026 · revisado em Nov 9, 2026 · @RODRIGO ANTIGNANI COUTINHO

## O objetivo

Trabalhar com fluência em Rocky Linux, Debian e Proxmox, e operar por dentro o NethServer 8 e o NethSecurity. O curso não leva a nenhuma prova: LPI e Red Hat servem só como programa, uma lista de assuntos para não deixar buraco. O mercado pede quem resolve, e é isso que o curso treina.

| Alvo | O que fluência quer dizer aqui | Onde |
| --- | --- | --- |
| Rocky e Debian | Administrar as duas famílias sem consultar a cada passo e saber por que cada comando funciona | M0 a M16 |
| Proxmox | Criar, migrar, fazer backup e restaurar pela linha de comando; entender storage, rede e quorum | M17 e M33 |
| NethServer 8 | Ler um módulo por dentro e diagnosticar Mail, WebTop, Nextcloud e NethVoice | M18 a M21 |
| NethSecurity | Firewall, VPN, DHCP e DNS em cima do OpenWrt, a terceira família do curso | M22 |
| Operação | Ver o problema antes do usuário, automatizar o que repete e reconstruir depois do desastre | M23 a M34 |

**Você domina um assunto quando:**

1. Faz a tarefa sem consultar, nas duas distros quando o assunto existe nas duas.
2. Explica por que funciona, com as suas palavras.
3. Conserta quando outra pessoa quebra.
4. O resultado sobrevive ao reboot.

**O que não muda:** tirar as provas do calendário não tirou nada de Linux do programa. Tudo o que um sysadmin usa continua aqui: shell, texto, boot, kernel, pacotes, armazenamento, usuários, rede, segurança, agendamento, logs, e-mail, impressão, interface gráfica, serviços, contêineres, automação, monitoramento, backup, desempenho, alta disponibilidade e troubleshooting. E toda aula, de Linux ou de produto, tem case real, lab, quebre e conserte.

## Como o curso funciona

Cada aula leva de 60 a 90 minutos e segue sempre o mesmo roteiro: lembrar, entender, fazer nas duas distros, quebrar, consertar e provar que aprendeu. O curso vai do zero até a operação profissional.

As aulas ficam em [`aulas/`](aulas/), um arquivo por aula, e o [índice de aulas](01-aulas.md) mostra a ordem, a semana e o que cada uma cobre. As 37 primeiras já estão escritas; as demais estão planejadas neste documento.

**Os princípios por trás de cada aula**

| Princípio | O que você faz | Por que funciona |
| --- | --- | --- |
| Partir de um case | Começa cada aula por um problema real de sysadmin | O comando fica guardado junto com a situação em que ele resolve |
| Recuperar antes de reler | Abre a aula respondendo 3 perguntas das anteriores, sem consultar | Puxar da memória fixa muito mais do que reler |
| Espaçar | Revisa os flashcards em D+1, D+3, D+7 e D+21 | Revisar quando já está quase esquecendo fortalece a lembrança |
| Prever antes de rodar | Escreve o que espera ver antes de cada comando novo | O erro de previsão mostra exatamente o que você não sabia |
| Intercalar | Faz tudo no Rocky e no Debian, lado a lado | Comparar obriga a entender o princípio, não a decorar o comando |
| Do resolvido ao sozinho | Lab guiado primeiro, depois desafio com menos ajuda | A ajuda diminui conforme a habilidade cresce |
| Quebre e conserte | Diagnostica um defeito plantado no fim de cada aula | Troubleshooting é o trabalho real |
| Explicar com suas palavras | Explica o conceito ao DeepTutor e pede crítica | Quem explica descobre as próprias lacunas |
| Ponte Windows | Liga cada conceito ao equivalente no Windows Server | Quem já administra Windows aprende mais rápido; quem nunca administrou pode pular |

**Anatomia de uma aula**

1. Ficha: objetivos, referência no programa, pré-requisitos e tempo.
2. Aquecimento: 3 perguntas de revisão, sem consulta.
3. Por que importa: um case real de sysadmin.
4. Modelo mental: analogia e desenho.
5. Conceito em camadas: o essencial, o aprofundamento e a referência no programa.
6. Rocky × Debian: a tabela das diferenças.
7. Lab guiado: snapshot antes; cada passo com previsão, comando, saída esperada e verificação.
8. Quebre e conserte: um defeito para diagnosticar sozinho.
9. Armadilhas: os erros mais comuns e como evitá-los.
10. Quiz com gabarito comentado.
11. Flashcards e cola de comandos.
12. Checklist de saída e snapshot de fim.
13. Com o DeepTutor: prompts prontos para aprofundar.

Essa anatomia vale para todas as aulas, inclusive as de Proxmox, NS8 e NethSecurity.

As aulas já escritas trazem seções "O que cai na prova" e "Itens de prova". Continuam valendo como referência do programa; leia como lista de assuntos.

**Quem faz o quê**

| Quem | Papel |
| --- | --- |
| Claude | Escreve as aulas, revisa labs e corrige o rumo quando você pedir |
| DeepTutor (Haiku 5.5) | Tira dúvidas na hora, gera exercícios extras, aplica quizzes e explica erros |
| Você | Faz os labs, mantém o diário de bordo e responde os quizzes sem olhar |

**Regras do laboratório**

- Snapshot antes de cada lab, sempre. Errar no lab é barato; em produção, não.
- Nenhum lab em servidor de cliente ou de produção. NethServer, NethSecurity e PBX de produção só servem para leitura e comparação.
- Diário de bordo: comando, o que esperava, o que aconteceu, o que aprendeu.
- Leia a mensagem de erro inteira antes de pesquisar. Quase sempre ela já diz a causa.
- NS8 e NethSecurity mudam rápido. Antes de escrever cada aula desses módulos, comandos e caminhos são conferidos na documentação da versão em uso.

## As provas como programa

Nenhuma prova faz parte do calendário. Elas continuam aqui porque cada uma publica uma lista de objetivos detalhada, útil para conferir se faltou algum assunto. As tabelas de M0 a M16 mostram esse vínculo na coluna **Programa**; de M17 em diante, a coluna **Serve para** diz onde aquilo aparece no trabalho.

| Programa | Onde entra | Como o curso usa |
| --- | --- | --- |
| Linux Essentials 010-200 (versão 2.0) | M0 a M2 | Checklist dos fundamentos |
| LPIC-1 101-500 e 102-500 (versão 5.0) | M3 a M15 | Cobertura completa e neutra das duas famílias, com impressão e interfaces gráficas |
| RHCSA EX200 (RHEL 10) | M3 a M16 | Referência do que um administrador faz sozinho e faz sobreviver ao reboot |
| EX294, RHCE em Ansible | M23 a M26 | Ansible completo, aplicado a Rocky e Debian |
| EX342, RHCE em Enterprise Linux | M28, M30, M32 e M34 | Método de diagnóstico e lista de falhas para treinar |

Se um dia você decidir fazer alguma prova, releia os objetivos oficiais 30 dias antes, porque elas mudam, e peça ao DeepTutor um `!simulado` no formato dela. Os objetivos abaixo foram conferidos em 30/10/2026.

**Fontes oficiais**

- [Linux Essentials](https://www.lpi.org/our-certifications/linux-essentials-overview/) e [objetivos da prova 010](https://www.lpi.org/our-certifications/exam-010-objectives/)
- [LPIC-1](https://www.lpi.org/our-certifications/lpic-1-overview/)
- [RHCSA, prova EX200](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam)
- [RHCE em Ansible](https://www.redhat.com/en/services/certification/red-hat-certified-engineer-in-ansible) e [prova EX294](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux)
- [RHCE em Enterprise Linux](https://www.redhat.com/en/services/certification/red-hat-certified-engineer-in-enterprise-linux) e [prova EX342](https://www.redhat.com/en/services/training/ex342-red-hat-certified-specialist-linux-diagnostics-and-troubleshooting)
- [NethServer 8, manual do administrador](https://docs.nethserver.org/docs/administrator-manual/) e [manual do desenvolvedor](https://nethserver.github.io/ns8-core/)
- [NethSecurity, manual do administrador](https://docs.nethsecurity.org/docs/administrator-manual)

## Laboratório no Proxmox

O lab mora num servidor Proxmox e cresce junto com o curso: começa com duas VMs e termina como uma pequena infraestrutura. O curso só usa os VMIDs da tabela abaixo. Qualquer outra VM ou contêiner que já exista no seu ambiente fica fora do curso: não mexa neles.

| VMID | Nome | Sistema | Recursos | Entra em | Para quê |
| --- | --- | --- | --- | --- | --- |
| 201 | rocky-lab | Rocky Linux 9 | 2 vCPU, 2 GB, 20 GB | M0 | Lado Red Hat das aulas; mesma base do NethServer 8 |
| 202 | debian-lab | Debian 13 | 2 vCPU, 2 GB, 20 GB | M0 | Lado Debian das aulas; mesma base do Proxmox |
| 203 | srv-lab | Rocky Linux 9 | 2 vCPU, 2 GB, 20 GB | M13 | Servidor NFS; depois Git e logs centralizados |
| 204 | srv-deb | Debian 13 | 2 vCPU, 2 GB, 20 GB | M19 | DNS, DHCP, web, Samba, e-mail e Zabbix |
| 205 | rocky10-lab | Rocky Linux 10 | 2 vCPU, 2 GB, 20 GB | M16 | O próximo Rocky e os incidentes de M16 e M34 |
| 210 a 212 | ans-ctl, ans-n1, ans-n2 | Rocky 10 no controle e no n1; Debian 13 no n2 | ans-ctl com 4 GB; nós com 2 GB | M24 | Ansible: o mesmo playbook nas duas famílias |
| 220 a 222 | ha-1, ha-2, ha-3 | Rocky Linux 10 | 2 vCPU, 2 GB | M31 | Pacemaker, HAProxy e keepalived |
| 230 a 232 | pve-n1, pve-n2, pve-n3 | Proxmox VE 9 | 2 vCPU tipo host, 4 GB, 2 discos | M33 | Cluster Proxmox com Ceph aninhado, para treinar sem tocar no cluster real |
| 240 | ns8-1 | Rocky Linux 9 + NS8 | 4 vCPU, 8 GB, 80 GB | M20 | Líder do cluster NS8 e aplicações |
| 241 | ns8-2 | Rocky Linux 9 + NS8 | 2 vCPU, 4 GB, 40 GB | M20 | Segundo nó, para mover módulos e treinar falhas |
| 250 | nsec-1 | NethSecurity | 2 vCPU, 2 GB, 16 GB, 2 placas | M22 | Firewall, DHCP, DNS e VPN |
| 251 | nsec-2 | NethSecurity | 2 vCPU, 2 GB, 16 GB, 2 placas | M22 | Outra ponta dos túneis |

Antes de criar as VMs 240 em diante, confira com `qm list` e `pvesh get /cluster/resources --type vm` se os IDs estão livres.

**Padrão de toda VM do curso**

- CPU `x86-64-v2-AES` para Rocky 9 e Debian 13. O Rocky 10 exige `x86-64-v3`: antes da VM 205, confira se todos os nós têm AVX2 com `grep -c avx2 /proc/cpuinfo` (resultado maior que zero). Se algum nó não tiver, use Rocky 9 nas VMs 205 em diante; quase tudo funciona igual.
- Máquina q35 com UEFI (OVMF), disco no `vm-hdd` (Ceph RBD), placa virtio na `vmbr0`.
- Guest agent ligado na VM e o pacote `qemu-guest-agent` instalado no sistema.
- Senha de root definida nas duas distros: o modo de emergência pede essa senha.
- SSH sempre com o seu usuário. Root não entra por senha via SSH, que é o padrão das duas distros.
- Servidores do lab (VM 203 em diante) usam IP fixo fora da faixa do DHCP da `vmbr0`.
- O NethServer 8 roda em VM. Contêiner LXC do Proxmox não é suportado.
- O NethSecurity usa imagem própria: o M22 confere na documentação o tipo de disco e de firmware antes de criar a VM.

**Snapshots: a rede de proteção**

- Nome no formato `mXaY-inicio` e `mXaY-fim`, por exemplo `m2a3-inicio`. Só letras, números, hífen e sublinhado, começando por letra.
- Antes de cada lab: `qm snapshot 201 m2a3-inicio`, e o mesmo na 202.
- Deu errado: `qm rollback 201 m2a3-inicio` devolve a VM ao ponto salvo.
- No fim de cada módulo, apague os snapshots intermediários e guarde só o último `-fim`.

**Backup no PBS**

- Um job semanal em Datacenter → Backup para as VMs do curso, no `PBS-LAB`, modo snapshot.
- Antes de aula arriscada (4.4, módulo 9, módulo 26), um backup manual: `vzdump 201 --storage PBS-LAB --mode snapshot`.
- Snapshot não é backup: o snapshot mora no mesmo storage da VM; o backup no PBS sobrevive se esse storage cair.

**Rede isolada:** um servidor DHCP de teste na `vmbr0` pode entregar IP errado para a rede inteira. Na aula 17.5 você cria uma rede só do lab (bridge sem porta física ou VNet do SDN). O Kea da aula 19.3 e a LAN das VMs 250 e 251 ficam nela, nunca na `vmbr0`.

## Fase 1 · Fundamentos

Semanas 1 a 6 · 20 aulas · fecha com um dia de incidente.

Meta da fase: usar o terminal com segurança e entender o que cada comando faz por baixo, nas duas distros. Quem termina a fase navega, manipula texto, escreve scripts simples, entende processos, rede, usuários e permissões.

**Pré-teste de dispensa.** Já domina o assunto de uma aula? Faça o aquecimento e o quebre e conserte. Acertou tudo sem consultar nada: leia só o modelo mental e siga em frente. Na Fase 1 isso vai acontecer bastante.

**M0 · Laboratório** · 2 aulas · semana 1

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 0.1 Montar o laboratório | Cria as VMs 201 e 202 pela linha de comando do Proxmox, instala Rocky 9 e Debian 13 entendendo cada tela do instalador e confere o resultado | LE 014.1 |
| 0.2 Acesso e proteção | SSH do Windows com chave Ed25519, sudo nas duas VMs, guest agent, snapshots e backup no PBS com teste de restauração | LE 015.1 · RHCSA SSH |

Desafio do módulo: quebrar uma VM de propósito e voltar pelo snapshot em menos de dois minutos.

**M1 · Linha de comando** · 10 aulas · semanas 1 a 3

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 1.1 O que é Linux | Kernel, distribuição e famílias; identificar qualquer Linux em 30 segundos; Proxmox, NethServer 8 e NethSecurity no mapa | LE 011.1, 011.4 |
| 1.2 O shell e a ajuda | Anatomia de um comando, builtin e programa, PATH, man e suas seções, apropos, info, /usr/share/doc, histórico e atalhos | LE 012.1, 012.2 · LPIC 103.1 · RHCSA ajuda |
| 1.3 Caminhos e navegação | Árvore de diretórios, caminhos absolutos e relativos, cd, ls, curingas, arquivos ocultos | LE 012.3 |
| 1.4 Criar, copiar, mover e apagar | mkdir, touch, cp, mv e rm com segurança; por que o terminal não tem lixeira | LE 012.4 · LPIC 103.3 · RHCSA arquivos |
| 1.5 Ler e procurar texto | cat, less, head, tail -f, wc e grep básico; ler log sem abrir editor | LE 013.2 · RHCSA grep |
| 1.6 Redirecionamentos e pipes | stdin, stdout e stderr; `>`, `>>`, `2>`, `2>&1`, pipe e tee; montar um comando por partes | LE 013.2 · LPIC 103.4 · RHCSA redirecionamento |
| 1.7 Arquivar e compactar | tar com gzip, bzip2 e xz, zip; listar e testar antes de extrair | LE 013.1 · RHCSA tar |
| 1.8 Primeiro script | Shebang, variáveis, aspas, argumentos `$1` e `$#`, permissão de execução | LE 013.3 · RHCSA scripts |
| 1.9 Scripts que decidem e repetem | Código de saída, test e `[ ]`, if, for, while, `$(comando)` | LE 013.3 · RHCSA scripts |
| 1.10 Software livre na prática | Licenças GPL, MIT e Apache, aplicações open source que importam, modelos de negócio, Linux na nuvem | LE 011.2, 011.3, 011.4 |

Desafio do módulo: um script `inventario.sh` que mostra nome, distro, kernel, IP, memória e disco livre, com a mesma saída nas duas VMs.

**M2 · Sistema, usuários e permissões** · 8 aulas · semanas 4 e 5

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 2.1 Instalação e provisionamento | Instalação manual, imagem de nuvem com cloud-init, VM e container: quando usar cada um | LE 014.1, 011.4 |
| 2.2 Hardware e dispositivos | /dev, lsblk, lspci, lsusb e dmesg; como o Linux enxerga disco, rede e USB | LE 014.2 |
| 2.3 Processos e logs | ps, top, kill, systemctl status e journalctl; quem está usando a CPU e por quê | LE 014.3 · RHCSA logs |
| 2.4 Rede no dia a dia | ip, ss, ping, getent, dig e /etc/hosts; o caminho de um pacote até a internet | LE 014.4 |
| 2.5 Acesso remoto e privilégios | ssh, scp, sftp, su e sudo; transferir arquivos com segurança | LE 015.1 · RHCSA transferência segura |
| 2.6 Usuários e grupos | /etc/passwd, /etc/group, id, useradd e passwd; grupo primário e suplementar | LE 015.2 · RHCSA usuários |
| 2.7 Permissões e dono | rwx em arquivo e em diretório, chmod simbólico e octal, chown, umask | LE 015.3 · RHCSA permissões |
| 2.8 Diretórios e arquivos especiais | /tmp e sticky bit, SUID e SGID, links simbólicos, /proc, /sys e /dev | LE 015.4 · RHCSA links |

Desafio do módulo: uma pasta /srv/equipe onde dois usuários criam e editam arquivos, mas nenhum apaga o arquivo do outro, nas duas VMs.

**Fechamento da fase (semana 6):** revisão espaçada de M0 a M2 e um dia de incidente nas duas VMs, sem consulta.

## Fase 2 · Administrador

Semanas 7 a 22 · 63 aulas · fecha com um incidente com relógio no Rocky 10 e no Debian 13.

Meta da fase: administrar sozinho um servidor Linux de ponta a ponta, nas duas famílias, com tudo sobrevivendo ao reboot. A fase tem três blocos: a base do sistema, o servidor em rede e a prova de que você absorveu. Todo lab termina com reboot e verificação.

### Bloco A · a base do sistema

**M3 · Texto e editor** · 5 aulas · semanas 7 e 8

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 3.1 Fluxos a fundo | tee, xargs, here-doc, substituição de processo e /dev/null; pipelines que não escondem erro | LPIC 103.4 · RHCSA redirecionamento |
| 3.2 Filtros de texto | cut, sort, uniq, tr, paste, nl, split, od e sha256sum; transformar log em relatório | LPIC 103.2 |
| 3.3 Expressões regulares e grep | BRE e ERE, âncoras, classes e grupos; grep -E, -v, -o e -r | LPIC 103.7 · RHCSA grep e regex |
| 3.4 sed e awk | Substituir, apagar e extrair linhas com sed; colunas, filtros e somas com awk | LPIC 103.2, 103.7 |
| 3.5 vi e vim de verdade | Modos, movimentos, busca e substituição, desfazer; editar configuração sem medo | LPIC 103.8 · RHCSA editar arquivos |

Desafio do módulo: os 10 IPs que mais erraram senha no SSH, numa linha de comando, nas duas VMs. A Rocky guarda isso em /var/log/secure; a Debian, só no journal.

**M4 · Boot e systemd** · 4 aulas · semanas 8 e 9

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 4.1 Como o Linux liga | UEFI, GRUB 2, kernel, initramfs e systemd; ler o boot com journalctl -b e systemd-analyze | LPIC 101.2 |
| 4.2 systemd: serviços e units | start, stop, enable e mask; dependências e overrides com systemctl edit | LPIC 101.3 · RHCSA serviços |
| 4.3 Targets, desligar e reiniciar | multi-user e graphical, target padrão, rescue e emergency, shutdown e wall | LPIC 101.3 · RHCSA targets |
| 4.4 GRUB e acesso de emergência | Parâmetros do kernel com grubby e update-grub; interromper o boot e recuperar a senha de root | LPIC 102.2 · RHCSA bootloader e recuperação |

Desafio do módulo: recuperar a senha de root das duas VMs sem rollback, incluindo o relabel do SELinux na Rocky. A aula 4.4 pede backup no PBS antes.

**M5 · Hardware, kernel e virtualização** · 3 aulas · semana 9

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 5.1 Hardware pelo kernel | /proc, /sys, udev, lspci -k, lsusb, lsblk e dmesg; o que é um driver | LPIC 101.1 |
| 5.2 Módulos e parâmetros | lsmod, modinfo, modprobe, blacklist e sysctl persistente | LPIC 101.1 · EX342 kernel |
| 5.3 Linux como convidado | virtio, guest agent, cloud-init, clones e machine-id; VM e container lado a lado | LPIC 102.6 |

Desafio do módulo: clonar a VM 202 e dar ao clone identidade própria: hostname, machine-id e chaves SSH do host.

**M6 · Software** · 5 aulas · semanas 10 e 11

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 6.1 Pacotes no Debian | dpkg e apt: instalar, remover, purgar, descobrir qual pacote trouxe um arquivo; fontes no formato deb822 | LPIC 102.4 |
| 6.2 Pacotes na Rocky | rpm e dnf: instalar, remover, consultar, histórico e desfazer | LPIC 102.5 · RHCSA pacotes |
| 6.3 Repositórios | Arquivos .repo, chaves GPG, EPEL, repositório local a partir da ISO | LPIC 102.4, 102.5 · RHCSA repositórios |
| 6.4 Flatpak | Remotes, instalar e remover aplicações, Flathub; quando faz sentido num servidor | RHCSA Flatpak |
| 6.5 Bibliotecas compartilhadas | ldd, ldconfig e /etc/ld.so.conf.d; o erro "cannot open shared object file" | LPIC 102.3 · EX342 bibliotecas |

Desafio do módulo: a VM 201 instala pacotes sem internet, só com a ISO como repositório.

**M7 · Processos e desempenho** · 3 aulas · semana 11

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 7.1 Processos e sinais | ps, top, pgrep, pkill, kill e os sinais; estados e zumbis | LPIC 103.5 · RHCSA processos |
| 7.2 Jobs e sessões | &, jobs, fg, bg, nohup e tmux; tarefa longa que sobrevive à queda do SSH | LPIC 103.5 |
| 7.3 Prioridade e perfis | nice, renice e tuned-adm; achar e conter o processo que devora CPU ou memória | LPIC 103.6 · RHCSA prioridade e tuned |

Desafio do módulo: um processo misterioso devora CPU e memória. Ache, rebaixe a prioridade e encerre, sem reiniciar nada.

**M8 · Arquivos a fundo** · 5 aulas · semanas 12 e 13

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 8.1 FHS e onde cada coisa mora | /etc, /var, /usr, /opt e /srv; which, type, whereis e locate | LPIC 104.7 |
| 8.2 find a fundo | Por nome, tipo, dono, tamanho, data e permissão; -exec e xargs com segurança | LPIC 103.3, 104.7 |
| 8.3 Arquivamento avançado | tar com seleção e exclusão, cpio e dd; imagem de disco e checksum | LPIC 103.3 · RHCSA tar |
| 8.4 Links | Inodes, links físicos e simbólicos; o que acontece quando o original some | LPIC 104.6 · RHCSA links |
| 8.5 Permissões avançadas | SUID, SGID, sticky, umask e ACL; diagnosticar "Permission denied" passo a passo | LPIC 104.5 · RHCSA umask e diagnóstico |

Desafio do módulo: três "Permission denied" com causas diferentes; achar cada uma.

**M9 · Armazenamento** · 7 aulas · semanas 13 e 14 · backup no PBS antes

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 9.1 Discos e layout | MBR e GPT, nomes de dispositivo, planejar partições e LVM | LPIC 102.1 |
| 9.2 Particionar | fdisk, gdisk e parted em discos novos adicionados pelo Proxmox | LPIC 104.1 · RHCSA GPT |
| 9.3 Sistemas de arquivos | ext4, XFS e VFAT: criar, rotular e comparar | LPIC 104.1 · RHCSA sistemas de arquivos |
| 9.4 Montar e persistir | mount, /etc/fstab por UUID e LABEL, nofail, units de montagem | LPIC 104.3 · RHCSA montagem |
| 9.5 Integridade e espaço | df, du, fsck, xfs\_repair e tune2fs; disco cheio de verdade | LPIC 104.2 |
| 9.6 LVM | PV, VG e LV: criar, estender, reduzir e remover | RHCSA LVM |
| 9.7 Crescer sem destruir | Nova partição, novo LV e swap sem perder dados; aumentar o disco no Proxmox até o sistema de arquivos | RHCSA armazenamento |

Desafio do módulo: um fstab com erro impede o boot. Conserte pelo modo de emergência.

**Fechamento do bloco A (semana 14):** dia de incidente misturando M3 a M9 e revisão do caderno de erros.

### Bloco B · o servidor em rede

**M10 · Usuários e acesso privilegiado** · 4 aulas · semana 15

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 10.1 Contas | useradd, usermod e userdel; /etc/passwd, /etc/shadow e /etc/skel | LPIC 107.1 · RHCSA usuários |
| 10.2 Senhas e validade | passwd, chage e /etc/login.defs; bloquear e expirar contas | LPIC 107.1 · RHCSA senhas |
| 10.3 Grupos e trabalho em equipe | groupadd, gpasswd, grupos suplementares, diretório com SGID | LPIC 107.1 · RHCSA grupos |
| 10.4 sudo de verdade | sudoers, visudo, /etc/sudoers.d e privilégio mínimo | LPIC 110.1 · RHCSA acesso privilegiado |

Desafio do módulo: uma equipe de três usuários, senhas que vencem em 90 dias e um operador que só pode reiniciar o nginx.

**M11 · Rede** · 5 aulas · semanas 16 e 17

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 11.1 TCP/IP para quem administra | IPv4 e IPv6, prefixos, portas, TCP, UDP e ICMP | LPIC 109.1 · RHCSA rede |
| 11.2 NetworkManager e nmcli | Conexões, IP fixo, DNS e IPv6; keyfiles | LPIC 109.2 · RHCSA rede |
| 11.3 Rede no Debian | ifupdown, comparado com NetworkManager e systemd-networkd | LPIC 109.2 |
| 11.4 Nomes e resolução | hostnamectl, /etc/hosts, resolv.conf, nsswitch e getent | LPIC 109.4 · RHCSA resolução de nomes |
| 11.5 Diagnóstico de rede | ping, tracepath, ss, dig, nc e tcpdump; onde o pacote some | LPIC 109.3 · EX342 rede |

Desafio do módulo: IP fixo com IPv6 na VM 201 que sobrevive ao reboot; depois, um DNS quebrado de propósito para consertar.

**M12 · Segurança do host** · 5 aulas · semanas 17 e 18

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 12.1 SSH a fundo | Chaves, ssh-agent, \~/.ssh/config, túneis e sshd\_config seguro | LPIC 110.3 · RHCSA SSH |
| 12.2 Firewall | firewalld com zonas, serviços e portas; nftables no Debian | RHCSA firewall |
| 12.3 SELinux: modos e contextos | enforcing e permissive, ls -Z, ps -Z, semanage fcontext e restorecon | RHCSA SELinux |
| 12.4 SELinux: portas e booleanos | semanage port, setsebool -P, ler um AVC; AppArmor no Debian | RHCSA SELinux |
| 12.5 Auditoria e criptografia | SUID esquecido, portas abertas, last, who e ulimit; cifrar e assinar com GPG | LPIC 110.1, 110.2, 110.3 |

Desafio do módulo: nginx numa porta e num diretório fora do padrão, com SELinux enforcing e firewall ativo, sem desligar nada.

**M13 · Armazenamento em rede** · 3 aulas · semanas 18 e 19 · VM 203 entra

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 13.1 Servidor NFS | Criar a VM 203, exportar diretórios, firewall e SELinux do NFS | base do RHCSA NFS |
| 13.2 Cliente NFS | Montar na mão e no fstab, `_netdev` e opções; o erro "stale file handle" | RHCSA NFS |
| 13.3 autofs | Mapas mestre e indiretos; homes montados sob demanda | RHCSA autofs |

Desafio do módulo: homes de usuários de rede montados sozinhos nas VMs 201 e 202.

**M14 · Agendamento, logs e hora** · 5 aulas · semanas 19 e 20

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 14.1 cron e at | crontab de usuário e de sistema, /etc/cron.d, at e controle de acesso | LPIC 107.2 · RHCSA agendamento |
| 14.2 Timers do systemd | Par .timer e .service, OnCalendar, Persistent e list-timers | LPIC 107.2 · RHCSA timers |
| 14.3 journald e rsyslog | Filtrar o journal, journal persistente, rsyslog e logrotate | LPIC 108.2 · RHCSA logs e journal persistente |
| 14.4 Hora certa | chrony como cliente, timedatectl e fusos; o que quebra quando a hora erra | LPIC 108.1 · RHCSA serviço de hora |
| 14.5 E-mail local e impressão | MTA básico com Postfix, aliases e mail; CUPS e lp | LPIC 108.3, 108.4 |

Desafio do módulo: backup diário por timer, com log no journal e aviso por e-mail local quando falhar.

**M15 · Shell e ambiente** · 5 aulas · semanas 20 e 21

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 15.1 Ambiente do shell | Variáveis, export, PATH, \~/.bashrc, /etc/profile.d, aliases e funções | LPIC 105.1 |
| 15.2 Scripts robustos | Argumentos, testes, laços, case, funções e códigos de saída | LPIC 105.2 · RHCSA scripts |
| 15.3 Scripts de administração | Usar a saída de comandos, gerar relatório, rodar em várias VMs por SSH | LPIC 105.2 · RHCSA scripts |
| 15.4 Interfaces gráficas | X11 e Wayland, display manager, desktops e acessibilidade; instalar num snapshot e voltar | LPIC 106.1, 106.2, 106.3 |
| 15.5 Idioma, teclado e fuso | locale, localectl, UTF-8 e iconv; acentos que chegam quebrados | LPIC 107.3 |

Desafio do módulo: um script de saúde (disco, memória, serviços, último backup) com código de saída que o Zabbix vai ler no M27.

**Fechamento do bloco B (semana 21):** dia de incidente misturando M10 a M15 e revisão do caderno de erros.

### Bloco C · provar que absorveu

**M16 · Semana de incidentes no Rocky 10** · 4 aulas · semanas 21 e 22 · VM 205 entra

| Aula | O que você faz | Programa |
| --- | --- | --- |
| 16.1 Rocky 10: o que muda | Criar a VM 205, o que muda do 9 para o 10 e o que continua igual | RHCSA |
| 16.2 Incidentes por área | Sistemas quebrados por script, com dicas liberadas aos poucos | RHCSA |
| 16.3 Incidente com relógio | Rocky 10 e Debian 13 quebrados, relógio ligado, só man e /usr/share/doc, reboot no fim | RHCSA |
| 16.4 Correção e reforço | Correção por script de verificação e plano para os pontos fracos | RHCSA |

**Critério para seguir:** o 16.3 passa inteiro depois do reboot e você explica cada correção.

## Fase 3 · Infraestrutura real

Semanas 22 a 31 · 36 aulas · fecha com um incidente combinado no NS8.

Meta da fase: sair do servidor isolado para a pilha usada no trabalho. A ordem segue a dependência: o Proxmox onde tudo roda, o Podman que sustenta o NS8, os serviços montados à mão para você entender o que cada módulo esconde e, por fim, o NS8 e as aplicações.

**M17 · Proxmox na prática** · 7 aulas · semanas 22 a 24 · só com os VMIDs do curso

O módulo abre com um diagnóstico sem consulta: criar, migrar, fazer backup e restaurar pela linha de comando. Quem já usa Proxmox passa rápido pelo que fizer com segurança e gasta o tempo nas falhas. A aula 29.2 começa da mesma forma, com o PBS.

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 17.1 Proxmox por dentro | Debian com kernel e serviços próprios; pveversion, pvesh, /etc/pve e os logs que importam | Achar a causa quando a interface web não ajuda |
| 17.2 VM pela linha de comando | qm create, config, set e start; template, clone e cloud-init | Criar e ajustar VM sem clicar |
| 17.3 Contêiner LXC | pct create, enter e config; privilegiado ou não; por que o NS8 exige VM | Escolher entre VM e CT |
| 17.4 Storage | pvesm, tipos de storage e de conteúdo, mover e aumentar disco, thin provisioning | Disco cheio e troca de storage |
| 17.5 Rede | Bridges, VLAN aware, bond e SDN; criar a rede isolada do lab | Descobrir por que a VM não sai |
| 17.6 Backup e restauração | vzdump, PBS, retenção e verify; restaurar uma VM inteira e um único arquivo | Restaurar sob pressão |
| 17.7 Migração e quorum | qm migrate; corosync e pvecm status em modo leitura; o que o quorum protege | Manutenção de nó sem susto |

Desafio do módulo: sem abrir a interface web, criar uma VM a partir de um template, ligar na rede isolada, fazer backup no PBS, apagar a VM e restaurar.

**M18 · Podman** · 5 aulas · semanas 24 e 25

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 18.1 Contêiner não é VM | Imagens, camadas, registries e namespaces; podman pull, images e inspect | Base de todo módulo do NS8 |
| 18.2 Rodar e persistir | run, ps, logs e exec; portas e volumes com `:Z`; contêiner rootless e o SELinux | Saber onde mora o dado do contêiner |
| 18.3 Contêiner como serviço | Quadlet com arquivo .container, systemctl --user e loginctl enable-linger | O mesmo desenho do NS8: usuário, systemd e contêiner |
| 18.4 Diagnosticar contêiner rootless | logs, inspect, top e podman unshare; subuid, ambiente do usuário dono e journalctl --user | Entrar no contêiner certo com o usuário certo |
| 18.5 Construir imagens | Containerfile, podman build, tags e registry local | Ler como uma imagem foi feita |

Desafio do módulo: um nginx rootless com conteúdo persistente que sobe sozinho no boot, sem ninguém logado.

**M19 · Serviços de rede** · 9 aulas · semanas 25 a 27 · VM 204 entra

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 19.1 DNS autoritativo | Criar a VM 204; BIND com zona direta e reversa do lab; named-checkconf e named-checkzone | Registros A, MX e reverso que Mail e WebTop exigem |
| 19.2 DNS recursivo e diagnóstico | Cache, encaminhadores e TTL; dig +trace; por que a culpa costuma ser do DNS | Metade dos chamados de rede |
| 19.3 DHCP | DORA, escopos e reservas; Kea na rede isolada, comparado com dnsmasq | Base do DHCP do NethSecurity |
| 19.4 Servidor web | nginx e Apache nas duas famílias: virtual hosts, logs e permissões; SELinux na Rocky, AppArmor no Debian | Ler erro 502 e 403 sem chute |
| 19.5 TLS e proxy reverso | CA própria com openssl, certificado com SAN, HTTPS e proxy reverso para o contêiner do M18 | Entender o Traefik do NS8 |
| 19.6 Samba, a ponte Windows | Compartilhamento com usuários e permissões, samba\_share\_t na Rocky; mapear a unidade no Windows 11 | Arquivos e domínio no NS8 |
| 19.7 Postfix | Registro MX no BIND, domínio do lab, aliases, fila e logs; relay só para a rede interna | O motor do Mail do NS8 |
| 19.8 Dovecot e teste ponta a ponta | IMAP com o certificado da 19.5; enviar, entregar, ler e seguir a mensagem pelos logs | Seguir um e-mail perdido |
| 19.9 Proxy de saída com Squid | Proxy explícito, ACLs por rede, horário e domínio, autenticação, CONNECT para HTTPS e leitura do access.log; cliente Windows configurado | Controlar e auditar a navegação da empresa |

Desafio do módulo: uma VM nova liga na rede isolada, recebe IP do Kea, resolve nomes pelo BIND, abre o site em HTTPS e lê um e-mail.

**M20 · NethServer 8 por dentro** · 7 aulas · semanas 27 a 29 · VMs 240 e 241 entram

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 20.1 Instalar em VM | Criar a VM 240 com Rocky 9, conferir requisitos, instalar e abrir o painel; por que LXC não serve | Subir um NS8 limpo |
| 20.2 Cluster, nó e módulo | Líder e demais nós, Redis e agentes; o que é uma instância de módulo | Saber quem manda em quem |
| 20.3 Um módulo por dentro | Usuário Unix do módulo, runagent, podman, systemctl --user; dados, journal e busca de logs | Sair do painel e ir à causa |
| 20.4 Proxy e certificados | Traefik, nomes e rotas; Let's Encrypt; portas e firewalld | Aplicação que não abre pelo nome |
| 20.5 Domínios de usuário | OpenLDAP e Samba AD internos, domínio externo; quais aplicações dependem deles | Login que parou de funcionar |
| 20.6 Backup e restauração | Destinos, restic por instância, restaurar um módulo e recuperar o cluster | Voltar depois de perder a VM |
| 20.7 Atualizar, mover e falhar | Atualizar core e módulos, adicionar a VM 241, mover uma instância, derrubar um nó | Manutenção sem surpresa |

Desafio do módulo: apagar uma instância no lab e restaurar do backup, explicando pelo terminal onde cada parte voltou a rodar.

**M21 · Aplicações do NS8** · 8 aulas · semanas 29 a 31 · só no lab

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 21.1 Mail: anatomia | Instalar, domínios e caixas; Postfix, Dovecot e Rspamd em contêineres; portas e DNS exigidos | Saber qual peça olhar |
| 21.2 Mail: diagnóstico | Fila, logs e Message-ID; Rspamd, SPF, DKIM e DMARC; restaurar uma pasta de uma caixa | E-mail que não chega ou cai no spam |
| 21.3 WebTop | FQDN próprio e vínculo com o Mail; ActiveSync, CalDAV, CardDAV e autodiscover | Celular que não sincroniza |
| 21.4 Nextcloud: anatomia | Instalar, MariaDB e Redis, usuários do domínio, occ | Administrar além do painel |
| 21.5 Nextcloud: operação | Espaço, permissões, atualização, restauração e lentidão | Arquivo perdido e upgrade seguro |
| 21.6 NethVoice: SIP e anatomia | SIP e RTP; NethVoice Proxy com Kamailio e RTPengine; Asterisk e FreePBX em contêiner | Entender o caminho da chamada |
| 21.7 NethVoice: ramais e troncos | Proxy antes da instância, ramais, softphone, rotas de entrada e saída, com tronco de teste | Montar sem tocar em linha real |
| 21.8 NethVoice: diagnóstico | Registro que falha, áudio de um lado só, NAT e portas RTP; console do Asterisk e captura SIP | Os chamados clássicos de telefonia |

Desafio do módulo: incidente combinado. Um usuário não recebe e-mail, o WebTop não abre e um ramal não registra; três causas diferentes, achadas pelo terminal.

## Fase 4 · Especialista

Semanas 31 a 48 · 69 aulas · fecha com um dia inteiro de incidentes.

Meta da fase: operar como sênior. Fechar o perímetro, automatizar o que repete, ver o problema antes do usuário, reconstruir depois do desastre e diagnosticar o que ninguém documentou.

**M22 · NethSecurity por dentro** · 8 aulas · semanas 31 a 33 · VMs 250 e 251 entram; LAN só na rede isolada

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 22.1 OpenWrt, a terceira família | Criar a VM 250; uci, /etc/config e serviços; o que muda em relação a Rocky e Debian | Não procurar systemd onde não existe |
| 22.2 Zonas e políticas | wan, lan e guest; fw4 em cima do nftables; ler a tabela inet fw4 | Saber por que o pacote passou ou caiu |
| 22.3 Regras e port forward | Regras, objetos e hairpin; regras próprias em /etc/nftables.d e fw4 reload | Publicar serviço sem abrir demais |
| 22.4 DHCP com dnsmasq | Faixas, reservas, strict binding, leases e limite de concessões | Cliente sem IP ou com IP errado |
| 22.5 DNS com dnsmasq | Encaminhadores, registros locais e cache; regra de entrada na zona guest | Rede que navega por IP e não por nome |
| 22.6 VPN de acesso remoto | OpenVPN road warrior: contas, IP fixo, DNS enviado ao cliente e regra por usuário | Usuário remoto que conecta e não acessa |
| 22.7 VPN entre redes | OpenVPN net-to-net, IPsec e WireGuard entre as VMs 250 e 251; rotas e zonas | Túnel de pé sem tráfego |
| 22.8 Atualizar e recuperar | Backup da configuração, atualização e volta depois de falha; multi-WAN básico; visão de HA e Controller | Mexer no firewall com plano de volta |

Desafio do módulo: criar uma rede guest com DHCP, DNS e saída para a internet, sem acesso à LAN, e alcançar a rede da VM 251 pelo túnel.

**M23 · Git e VS Code** · 4 aulas · semanas 33 e 34

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 23.1 Git do zero | init, add, commit, status, log e diff; .gitignore; desfazer com restore e revert | Histórico de toda mudança |
| 23.2 Repositório central | Repositório bare na VM 203 por SSH; clone, push, pull, branch e merge; resolver um conflito | Configuração em um lugar só |
| 23.3 VS Code como estação de trabalho | Remote - SSH a partir do Windows, terminal integrado e as extensões de YAML e Ansible | Editar o servidor sem sair do Windows |
| 23.4 YAML sem sustos | Indentação, listas, dicionários, textos de várias linhas e aspas; yamllint e os erros clássicos | Playbook que não quebra por um espaço |

Desafio do módulo: os scripts das fases anteriores versionados na VM 203, com mensagens de commit claras e um conflito resolvido.

**M24 · Ansible I · fundamentos** · 4 aulas · semanas 34 e 35 · VMs 210 a 212 entram

Regra do Ansible: todo playbook vai para o Git e roda duas vezes; a segunda execução tem que terminar com `changed=0`.

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 24.1 Nó de controle | Criar as VMs 210 a 212; instalar ansible-core e ansible-navigator; dev container no VS Code | Ter de onde comandar a frota |
| 24.2 Inventário e ansible.cfg | Inventário em INI e YAML, grupos e grupos de grupos; usuário com chave SSH e sudo nos nós | Alcançar Rocky e Debian com o mesmo acesso |
| 24.3 Ad hoc e documentação | ansible -m, ansible-doc e ansible-navigator doc; o módulo certo em vez de shell | Conferir 30 servidores em um comando |
| 24.4 Primeiro playbook | Plays e tasks, idempotência, --syntax-check, --check e --diff; commit e push | Trocar script frágil por estado desejado |

Desafio do módulo: um playbook que prepara os nós do zero e termina com `changed=0` na segunda execução.

**M25 · Ansible II · playbooks de verdade** · 8 aulas · semanas 35 a 37

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 25.1 Variáveis e precedência | vars, group\_vars, host\_vars e extra vars; quem ganha quando dois definem | Valor errado vindo de onde você não olhou |
| 25.2 Facts e register | gather\_facts, ansible\_facts, facts customizados e register | Decidir pelo que o servidor é de verdade |
| 25.3 Condicionais | when com facts, variáveis e resultados; testes como is defined | Um playbook para Rocky e Debian |
| 25.4 Loops | loop e loop\_control sobre listas e dicionários | Criar 20 usuários sem copiar 20 tasks |
| 25.5 Handlers | notify, listen e flush\_handlers; reiniciar só quando algo mudou | Não derrubar serviço à toa |
| 25.6 Tratar erros | ignore\_errors, failed\_when e changed\_when; block, rescue e always | Parar antes de estragar o resto da frota |
| 25.7 Templates Jinja2 | Módulo template, filtros, laços e condicionais; um arquivo diferente por host | Configuração gerada, sem edição à mão |
| 25.8 Ansible Vault | create, edit, rekey e vault-id; arquivo de senha fora do Git | Segredo versionado e protegido |

Desafio do módulo: nginx com página gerada por template, reinício só quando a configuração muda e uma senha protegida pelo Vault.

**M26 · Ansible III · roles e frota real** · 6 aulas · semanas 37 e 38 · backup no PBS antes

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 26.1 Roles | Estrutura, defaults e vars, ansible-galaxy role init; transformar o playbook do M25 em role | Reaproveitar sem copiar |
| 26.2 Collections | FQCN, requirements.yml e ansible-galaxy collection install; RHEL System Roles e execution environments | Usar o que já está pronto e testado |
| 26.3 Administração automatizada I | Usuários, grupos, pacotes, serviços, firewall, agendamento e arquivos, nas duas famílias | O dia a dia virando código |
| 26.4 Administração automatizada II | Partições, LVM, sistemas de arquivos, montagens e SELinux ou AppArmor | Disco e segurança sem passo manual |
| 26.5 Frota por áreas | Tarefas por área em nós restaurados do PBS, com dicas liberadas aos poucos | Treinar em máquina limpa |
| 26.6 Frota do zero com relógio | Tudo em nós limpos, cronometrado; correção por script e plano para os pontos fracos | Máquina nova pronta em minutos |

Desafio do módulo: um nó vazio de cada família vira servidor pronto com uma única execução, combinando roles suas e System Roles.

**M27 · Monitoramento** · 4 aulas · semana 39

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 27.1 O servidor por dentro | Cockpit, sar e PCP; a linha de base do que é normal | Saber o que é anormal |
| 27.2 Zabbix | Servidor na VM 204 e agentes nas VMs do curso; hosts, templates e painéis | Enxergar a frota |
| 27.3 Alertas que importam | Item com o script de saúde do M15, triggers sem alarme falso e aviso pelo Postfix do M19 | Dormir sem alarme falso |
| 27.4 O que vence e o que enche | Certificados perto do vencimento, serviços parados e disco enchendo; previsão de capacidade | Resolver antes do chamado |

Desafio do módulo: derrubar um serviço, encher um disco e emitir um certificado que vence amanhã. O Zabbix avisa sobre os três antes de você abrir o terminal.

**M28 · Logs centralizados e integridade** · 4 aulas · semana 40 · VM 203 vira servidor de logs

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 28.1 rsyslog central | Servidor na VM 203, clientes por TCP e um diretório por host; a porta no firewall e no SELinux | Log que sobrevive ao servidor |
| 28.2 Journal remoto | systemd-journal-remote e systemd-journal-upload; quando usar cada solução | Centralizar sem perder os campos do journal |
| 28.3 auditd | Regras para arquivos e comandos sensíveis; ausearch e aureport; quem mexeu no sudoers | Responder quem fez o quê |
| 28.4 AIDE | Base de integridade, verificação diária por timer e investigação de uma mudança plantada | Provar o que foi alterado |

Desafio do módulo: alguém trocou um binário e editou uma configuração. Descubra o quê, quando e quem, só com os logs centrais, o auditd e o AIDE.

**M29 · Backup e recuperação** · 5 aulas · semanas 41 e 42

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 29.1 Estratégia antes da ferramenta | 3-2-1, RPO e RTO; o que copiar e o que reconstruir; plano de backup por escrito | Prometer só o que dá para cumprir |
| 29.2 PBS a fundo | Num namespace só do curso: retenção, verify, sync e restauração de um único arquivo | Confiar no backup porque testou |
| 29.3 Backup dentro do Linux | restic ou borg com criptografia, dump de banco e restauração testada | Copiar dado consistente |
| 29.4 Restaurar a pilha | Proxmox, NS8 e NethSecurity: o que volta primeiro e o que depende do quê | Ordem certa no dia ruim |
| 29.5 Dia do desastre | Uma VM perdida de propósito: restaurar, conferir os dados e medir o RTO real | Saber o tempo de verdade |

Desafio do módulo: com o cronômetro ligado, a VM 204 e a VM 240 voltam inteiras do PBS; os serviços do M19 e Mail, WebTop, Nextcloud e NethVoice respondem.

**M30 · Desempenho e depuração** · 5 aulas · semanas 42 e 43

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 30.1 Método USE | Uso, saturação e erros de CPU, memória, disco e rede; vmstat, mpstat e pidstat | Medir antes de culpar |
| 30.2 Memória | free, /proc/meminfo, pmap, swap e OOM killer; achar um vazamento com valgrind | Processo morto sem aviso |
| 30.3 Disco e I/O | iostat, iotop e fio; latência e vazão; o disco Ceph visto de dentro da VM | "O servidor está lento" |
| 30.4 Ferramentas de depuração | strace, ltrace, ldd, gdb e coredumpctl; por que o programa morreu | Falha sem log |
| 30.5 Ajuste fino | tuned, sysctl, limits e limites de recursos no systemd; medir antes e depois | Melhorar com prova |

Desafio do módulo: um serviço fica lento sem motivo aparente. Prove com números onde está o gargalo antes de mudar qualquer coisa.

**M31 · Alta disponibilidade** · 5 aulas · semanas 43 e 44 · VMs 220 a 222 entram

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 31.1 Conceitos de HA | Ponto único de falha, quorum, split-brain e fencing; criar as VMs 220 a 222 | Decidir o que precisa de HA |
| 31.2 IP flutuante | keepalived com VRRP e verificação de serviço; derrubar o mestre e ver o IP mudar de nó | Serviço que muda de nó sem trocar de IP |
| 31.3 HAProxy | Balancear dois servidores web, health checks e página de estatísticas | Tirar servidor doente de circulação |
| 31.4 Pacemaker e pcs | Cluster de três nós, recursos, restrições e ordem; IP virtual junto com o serviço | Ler e operar cluster de aplicação |
| 31.5 Fencing e testes de falha | fence\_pve pela API do Proxmox, com usuário restrito às VMs 220 a 222; HA do Proxmox ou da aplicação? | Testar a falha antes que ela venha |

Desafio do módulo: desligar a placa de rede do nó ativo no meio de um teste de carga. O serviço volta sozinho em segundos e o fencing aparece no log.

**M32 · Hardening** · 5 aulas · semanas 44 e 45

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 32.1 Medir antes de endurecer | OpenSCAP com um perfil CIS; relatório e remediação escolhida item a item | Endurecer sem quebrar |
| 32.2 SSH e senhas | sshd\_config.d só com chave e sem login de root; política de senha com pwquality | Fechar a porta mais atacada |
| 32.3 PAM | authselect na Rocky, pam-auth-update no Debian; faillock e acesso por grupo | Login que falha sem motivo |
| 32.4 LUKS | Disco cifrado, crypttab, slots de chave e backup do cabeçalho; recuperar o acesso | Dado protegido e recuperável |
| 32.5 Superfície mínima | Menos serviços e portas, fail2ban, atualizações automáticas; módulo SELinux com audit2allow | Menos coisa para defender |

Desafio do módulo: subir a nota do OpenSCAP da VM 201 sem perder o acesso SSH, com cada mudança justificada num commit.

**M33 · Cluster Proxmox e Ceph** · 5 aulas · semanas 46 e 47 · VMs 230 a 232 entram; o cluster real não é tocado

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 33.1 Proxmox dentro do Proxmox | Três VMs com Proxmox VE e virtualização aninhada; criar o cluster com pvecm | Treinar sem risco |
| 33.2 Perder nó e quorum | corosync, perda de nó e de quorum; regras de HA | Agir certo quando o cluster trava |
| 33.3 Ceph por dentro | ceph -s, OSDs, pools e PGs; substituir um OSD com defeito | Ler a saúde do storage |
| 33.4 Atualizar sem parar | Atualização nó a nó: migrar, noout, reiniciar, conferir a saúde e seguir | Manutenção com VM no ar |
| 33.5 Automatizar e documentar | API com token e Ansible; o runbook de incidente | Procedimento que outro consegue seguir |

Desafio do módulo: um nó do cluster aninhado morre sem aviso. Recupere o quorum, a saúde do Ceph e as VMs seguindo o seu runbook.

**M34 · Troubleshooting de casos reais** · 6 aulas · semanas 47 e 48

| Aula | O que você faz | Serve para |
| --- | --- | --- |
| 34.1 Método e sos | Hipótese, teste e registro; sos report e a documentação oficial como ferramenta | Parar de chutar |
| 34.2 Boot quebrado | GRUB, initramfs com dracut, rd.break e emergency.target; acesso de root perdido | Servidor que não sobe |
| 34.3 Disco quebrado | fsck e xfs\_repair, LVM apagado com vgcfgrestore, LUKS sem a senha principal | Recuperar antes de reinstalar |
| 34.4 Pacotes quebrados | rpm --rebuilddb, rpm -Va, dpkg --audit, dependências quebradas e arquivos alterados | Atualização interrompida |
| 34.5 Rede, kernel e hardware | tcpdump e tshark; kdump e crash; lshw, dmidecode e módulos | Falha que não aparece no log |
| 34.6 Dia inteiro de incidentes | Defeitos plantados em Rocky, Debian, Proxmox aninhado, NS8 e NethSecurity; um diário para cada diagnóstico | Fechar o curso provando fluência |

**Critério final:** todos os defeitos da 34.6 resolvidos e explicados no diário, sem ajuda.

**Depois da semana 48:** um !quebra por semana no DeepTutor e um dia do desastre por mês mantêm tudo afiado.

## Cronograma

48 semanas e 188 aulas. O ritmo de referência é de 4 aulas por semana, de 60 a 90 minutos cada. Com 5 ou 6 aulas por semana o calendário encolhe; com 2 ou 3, estica. Quem decide se você avança é o critério de fluência, nunca o calendário.

| Fase | Semanas | Aulas | Módulos | Fecha com |
| --- | --- | --- | --- | --- |
| 1 · Fundamentos | 1 a 6 | 20 | M0 a M2 | Dia de incidente (semana 6) |
| 2 · Administrador | 7 a 22 | 63 | M3 a M16 | Incidente com relógio no Rocky 10 e no Debian 13 |
| 3 · Infraestrutura real | 22 a 31 | 36 | M17 a M21 | Incidente combinado no NS8 |
| 4 · Especialista | 31 a 48 | 69 | M22 a M34 | Dia inteiro de incidentes |

Começando na segunda-feira, 2 de novembro de 2026, e sem pausas, a semana 48 começa em 27 de setembro de 2027. Com duas semanas de folga no Natal e três em agosto, ela começa em 1º de novembro de 2027.

### A semana típica

| Quando | O que você faz | Tempo |
| --- | --- | --- |
| Começo de cada sessão | Revisões que vencem hoje, com o DeepTutor e sem consulta | 10 a 15 min |
| 4 sessões por semana | Uma aula completa: aquecimento, conceito, lab, quebre e conserte, quiz | 60 a 90 min |
| 1 sessão por semana | Desafio do módulo ou um !quebra no DeepTutor; uma vez por mês, dia de incidente | 45 a 60 min |
| Fim da semana | Diário de bordo, caderno de erros, snapshot de fim e conferência do backup no PBS | 15 a 20 min |

### Revisão espaçada

Cada aula termina com 5 a 10 flashcards. Cada cartão volta 1, 3, 7 e 21 dias depois da aula (D+1, D+3, D+7 e D+21). Acertou sem hesitar: o cartão segue para o intervalo seguinte. Errou ou hesitou: volta para D+1. Depois do D+21, o assunto reaparece nos dias de incidente. As revisões não passam de 15 minutos por dia; se acumularem, comece pelas mais atrasadas.

### Dias de incidente e critério para avançar

Uma vez por mês, um sistema quebrado com o relógio ligado, misturando assuntos e sem pesquisa, só com man e a documentação local. O dia de incidente substitui os antigos simulados.

| Marco | Como você prova | Semana | Avance quando |
| --- | --- | --- | --- |
| Fundamentos | Dia de incidente M0 a M2 | 6 | Resolver e explicar tudo sem consulta nas duas VMs |
| Bloco A | Dia de incidente M3 a M9 | 14 | Tudo sobrevive ao reboot |
| Bloco B | Dia de incidente M10 a M15 | 21 | Tudo sobrevive ao reboot |
| Administrador | Aula 16.3 | 22 | Passar inteiro depois do reboot |
| Proxmox | Desafio do M17 | 24 | Fazer sem abrir a interface web |
| NS8 | Desafio do M21 | 31 | Três causas achadas pelo terminal |
| NethSecurity | Desafio do M22 | 33 | Guest isolada e túnel funcionando depois do reboot |
| Especialista | Aula 34.6 | 48 | Todos os defeitos resolvidos e explicados |

### Caderno de erros

Todo erro vira uma linha: data, aula, o que aconteceu, a causa e a regra que impede a repetição. Erro que aparece duas vezes vira flashcard. Antes de cada dia de incidente, o caderno é a primeira coisa que você relê.

### Entregas que provam o nível

Cada etapa deixa algo que você consegue mostrar a um chefe ou numa entrevista. Guarde tudo num repositório seu, sem dados de empresa ou de clientes.

| Semana | O que você passa a ter |
| --- | --- |
| 22 | Incidentes com relógio resolvidos em Rocky e Debian, com o tempo registrado |
| 31 | NS8 com Mail, WebTop, Nextcloud e NethVoice montado do zero e documentado |
| 38 | Servidor novo pronto com um comando, em roles Ansible versionadas |
| 42 | Restauração testada, com RTO medido e plano de backup por escrito |
| 48 | Runbooks de incidente e o dia inteiro de incidentes resolvido sem ajuda |

### Se atrasar

Perdeu uma semana? Não comprima duas em uma: empurre o calendário inteiro. Faça só as revisões vencidas e retome de onde parou. Pular o lab para ganhar tempo é a única economia proibida.

## Prompt do tutor no DeepTutor

Cole o texto abaixo nas instruções do DeepTutor. Se a sua versão não tiver esse campo, cole como primeira mensagem de cada conversa nova. Ele transforma o modelo num tutor que pergunta antes de responder, segue a anatomia das aulas e respeita os limites do laboratório.

```text
Você é o tutor particular do curso "Linux Sysadmin". O objetivo é fluência real em Rocky Linux, Debian e Proxmox, chegando a operar NethServer 8 e NethSecurity por dentro. O aluno não vai fazer provas. Fale sempre em português do Brasil e mantenha os comandos em inglês.

QUEM É O ALUNO
- Perfil do aluno (troque pelo seu): sysadmin que vem do Windows Server e já usa Proxmox, NethServer e firewalls no trabalho. Está construindo uma base Linux sólida, do zero, para se tornar especialista.
- Laboratório num cluster Proxmox. VMs do curso: 201 rocky-lab (Rocky Linux 9), 202 debian-lab (Debian 13), 203 srv-lab (Rocky 9: NFS, Git e logs), 204 srv-deb (Debian 13: serviços de rede), 205 rocky10-lab (Rocky Linux 10), 210 a 212 (Ansible, Rocky e Debian), 220 a 222 (alta disponibilidade), 230 a 232 (Proxmox aninhado), 240 e 241 (NethServer 8) e 250 e 251 (NethSecurity).
- Aplicações que importam no NS8: Mail, WebTop, Nextcloud e NethVoice. No NethSecurity: firewall, VPN, DHCP e DNS.
- Programas de referência, só como lista de assuntos: Linux Essentials 010-200, LPIC-1, RHCSA EX200, EX294 e EX342.

COMO VOCÊ ENSINA
1. Abra cada sessão perguntando em que aula o aluno está (por exemplo, 1.3). Faça 3 perguntas de revisão das aulas anteriores, uma por vez, sem consulta, e corrija cada uma em uma ou duas frases.
2. Nunca entregue a resposta antes de o aluno tentar. Dê dicas em três níveis: pista, direção e, só se ele pedir, a solução comentada.
3. Antes de cada comando, peça que o aluno preveja a saída. Depois compare previsão e resultado.
4. Sempre que houver diferença, mostre Rocky e Debian lado a lado: pacotes, caminhos, firewall, SELinux e AppArmor, grupo wheel e grupo sudo. No NethSecurity, lembre que a base é OpenWrt: uci, /etc/config e fw4.
5. Quando ajudar, compare com o equivalente no Windows Server.
6. Peça que o aluno explique com as próprias palavras, como se ensinasse um colega. Aponte o que faltou ou ficou errado.
7. Para cada erro, diga o tipo (conceito, sintaxe ou distração) e sugira a linha para o caderno de erros.
8. Parta de um case real de sysadmin e diga onde o assunto aparece no trabalho. Cite um objetivo de prova só se o aluno pedir, e não invente objetivos.
9. Uma pergunta por mensagem, mensagens curtas e comandos sempre em bloco de código.
10. Se não tiver certeza de um detalhe de versão, diga isso e mostre como conferir: man, --help, /usr/share/doc ou a documentação oficial. NS8 e NethSecurity mudam rápido: nunca afirme comando ou caminho deles de memória sem avisar.

SEGURANÇA DO LABORATÓRIO
- Comandos destrutivos só nas VMs do curso (201 a 251) e só depois de o aluno confirmar que existe snapshot ou backup.
- Nunca proponha nada que mexa nas VMs 100 a 103 nem no CT 108, onde você mesmo roda. No host Proxmox, só comandos de leitura ou comandos qm com os IDs do curso.
- Em sistemas de produção e de clientes, somente leitura.
- Nunca peça senhas, tokens ou chaves privadas. Se o aluno colar um segredo, peça que ele troque esse segredo e não o repita.

COMANDOS
!quiz [aula ou tema]: 5 perguntas, uma por vez, misturando múltipla escolha, completar o comando e "o que acontece se". No fim, gabarito comentado e nota.
!quebra [tema]: incidente simulado. Descreva só o sintoma. O aluno pede comandos e você responde com saídas realistas do sistema em questão, sem revelar a causa, até ele diagnosticar e propor a correção. No fim, explique a causa e como evitar.
!simulado [tema] [n]: n tarefas práticas com critério de verificação, relógio ligado e sem pesquisa. Corrija no fim e liste os pontos fracos. Só use o formato de uma prova específica se o aluno pedir.
!revisao [cartões ou aula]: pergunte os cartões que vencem hoje, um por vez, sem mostrar a resposta antes. No fim, diga quais avançam para o próximo intervalo e quais voltam para D+1.
!cartoes [aula]: gere de 5 a 10 flashcards de pergunta e resposta curtas para a revisão espaçada.
!explica [conceito]: explique em camadas: analogia, o essencial, o aprofundamento e onde isso aparece no trabalho.
!feynman [tema]: o aluno explica o tema; você avalia clareza, precisão e lacunas, com nota de 0 a 10.
!erro: o aluno cola uma mensagem de erro; você guia o diagnóstico com perguntas antes de sugerir qualquer correção.
```

Para testar, mande `!quiz 1.1`: o tutor deve fazer uma pergunta por vez e esperar a sua resposta antes de corrigir.
