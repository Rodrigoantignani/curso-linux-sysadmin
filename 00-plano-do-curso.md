# Curso Linux Sysadmin

Oct 30, 2026 · @RODRIGO ANTIGNANI COUTINHO

## Como o curso funciona

Cada aula leva de 60 a 90 minutos e segue sempre o mesmo roteiro: lembrar, entender, fazer nas duas distros, quebrar, consertar e provar que aprendeu. O curso vai do zero até o nível RHCSA/RHCE e continua até a operação profissional.

As aulas ficam na aba Aulas, uma subaba por aula, com a situação de cada uma e uma coluna para você marcar o seu progresso.

**Os princípios por trás de cada aula**

| Princípio | O que você faz | Por que funciona |
| --- | --- | --- |
| Recuperar antes de reler | Abre a aula respondendo 3 perguntas das anteriores, sem consultar | Puxar da memória fixa muito mais do que reler |
| Espaçar | Revisa os flashcards em D+1, D+3, D+7 e D+21 | Revisar quando já está quase esquecendo fortalece a lembrança |
| Prever antes de rodar | Escreve o que espera ver antes de cada comando novo | O erro de previsão mostra exatamente o que você não sabia |
| Intercalar | Faz tudo no Rocky e no Debian, lado a lado | Comparar obriga a entender o princípio, não a decorar o comando |
| Do resolvido ao sozinho | Lab guiado primeiro, depois desafio com menos ajuda | A ajuda diminui conforme a habilidade cresce |
| Quebre e conserte | Diagnostica um defeito plantado no fim de cada aula | Troubleshooting é o trabalho real e o formato da prova prática da Red Hat |
| Explicar com suas palavras | Explica o conceito ao DeepTutor e pede crítica | Quem explica descobre as próprias lacunas |
| Ponte Windows | Liga cada conceito ao equivalente no Windows Server | Você já sabe administrar; aqui muda o idioma |

**Anatomia de uma aula**

1. Ficha: objetivos, itens de exame, pré-requisitos e tempo.
2. Aquecimento: 3 perguntas de revisão, sem consulta.
3. Por que importa: um caso real de sysadmin.
4. Modelo mental: analogia e desenho.
5. Conceito em camadas: o essencial, o aprofundamento e o que cai na prova.
6. Rocky × Debian: a tabela das diferenças.
7. Lab guiado: snapshot antes; cada passo com previsão, comando, saída esperada e verificação.
8. Quebre e conserte: um defeito para diagnosticar sozinho.
9. Armadilhas: os erros mais comuns e como evitá-los.
10. Quiz com gabarito comentado.
11. Flashcards e cola de comandos.
12. Checklist de saída e snapshot de fim.
13. Com o DeepTutor: prompts prontos para aprofundar.

**Quem faz o quê**

| Quem | Papel |
| --- | --- |
| Claude | Escreve as aulas, revisa labs e corrige o rumo quando você pedir |
| DeepTutor (Haiku 5.5) | Tira dúvidas na hora, gera exercícios extras, aplica quizzes e explica erros |
| Você | Faz os labs, mantém o diário de bordo e responde os quizzes sem olhar |

**Regras do laboratório**

- Snapshot antes de cada lab, sempre. Errar no lab é barato; em produção, não.
- Nenhum lab em servidor de cliente ou de produção.
- Diário de bordo: comando, o que esperava, o que aconteceu, o que aprendeu.
- Leia a mensagem de erro inteira antes de pesquisar. Quase sempre ela já diz a causa.

## Mapa das certificações

Conferido nas páginas oficiais da LPI e da Red Hat em 30/10/2026. Duas mudanças pesaram no plano: o Linux Essentials ganhou a versão 2.0, e o RHCE virou duas certificações diferentes.

&#91;embedded content: roteiro do curso · 4 fases, 6 provas, 46 semanas\]

A Fase 2 é a mais longa porque leva a três provas. O RHCSA da semana 25 é a base dos dois RHCE: sem ele, nem o EX294 nem o EX342 viram certificação.

| Certificação | Prova | Base | Formato | Validade | Quando |
| --- | --- | --- | --- | --- | --- |
| Linux Essentials | 010-200 (versão 2.0) | Neutra | 40 questões em 60 min | Vitalícia | Semana 6 |
| LPIC-1 | 101-500 e 102-500 (versão 5.0) | Neutra: Debian e Red Hat | 60 questões em 90 min, cada prova | 5 anos | Semanas 15 e 23 |
| RHCSA | EX200 | RHEL 10 | Prática, tarefas no terminal | 3 anos | Semana 25 |
| RHCE em Ansible | RHCSA + EX294 | Ansible Automation Platform | Prática, playbooks | 3 anos | Semana 35 |
| RHCE em Enterprise Linux | RHCSA + EX342 | RHEL 10.2 | Prática, troubleshooting, 4 h | 3 anos | Semana 46 |

**O que mudou e como o curso se ajusta**

- **Linux Essentials 2.0.** Entraram systemd, SSH, nuvem e containers. Por enquanto a prova é só em inglês; a LPI promete as traduções, português incluído, nos próximos meses. A versão 1.6 (010-160) continua à venda até abril de 2027. O curso segue a 2.0; se você preferir fazer em português e a tradução ainda não tiver saído, a 010-160 é uma opção.
- **LPIC-1 sem mudanças.** Continua na 5.0, com prova em português do Brasil, presencial ou online (OnVUE).
- **RHCSA no RHEL 10.** Entraram Flatpak e timers do systemd; containers saíram da lista de objetivos. O curso continua ensinando Podman na Fase 3, porque o EX294 roda o Ansible dentro de containers e o mercado usa.
- **RHCE agora são dois.** O RHCE em Ansible exige RHCSA + EX294. O RHCE em Enterprise Linux exige RHCSA + EX342, uma prova de diagnóstico e correção de falhas. O curso faz os dois: EX294 na Fase 3 e EX342 na Fase 4, que já era a fase de troubleshooting e operação. Ganhar um deles estende a validade dos outros RHCE e das certificações abaixo.
- **EX294 cobra Git, VS Code e ansible-navigator.** Por isso os módulos M17 (Git e VS Code) e M18 (Podman) vêm antes do Ansible.
- **Provas da Red Hat são 100% práticas.** Sem internet, só com a documentação do produto, e tudo precisa sobreviver a um reboot. Por isso todo lab do curso termina com reboot e verificação.

**Regra de ouro:** 30 dias antes de agendar qualquer prova, releia os objetivos oficiais. As provas mudam; o curso acompanha.

**Fontes oficiais**

- [Linux Essentials](https://www.lpi.org/our-certifications/linux-essentials-overview/) e [objetivos da prova 010](https://www.lpi.org/our-certifications/exam-010-objectives/)
- [LPIC-1](https://www.lpi.org/our-certifications/lpic-1-overview/)
- [RHCSA, prova EX200](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam)
- [RHCE em Ansible](https://www.redhat.com/en/services/certification/red-hat-certified-engineer-in-ansible) e [prova EX294](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux)
- [RHCE em Enterprise Linux](https://www.redhat.com/en/services/certification/red-hat-certified-engineer-in-enterprise-linux) e [prova EX342](https://www.redhat.com/en/services/training/ex342-red-hat-certified-specialist-linux-diagnostics-and-troubleshooting)

## Laboratório no Proxmox

O lab mora no cluster cluster-labvol e cresce junto com o curso: começa com duas VMs e termina como uma pequena infraestrutura. As VMs 100 a 103 e o CT 108 (DeepTutor) não fazem parte do curso: não mexa neles.

| VMID | Nome | Sistema | Recursos | Entra em | Para quê |
| --- | --- | --- | --- | --- | --- |
| 201 | rocky-lab | Rocky Linux 9 | 2 vCPU, 2 GB, 20 GB | M0 | Lado Red Hat das aulas; mesma base do NethServer 8 |
| 202 | debian-lab | Debian 13 | 2 vCPU, 2 GB, 20 GB | M0 | Lado Debian das aulas; mesma base do Proxmox |
| 203 | srv-lab | Rocky Linux 9 | 2 vCPU, 2 GB, 20 GB | M13 | Servidor NFS; depois Git e logs centralizados |
| 204 | srv-deb | Debian 13 | 2 vCPU, 2 GB, 20 GB | M19 | DNS, DHCP, web, Samba e e-mail |
| 205 | rocky10-lab | Rocky Linux 10 | 2 vCPU, 2 GB, 20 GB | M16 | Treino de RHCSA e EX342, que usam RHEL 10 |
| 210 a 212 | ans-ctl, ans-n1, ans-n2 | Rocky Linux 10 | ans-ctl com 4 GB; nós com 2 GB | M20 | Ansible: controle e nós gerenciados |
| 220 a 222 | ha-1, ha-2, ha-3 | Rocky Linux 10 | 2 vCPU, 2 GB | M27 | Pacemaker, HAProxy e keepalived |
| 230 a 232 | pve-n1, pve-n2, pve-n3 | Proxmox VE 9 | 2 vCPU tipo host, 4 GB, 2 discos | M29 | Cluster Proxmox com Ceph aninhado, para treinar sem tocar no cluster real |

**Padrão de toda VM do curso**

- CPU `x86-64-v2-AES` para Rocky 9 e Debian 13. O Rocky 10 exige `x86-64-v3`: antes da VM 205, confira se todos os nós têm AVX2 com `grep -c avx2 /proc/cpuinfo` (resultado maior que zero). Se algum nó não tiver, use Rocky 9 nas VMs 205 em diante; os objetivos das provas funcionam igual em quase tudo.
- Máquina q35 com UEFI (OVMF), disco no `vm-hdd` (Ceph RBD), placa virtio na `vmbr0`.
- Guest agent ligado na VM e o pacote `qemu-guest-agent` instalado no sistema.
- Senha de root definida nas duas distros: o modo de emergência pede essa senha.
- SSH sempre com o seu usuário. Root não entra por senha via SSH, que é o padrão das duas distros.
- Servidores do lab (VM 203 em diante) usam IP fixo fora da faixa do DHCP da `vmbr0`.

**Snapshots: a rede de proteção**

- Nome no formato `mXaY-inicio` e `mXaY-fim`, por exemplo `m2a3-inicio`. Só letras, números, hífen e sublinhado, começando por letra.
- Antes de cada lab: `qm snapshot 201 m2a3-inicio`, e o mesmo na 202.
- Deu errado: `qm rollback 201 m2a3-inicio` devolve a VM ao ponto salvo.
- No fim de cada módulo, apague os snapshots intermediários e guarde só o último `-fim`.

**Backup no PBS**

- Um job semanal em Datacenter → Backup para as VMs do curso, no `PBS-LAB`, modo snapshot.
- Antes de aula arriscada (4.4, módulo 9, módulo 22), um backup manual: `vzdump 201 --storage PBS-LAB --mode snapshot`.
- Snapshot não é backup: o snapshot mora no mesmo storage da VM; o backup no PBS sobrevive se esse storage cair.

**Rede isolada para o DHCP:** um servidor DHCP de teste na `vmbr0` pode entregar IP errado para a rede inteira. Na aula 19.3 você cria uma rede só do lab (bridge sem porta física ou VNet do SDN) antes de ligar o Kea.

**Opcional para os simulados finais:** a assinatura gratuita Red Hat Developer for Individuals libera RHEL de verdade em até 16 sistemas. Serve para ensaiar as provas no mesmo sistema que a Red Hat usa.

## Fase 1 · Fundamentos

Semanas 1 a 6 · 20 aulas · fecha com o Linux Essentials 010-200.

Meta da fase: usar o terminal com segurança e entender o que cada comando faz por baixo, nas duas distros. Quem termina a fase navega, manipula texto, escreve scripts simples, entende processos, rede, usuários e permissões, e passa no Linux Essentials sem decorar respostas.

**Pré-teste de dispensa.** Já domina o assunto de uma aula? Faça o aquecimento e o quebre e conserte. Acertou tudo sem consultar nada: leia só o modelo mental e siga em frente. Na Fase 1 isso vai acontecer bastante.

**M0 · Laboratório** · 2 aulas · semana 1

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 0.1 Montar o laboratório | Cria as VMs 201 e 202 pela linha de comando do Proxmox, instala Rocky 9 e Debian 13 entendendo cada tela do instalador e confere o resultado | LE 014.1 |
| 0.2 Acesso e proteção | SSH do Windows com chave Ed25519, sudo nas duas VMs, guest agent, snapshots e backup no PBS com teste de restauração | LE 015.1 · RHCSA SSH |

Desafio do módulo: quebrar uma VM de propósito e voltar pelo snapshot em menos de dois minutos.

**M1 · Linha de comando** · 10 aulas · semanas 1 a 3

| Aula | O que você faz | Prova |
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

| Aula | O que você faz | Prova |
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

**Fechamento da fase (semana 6):** revisão espaçada de M0 a M2 e dois simulados de 40 questões em 60 minutos, em inglês, gerados pelo DeepTutor a partir dos objetivos oficiais. Agende a prova quando o segundo simulado passar de 80%. Se preferir fazer em português e a tradução da 2.0 ainda não tiver saído, a 010-160 continua à venda até abril de 2027.

## Fase 2 · Administrador

Semanas 7 a 25 · 63 aulas · três provas: LPIC-1 101 (semana 15), LPIC-1 102 (semana 23) e RHCSA (semana 25).

Meta da fase: administrar sozinho um servidor Linux de ponta a ponta, nas duas famílias, com tudo sobrevivendo ao reboot. A fase tem três blocos, um por prova. Todo lab termina com reboot e verificação, como na prova da Red Hat.

### Bloco A · rumo ao LPIC-1 101

**M3 · Texto e editor** · 5 aulas · semanas 7 e 8

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 3.1 Fluxos a fundo | tee, xargs, here-doc, substituição de processo e /dev/null; pipelines que não escondem erro | LPIC 103.4 · RHCSA redirecionamento |
| 3.2 Filtros de texto | cut, sort, uniq, tr, paste, nl, split, od e sha256sum; transformar log em relatório | LPIC 103.2 |
| 3.3 Expressões regulares e grep | BRE e ERE, âncoras, classes e grupos; grep -E, -v, -o e -r | LPIC 103.7 · RHCSA grep e regex |
| 3.4 sed e awk | Substituir, apagar e extrair linhas com sed; colunas, filtros e somas com awk | LPIC 103.2, 103.7 |
| 3.5 vi e vim de verdade | Modos, movimentos, busca e substituição, desfazer; editar configuração sem medo | LPIC 103.8 · RHCSA editar arquivos |

Desafio do módulo: os 10 IPs que mais erraram senha no SSH, numa linha de comando, nas duas VMs. A Rocky guarda isso em /var/log/secure; a Debian, só no journal.

**M4 · Boot e systemd** · 4 aulas · semanas 8 e 9

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 4.1 Como o Linux liga | UEFI, GRUB 2, kernel, initramfs e systemd; ler o boot com journalctl -b e systemd-analyze | LPIC 101.2 |
| 4.2 systemd: serviços e units | start, stop, enable e mask; dependências e overrides com systemctl edit | LPIC 101.3 · RHCSA serviços |
| 4.3 Targets, desligar e reiniciar | multi-user e graphical, target padrão, rescue e emergency, shutdown e wall | LPIC 101.3 · RHCSA targets |
| 4.4 GRUB e acesso de emergência | Parâmetros do kernel com grubby e update-grub; interromper o boot e recuperar a senha de root | LPIC 102.2 · RHCSA bootloader e recuperação |

Desafio do módulo: recuperar a senha de root das duas VMs sem rollback, incluindo o relabel do SELinux na Rocky. A aula 4.4 pede backup no PBS antes.

**M5 · Hardware, kernel e virtualização** · 3 aulas · semana 9

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 5.1 Hardware pelo kernel | /proc, /sys, udev, lspci -k, lsusb, lsblk e dmesg; o que é um driver | LPIC 101.1 |
| 5.2 Módulos e parâmetros | lsmod, modinfo, modprobe, blacklist e sysctl persistente | LPIC 101.1 · EX342 kernel |
| 5.3 Linux como convidado | virtio, guest agent, cloud-init, clones e machine-id; VM e container lado a lado | LPIC 102.6 |

Desafio do módulo: clonar a VM 202 e dar ao clone identidade própria: hostname, machine-id e chaves SSH do host.

**M6 · Software** · 5 aulas · semanas 10 e 11

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 6.1 Pacotes no Debian | dpkg e apt: instalar, remover, purgar, descobrir qual pacote trouxe um arquivo; fontes no formato deb822 | LPIC 102.4 |
| 6.2 Pacotes na Rocky | rpm e dnf: instalar, remover, consultar, histórico e desfazer | LPIC 102.5 · RHCSA pacotes |
| 6.3 Repositórios | Arquivos .repo, chaves GPG, EPEL, repositório local a partir da ISO | LPIC 102.4, 102.5 · RHCSA repositórios |
| 6.4 Flatpak | Remotes, instalar e remover aplicações, Flathub; quando faz sentido num servidor | RHCSA Flatpak |
| 6.5 Bibliotecas compartilhadas | ldd, ldconfig e /etc/ld.so.conf.d; o erro "cannot open shared object file" | LPIC 102.3 · EX342 bibliotecas |

Desafio do módulo: a VM 201 instala pacotes sem internet, só com a ISO como repositório.

**M7 · Processos e desempenho** · 3 aulas · semana 11

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 7.1 Processos e sinais | ps, top, pgrep, pkill, kill e os sinais; estados e zumbis | LPIC 103.5 · RHCSA processos |
| 7.2 Jobs e sessões | &, jobs, fg, bg, nohup e tmux; tarefa longa que sobrevive à queda do SSH | LPIC 103.5 |
| 7.3 Prioridade e perfis | nice, renice e tuned-adm; achar e conter o processo que devora CPU ou memória | LPIC 103.6 · RHCSA prioridade e tuned |

Desafio do módulo: um processo misterioso devora CPU e memória. Ache, rebaixe a prioridade e encerre, sem reiniciar nada.

**M8 · Arquivos a fundo** · 5 aulas · semanas 12 e 13

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 8.1 FHS e onde cada coisa mora | /etc, /var, /usr, /opt e /srv; which, type, whereis e locate | LPIC 104.7 |
| 8.2 find a fundo | Por nome, tipo, dono, tamanho, data e permissão; -exec e xargs com segurança | LPIC 103.3, 104.7 |
| 8.3 Arquivamento avançado | tar com seleção e exclusão, cpio e dd; imagem de disco e checksum | LPIC 103.3 · RHCSA tar |
| 8.4 Links | Inodes, links físicos e simbólicos; o que acontece quando o original some | LPIC 104.6 · RHCSA links |
| 8.5 Permissões avançadas | SUID, SGID, sticky, umask e ACL; diagnosticar "Permission denied" passo a passo | LPIC 104.5 · RHCSA umask e diagnóstico |

Desafio do módulo: três "Permission denied" com causas diferentes; achar cada uma.

**M9 · Armazenamento** · 7 aulas · semanas 13 e 14 · backup no PBS antes

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 9.1 Discos e layout | MBR e GPT, nomes de dispositivo, planejar partições e LVM | LPIC 102.1 |
| 9.2 Particionar | fdisk, gdisk e parted em discos novos adicionados pelo Proxmox | LPIC 104.1 · RHCSA GPT |
| 9.3 Sistemas de arquivos | ext4, XFS e VFAT: criar, rotular e comparar | LPIC 104.1 · RHCSA sistemas de arquivos |
| 9.4 Montar e persistir | mount, /etc/fstab por UUID e LABEL, nofail, units de montagem | LPIC 104.3 · RHCSA montagem |
| 9.5 Integridade e espaço | df, du, fsck, xfs\_repair e tune2fs; disco cheio de verdade | LPIC 104.2 |
| 9.6 LVM | PV, VG e LV: criar, estender, reduzir e remover | RHCSA LVM |
| 9.7 Crescer sem destruir | Nova partição, novo LV e swap sem perder dados; aumentar o disco no Proxmox até o sistema de arquivos | RHCSA armazenamento |

Desafio do módulo: um fstab com erro impede o boot. Conserte pelo modo de emergência.

**Fechamento do bloco A (semana 15):** dois simulados de 60 questões em 90 minutos, revisão do caderno de erros e a prova LPIC-1 101-500.

### Bloco B · rumo ao LPIC-1 102

**M10 · Usuários e acesso privilegiado** · 4 aulas · semana 16

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 10.1 Contas | useradd, usermod e userdel; /etc/passwd, /etc/shadow e /etc/skel | LPIC 107.1 · RHCSA usuários |
| 10.2 Senhas e validade | passwd, chage e /etc/login.defs; bloquear e expirar contas | LPIC 107.1 · RHCSA senhas |
| 10.3 Grupos e trabalho em equipe | groupadd, gpasswd, grupos suplementares, diretório com SGID | LPIC 107.1 · RHCSA grupos |
| 10.4 sudo de verdade | sudoers, visudo, /etc/sudoers.d e privilégio mínimo | LPIC 110.1 · RHCSA acesso privilegiado |

Desafio do módulo: uma equipe de três usuários, senhas que vencem em 90 dias e um operador que só pode reiniciar o nginx.

**M11 · Rede** · 5 aulas · semanas 17 e 18

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 11.1 TCP/IP para quem administra | IPv4 e IPv6, prefixos, portas, TCP, UDP e ICMP | LPIC 109.1 · RHCSA rede |
| 11.2 NetworkManager e nmcli | Conexões, IP fixo, DNS e IPv6; keyfiles | LPIC 109.2 · RHCSA rede |
| 11.3 Rede no Debian | ifupdown, comparado com NetworkManager e systemd-networkd | LPIC 109.2 |
| 11.4 Nomes e resolução | hostnamectl, /etc/hosts, resolv.conf, nsswitch e getent | LPIC 109.4 · RHCSA resolução de nomes |
| 11.5 Diagnóstico de rede | ping, tracepath, ss, dig, nc e tcpdump; onde o pacote some | LPIC 109.3 · EX342 rede |

Desafio do módulo: IP fixo com IPv6 na VM 201 que sobrevive ao reboot; depois, um DNS quebrado de propósito para consertar.

**M12 · Segurança do host** · 5 aulas · semanas 18 e 19

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 12.1 SSH a fundo | Chaves, ssh-agent, \~/.ssh/config, túneis e sshd\_config seguro | LPIC 110.3 · RHCSA SSH |
| 12.2 Firewall | firewalld com zonas, serviços e portas; nftables no Debian | RHCSA firewall |
| 12.3 SELinux: modos e contextos | enforcing e permissive, ls -Z, ps -Z, semanage fcontext e restorecon | RHCSA SELinux |
| 12.4 SELinux: portas e booleanos | semanage port, setsebool -P, ler um AVC; AppArmor no Debian | RHCSA SELinux |
| 12.5 Auditoria e criptografia | SUID esquecido, portas abertas, last, who e ulimit; cifrar e assinar com GPG | LPIC 110.1, 110.2, 110.3 |

Desafio do módulo: nginx numa porta e num diretório fora do padrão, com SELinux enforcing e firewall ativo, sem desligar nada.

**M13 · Armazenamento em rede** · 3 aulas · semanas 19 e 20 · VM 203 entra

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 13.1 Servidor NFS | Criar a VM 203, exportar diretórios, firewall e SELinux do NFS | base do RHCSA NFS |
| 13.2 Cliente NFS | Montar na mão e no fstab, `_netdev` e opções; o erro "stale file handle" | RHCSA NFS |
| 13.3 autofs | Mapas mestre e indiretos; homes montados sob demanda | RHCSA autofs |

Desafio do módulo: homes de usuários de rede montados sozinhos nas VMs 201 e 202.

**M14 · Agendamento, logs e hora** · 5 aulas · semanas 20 e 21

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 14.1 cron e at | crontab de usuário e de sistema, /etc/cron.d, at e controle de acesso | LPIC 107.2 · RHCSA agendamento |
| 14.2 Timers do systemd | Par .timer e .service, OnCalendar, Persistent e list-timers | LPIC 107.2 · RHCSA timers |
| 14.3 journald e rsyslog | Filtrar o journal, journal persistente, rsyslog e logrotate | LPIC 108.2 · RHCSA logs e journal persistente |
| 14.4 Hora certa | chrony como cliente, timedatectl e fusos; o que quebra quando a hora erra | LPIC 108.1 · RHCSA serviço de hora |
| 14.5 E-mail local e impressão | MTA básico com Postfix, aliases e mail; CUPS e lp | LPIC 108.3, 108.4 |

Desafio do módulo: backup diário por timer, com log no journal e aviso por e-mail local quando falhar.

**M15 · Shell e ambiente** · 5 aulas · semanas 21 e 22

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 15.1 Ambiente do shell | Variáveis, export, PATH, \~/.bashrc, /etc/profile.d, aliases e funções | LPIC 105.1 |
| 15.2 Scripts robustos | Argumentos, testes, laços, case, funções e códigos de saída | LPIC 105.2 · RHCSA scripts |
| 15.3 Scripts de administração | Usar a saída de comandos, gerar relatório, rodar em várias VMs por SSH | LPIC 105.2 · RHCSA scripts |
| 15.4 Interfaces gráficas | X11 e Wayland, display manager, desktops e acessibilidade; instalar num snapshot e voltar | LPIC 106.1, 106.2, 106.3 |
| 15.5 Idioma, teclado e fuso | locale, localectl, UTF-8 e iconv | LPIC 107.3 |

Desafio do módulo: um script de saúde (disco, memória, serviços, último backup) com código de saída que o Zabbix vai ler na Fase 4.

**Fechamento do bloco B (semana 23):** dois simulados de 60 questões, revisão do caderno de erros e a prova LPIC-1 102-500.

### Bloco C · reta final do RHCSA

**M16 · RHCSA no Rocky 10** · 4 aulas · semana 24 · VM 205 entra

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 16.1 Rocky 10 para a prova | Criar a VM 205, o que muda do 9 para o 10, releitura dos objetivos oficiais | RHCSA |
| 16.2 Simulado 1 por blocos | Tarefas por área, com dicas liberadas aos poucos | RHCSA |
| 16.3 Simulado 2 cronometrado | Prova inteira sem internet, só man e /usr/share/doc, reboot no fim | RHCSA |
| 16.4 Correção e reforço | Correção por script de verificação e plano para os pontos fracos | RHCSA |

**Prova (semana 25):** RHCSA EX200. Agende só quando o simulado 16.3 passar inteiro depois do reboot.

## Fase 3 · Engenheiro

Semanas 26 a 35 · 34 aulas · uma prova: EX294 (semana 35), que somada ao RHCSA dá o RHCE em Ansible.

Meta da fase: fazer uma vez à mão e, daí em diante, deixar a automação repetir. Primeiro as ferramentas de engenheiro (Git, VS Code e Podman), depois os serviços de rede montados à mão e, por fim, o Ansible. Regra da fase: todo playbook vai para o Git e roda duas vezes; a segunda execução tem que terminar com `changed=0`.

**M17 · Git e VS Code** · 4 aulas · semana 26

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 17.1 Git do zero | init, add, commit, status, log e diff; .gitignore; desfazer com restore e revert | EX294 Git |
| 17.2 Repositório central | Repositório bare na VM 203 por SSH; clone, push, pull, branch e merge; resolver um conflito | EX294 Git |
| 17.3 VS Code como estação de trabalho | Remote - SSH a partir do Windows, terminal integrado e as extensões de YAML e Ansible | EX294 VS Code |
| 17.4 YAML sem sustos | Indentação, listas, dicionários, textos de várias linhas e aspas; yamllint e os erros clássicos | EX294 playbooks |

Desafio do módulo: os scripts das fases 1 e 2 versionados na VM 203, com mensagens de commit claras e um conflito resolvido.

**M18 · Podman** · 4 aulas · semana 27

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 18.1 Contêiner não é VM | Imagens, camadas, registries e namespaces; podman pull, images e inspect | base do ansible-navigator |
| 18.2 Rodar e persistir | run, ps, logs e exec; portas e volumes com `:Z`; contêiner rootless e o SELinux | base do ansible-navigator |
| 18.3 Contêiner como serviço | Quadlet com arquivo .container, systemctl --user e loginctl enable-linger | Profissional |
| 18.4 Construir imagens | Containerfile, podman build, tags e registry local; o que é um execution environment do Ansible | base do EX294 |

Desafio do módulo: um nginx rootless com conteúdo persistente que sobe sozinho no boot, sem ninguém logado.

**M19 · Serviços de rede** · 8 aulas · semanas 28 e 29 · VM 204 entra

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 19.1 DNS autoritativo | Criar a VM 204; BIND com zona direta e reversa do lab; named-checkconf e named-checkzone | Profissional |
| 19.2 DNS recursivo e diagnóstico | Cache, encaminhadores e TTL; dig +trace; por que a culpa costuma ser do DNS | Profissional · EX342 rede |
| 19.3 DHCP com Kea | Rede isolada só do lab no Proxmox; Kea DHCPv4 com reservas e leases | Profissional |
| 19.4 Servidor web | nginx e Apache nas duas famílias: virtual hosts, logs e permissões; SELinux na Rocky, AppArmor no Debian | Profissional |
| 19.5 TLS e proxy reverso | CA própria com openssl, certificado com SAN, HTTPS e proxy reverso para o contêiner do M18 | Profissional |
| 19.6 Samba, a ponte Windows | Compartilhamento com usuários e permissões, samba\_share\_t na Rocky; mapear a unidade no Windows 11 | Profissional |
| 19.7 Postfix | Registro MX no BIND, domínio do lab, aliases, fila e logs; relay só para a rede interna | Profissional |
| 19.8 Dovecot e teste ponta a ponta | IMAP com o certificado da 19.5; enviar, entregar, ler e seguir a mensagem pelos logs | Profissional |

Desafio do módulo: uma VM nova liga na rede isolada, recebe IP do Kea, resolve nomes pelo BIND, abre o site em HTTPS e lê um e-mail. Cada passo fica anotado no Git, pronto para virar playbook.

**M20 · Ansible I · fundamentos** · 4 aulas · semana 30 · VMs 210 a 212 entram

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 20.1 Nó de controle | Criar as VMs 210 a 212; instalar ansible-core e ansible-navigator; dev container no VS Code | EX294 instalar e configurar |
| 20.2 Inventário e ansible.cfg | Inventário em INI e YAML, grupos e grupos de grupos; usuário com chave SSH e sudo nos nós | EX294 inventário, chaves e become |
| 20.3 Ad hoc e documentação | ansible -m, ansible-doc e ansible-navigator doc; o módulo certo em vez de shell | EX294 ad hoc e documentação |
| 20.4 Primeiro playbook | Plays e tasks, idempotência, --syntax-check, --check e --diff; commit e push | EX294 playbooks e Git |

Desafio do módulo: um playbook que prepara os nós do zero e termina com `changed=0` na segunda execução.

**M21 · Ansible II · playbooks de verdade** · 8 aulas · semanas 31 e 32

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 21.1 Variáveis e precedência | vars, group\_vars, host\_vars e extra vars; quem ganha quando dois definem | EX294 variáveis |
| 21.2 Facts e register | gather\_facts, ansible\_facts, facts customizados e register | EX294 facts e variáveis registradas |
| 21.3 Condicionais | when com facts, variáveis e resultados; testes como is defined | EX294 condicionais |
| 21.4 Loops | loop e loop\_control sobre listas e dicionários | EX294 loops |
| 21.5 Handlers | notify, listen e flush\_handlers; reiniciar só quando algo mudou | EX294 handlers |
| 21.6 Tratar erros | ignore\_errors, failed\_when e changed\_when; block, rescue e always | EX294 tratamento de erros |
| 21.7 Templates Jinja2 | Módulo template, filtros, laços e condicionais; um arquivo diferente por host | EX294 templates |
| 21.8 Ansible Vault | create, edit, rekey e vault-id; arquivo de senha fora do Git | EX294 Vault |

Desafio do módulo: nginx com página gerada por template, reinício só quando a configuração muda e uma senha protegida pelo Vault.

**M22 · Ansible III · roles e o RHCSA automatizado** · 6 aulas · semanas 33 e 34 · backup no PBS antes

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 22.1 Roles | Estrutura, defaults e vars, ansible-galaxy role init; transformar o playbook do M21 em role | EX294 roles |
| 22.2 Collections | FQCN, requirements.yml e ansible-galaxy collection install; RHEL System Roles | EX294 Collections |
| 22.3 RHCSA automatizado I | Usuários, grupos, pacotes, serviços, firewall, agendamento e arquivos | EX294 tarefas de administração |
| 22.4 RHCSA automatizado II | Partições, LVM, sistemas de arquivos, montagens e SELinux | EX294 tarefas de administração |
| 22.5 Simulado 1 | Tarefas por área em nós restaurados do PBS, com dicas liberadas aos poucos | EX294 |
| 22.6 Simulado 2 e correção | Prova inteira cronometrada em nós limpos; correção por script e plano para os pontos fracos | EX294 |

Desafio do módulo: um nó vazio vira servidor pronto com um único ansible-navigator run, combinando roles suas e System Roles.

**Prova (semana 35):** EX294. Agende só quando o simulado 22.6 passar inteiro em nós restaurados do zero, porque a correção da Red Hat também usa sistemas novos.

## Fase 4 · Profissional

Semanas 36 a 46 · 38 aulas · uma prova: EX342 (semana 46), que somada ao RHCSA dá o RHCE em Enterprise Linux.

Meta da fase: operar como sênior. Ver o problema antes do usuário, reconstruir depois do desastre e diagnosticar o que ninguém documentou. A fase termina no troubleshooting do EX342: quatro horas consertando sistemas que outra pessoa quebrou.

**M23 · Monitoramento** · 4 aulas · semana 36

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 23.1 O servidor por dentro | Cockpit, sar e PCP; a linha de base do que é normal | EX342 monitoramento e Cockpit |
| 23.2 Zabbix | Servidor na VM 204 e agentes nas VMs do curso; hosts, templates e painéis | Profissional |
| 23.3 Alertas que importam | Item com o script de saúde do M15, triggers sem alarme falso e aviso pelo Postfix do M19 | Profissional |
| 23.4 O que vence e o que enche | Certificados perto do vencimento, serviços parados e disco enchendo; previsão de capacidade | Profissional |

Desafio do módulo: derrubar um serviço, encher um disco e emitir um certificado que vence amanhã. O Zabbix avisa sobre os três antes de você abrir o terminal.

**M24 · Logs centralizados e integridade** · 4 aulas · semana 37 · VM 203 vira servidor de logs

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 24.1 rsyslog central | Servidor na VM 203, clientes por TCP e um diretório por host; a porta no firewall e no SELinux | EX342 log centralizado |
| 24.2 Journal remoto | systemd-journal-remote e systemd-journal-upload; quando usar cada solução | EX342 log centralizado |
| 24.3 auditd | Regras para arquivos e comandos sensíveis; ausearch e aureport; quem mexeu no sudoers | EX342 segurança |
| 24.4 AIDE | Base de integridade, verificação diária por timer e investigação de uma mudança plantada | EX342 AIDE e arquivos alterados |

Desafio do módulo: alguém trocou um binário e editou uma configuração. Descubra o quê, quando e quem, só com os logs centrais, o auditd e o AIDE.

**M25 · Backup e recuperação** · 4 aulas · semana 38

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 25.1 Estratégia antes da ferramenta | 3-2-1, RPO e RTO; o que copiar e o que reconstruir; plano de backup por escrito | Profissional |
| 25.2 PBS a fundo | Num namespace só do curso: retenção, verify, sync e restauração de um único arquivo | Profissional |
| 25.3 Backup dentro do Linux | restic ou borg com criptografia, dump de banco e restauração testada | Profissional |
| 25.4 Dia do desastre | Uma VM perdida de propósito: restaurar, conferir os dados e medir o RTO real | Profissional |

Desafio do módulo: com o cronômetro ligado, a VM 204 volta inteira do PBS e todos os serviços do M19 respondem.

**M26 · Desempenho e depuração** · 5 aulas · semanas 39 e 40

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 26.1 Método USE | Uso, saturação e erros de CPU, memória, disco e rede; vmstat, mpstat e pidstat | EX342 método |
| 26.2 Memória | free, /proc/meminfo, pmap, swap e OOM killer; achar um vazamento com valgrind | EX342 vazamento de memória |
| 26.3 Disco e I/O | iostat, iotop e fio; latência e vazão; o disco Ceph visto de dentro da VM | Profissional |
| 26.4 Ferramentas de depuração | strace, ltrace, ldd, gdb e coredumpctl; por que o programa morreu | EX342 depuração e bibliotecas |
| 26.5 Ajuste fino | tuned, sysctl, limits e limites de recursos no systemd; medir antes e depois | Profissional |

Desafio do módulo: um serviço fica lento sem motivo aparente. Prove com números onde está o gargalo antes de mudar qualquer coisa.

**M27 · Alta disponibilidade** · 5 aulas · semanas 40 e 41 · VMs 220 a 222 entram

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 27.1 Conceitos de HA | Ponto único de falha, quorum, split-brain e fencing; criar as VMs 220 a 222 | Profissional |
| 27.2 IP flutuante | keepalived com VRRP e verificação de serviço; derrubar o mestre e ver o IP mudar de nó | Profissional |
| 27.3 HAProxy | Balancear dois servidores web, health checks e página de estatísticas | Profissional |
| 27.4 Pacemaker e pcs | Cluster de três nós, recursos, restrições e ordem; IP virtual junto com o serviço | Profissional |
| 27.5 Fencing e testes de falha | fence\_pve pela API do Proxmox, com usuário restrito às VMs 220 a 222; HA do Proxmox ou da aplicação? | Profissional |

Desafio do módulo: desligar a placa de rede do nó ativo no meio de um teste de carga. O serviço volta sozinho em segundos e o fencing aparece no log.

**M28 · Hardening** · 5 aulas · semanas 41 e 42

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 28.1 Medir antes de endurecer | OpenSCAP com um perfil CIS; relatório e remediação escolhida item a item | Profissional |
| 28.2 SSH e senhas | sshd\_config.d só com chave e sem login de root; política de senha com pwquality | EX342 políticas de conta |
| 28.3 PAM | authselect na Rocky, pam-auth-update no Debian; faillock e acesso por grupo | EX342 PAM |
| 28.4 LUKS | Disco cifrado, crypttab, slots de chave e backup do cabeçalho; recuperar o acesso | EX342 LUKS |
| 28.5 Superfície mínima | Menos serviços e portas, fail2ban, atualizações automáticas; módulo SELinux com audit2allow | EX342 SELinux |

Desafio do módulo: subir a nota do OpenSCAP da VM 201 sem perder o acesso SSH, com cada mudança justificada num commit.

**M29 · Operação de Proxmox e Ceph** · 5 aulas · semanas 42 e 43 · VMs 230 a 232 entram; o cluster real não é tocado

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 29.1 Proxmox dentro do Proxmox | Três VMs com Proxmox VE e virtualização aninhada; criar o cluster com pvecm | Profissional |
| 29.2 Cluster e quorum | corosync, pvecm status, perda de nó e de quorum; migração e regras de HA | Profissional |
| 29.3 Ceph por dentro | ceph -s, OSDs, pools e PGs; substituir um OSD com defeito | Profissional |
| 29.4 Atualizar sem parar | Atualização nó a nó: migrar, noout, reiniciar, conferir a saúde e seguir | Profissional |
| 29.5 Automatizar e documentar | Template com cloud-init, qm clone, API com token e Ansible; o runbook de incidente | Profissional |

Desafio do módulo: um nó do cluster aninhado morre sem aviso. Recupere o quorum, a saúde do Ceph e as VMs seguindo o seu runbook.

**M30 · Troubleshooting rumo ao EX342** · 6 aulas · semanas 44 e 45 · na VM 205

| Aula | O que você faz | Prova |
| --- | --- | --- |
| 30.1 Método e sos | Hipótese, teste e registro; sos report e a documentação oficial como ferramenta | EX342 método e sos |
| 30.2 Boot quebrado | GRUB, initramfs com dracut, rd.break e emergency.target; acesso de root perdido | EX342 boot e acesso de root |
| 30.3 Disco quebrado | fsck e xfs\_repair, LVM apagado com vgcfgrestore, LUKS sem a senha principal | EX342 sistemas de arquivos, LVM e LUKS |
| 30.4 Pacotes quebrados | rpm --rebuilddb, rpm -Va, dependências quebradas e arquivos alterados | EX342 RPM |
| 30.5 Rede, kernel e hardware | tcpdump e tshark; kdump e crash; lshw, dmidecode e módulos | EX342 rede, kdump e hardware |
| 30.6 Simulado de 4 horas | Defeitos plantados por script na VM 205 restaurada; um diário para cada diagnóstico | EX342 |

**Prova (semana 46):** EX342. Agende só quando o simulado 30.6 fechar dentro das 4 horas, com todos os defeitos resolvidos e explicados no diário.

**Depois da semana 46:** um !quebra por semana no DeepTutor e um dia do desastre por mês mantêm tudo afiado.

## Cronograma

46 semanas, 155 aulas e 6 provas. O ritmo de referência é de 4 aulas por semana, de 60 a 90 minutos cada. Com 5 ou 6 aulas por semana o calendário encolhe; com 2 ou 3, estica. Quem decide a data da prova é o simulado, nunca o calendário.

| Fase | Semanas | Aulas | Módulos | Provas |
| --- | --- | --- | --- | --- |
| 1 · Fundamentos | 1 a 6 | 20 | M0 a M2 | Linux Essentials 010-200 (semana 6) |
| 2 · Administrador | 7 a 25 | 63 | M3 a M16 | LPIC-1 101 (semana 15), LPIC-1 102 (semana 23) e RHCSA (semana 25) |
| 3 · Engenheiro | 26 a 35 | 34 | M17 a M22 | EX294, RHCE em Ansible (semana 35) |
| 4 · Profissional | 36 a 46 | 38 | M23 a M30 | EX342, RHCE em Enterprise Linux (semana 46) |

Começando na segunda-feira, 2 de novembro de 2026, e sem pausas, a semana 46 começa em 13 de setembro de 2027. Com duas semanas de folga no Natal e três em agosto, a última prova cai na segunda quinzena de outubro de 2027.

### A semana típica

| Quando | O que você faz | Tempo |
| --- | --- | --- |
| Começo de cada sessão | Revisões que vencem hoje, com o DeepTutor e sem consulta | 10 a 15 min |
| 4 sessões por semana | Uma aula completa: aquecimento, conceito, lab, quebre e conserte, quiz | 60 a 90 min |
| 1 sessão por semana | Desafio do módulo ou um !quebra no DeepTutor | 45 a 60 min |
| Fim da semana | Diário de bordo, caderno de erros, snapshot de fim e conferência do backup no PBS | 15 a 20 min |

### Revisão espaçada

Cada aula termina com 5 a 10 flashcards. Cada cartão volta 1, 3, 7 e 21 dias depois da aula (D+1, D+3, D+7 e D+21). Acertou sem hesitar: o cartão segue para o intervalo seguinte. Errou ou hesitou: volta para D+1. Depois do D+21, o cartão só reaparece nos simulados. As revisões não passam de 15 minutos por dia; se acumularem, comece pelas mais atrasadas.

### Simulados e critério para agendar

| Prova | Simulados | Semana | Agende quando |
| --- | --- | --- | --- |
| Linux Essentials 010-200 | 2 de 40 questões em 60 min | 6 | O segundo passar de 80% |
| LPIC-1 101-500 | 2 de 60 questões em 90 min | 15 | O segundo passar de 80% |
| LPIC-1 102-500 | 2 de 60 questões em 90 min | 23 | O segundo passar de 80% |
| RHCSA EX200 | Aulas 16.2 e 16.3 | 24 | O 16.3 passar inteiro depois do reboot |
| EX294 | Aulas 22.5 e 22.6 | 34 | O 22.6 passar inteiro em nós restaurados do zero |
| EX342 | Aula 30.6 | 45 | Todos os defeitos resolvidos dentro das 4 horas |

Antes de agendar, confira na página oficial a versão da prova e dos objetivos: as provas mudam, e o plano muda junto.

### Caderno de erros

Todo erro vira uma linha: data, aula, o que aconteceu, a causa e a regra que impede a repetição. Erro que aparece duas vezes vira flashcard. Na semana de cada prova, o caderno é a primeira coisa que você relê.

### Se atrasar

Perdeu uma semana? Não comprima duas em uma: empurre o calendário inteiro. Faça só as revisões vencidas e retome de onde parou. Pular o lab para ganhar tempo é a única economia proibida.

## Prompt do tutor no DeepTutor

Cole o texto abaixo nas instruções do DeepTutor. Se a sua versão não tiver esse campo, cole como primeira mensagem de cada conversa nova. Ele transforma o modelo num tutor que pergunta antes de responder, segue a anatomia das aulas e respeita os limites do laboratório.

```text
Você é o tutor particular do curso "Linux Sysadmin", do Linux Essentials ao RHCE. Fale sempre em português do Brasil.

QUEM É O ALUNO
- Sysadmin que vem do Windows Server e já usa Proxmox, NethServer e firewalls no trabalho. Está construindo uma base Linux sólida, do zero, rumo ao RHCE.
- Laboratório num cluster Proxmox. VMs do curso: 201 rocky-lab (Rocky Linux 9), 202 debian-lab (Debian 13), 203 srv-lab (Rocky 9: NFS, Git e logs), 204 srv-deb (Debian 13: serviços de rede), 205 rocky10-lab (Rocky Linux 10), 210 a 212 (Ansible), 220 a 222 (alta disponibilidade) e 230 a 232 (Proxmox aninhado).
- Provas: Linux Essentials 010-200, LPIC-1 101-500 e 102-500, RHCSA EX200 (RHEL 10), EX294 (RHCE em Ansible) e EX342 (RHCE em Enterprise Linux, troubleshooting).

COMO VOCÊ ENSINA
1. Abra cada sessão perguntando em que aula o aluno está (por exemplo, 1.3). Faça 3 perguntas de revisão das aulas anteriores, uma por vez, sem consulta, e corrija cada uma em uma ou duas frases.
2. Nunca entregue a resposta antes de o aluno tentar. Dê dicas em três níveis: pista, direção e, só se ele pedir, a solução comentada.
3. Antes de cada comando, peça que o aluno preveja a saída. Depois compare previsão e resultado.
4. Sempre que houver diferença, mostre Rocky e Debian lado a lado: pacotes, caminhos, firewall, SELinux e AppArmor, grupo wheel e grupo sudo.
5. Quando ajudar, compare com o equivalente no Windows Server.
6. Peça que o aluno explique com as próprias palavras, como se ensinasse um colega. Aponte o que faltou ou ficou errado.
7. Para cada erro, diga o tipo (conceito, sintaxe ou distração) e sugira a linha para o caderno de erros.
8. Diga a qual objetivo de prova o assunto pertence (por exemplo, LE 013.2, LPIC 103.4 ou RHCSA). Não invente objetivos.
9. Uma pergunta por mensagem, mensagens curtas e comandos sempre em bloco de código.
10. Se não tiver certeza de um detalhe de versão, diga isso e mostre como conferir: man, --help, /usr/share/doc ou a documentação oficial.

SEGURANÇA DO LABORATÓRIO
- Comandos destrutivos só nas VMs do curso (201 a 232) e só depois de o aluno confirmar que existe snapshot ou backup.
- Nunca proponha nada que mexa nas VMs 100 a 103 nem no CT 108, onde você mesmo roda. No host Proxmox, só comandos de leitura ou comandos qm com os IDs do curso.
- Nunca peça senhas, tokens ou chaves privadas. Se o aluno colar um segredo, peça que ele troque esse segredo e não o repita.

COMANDOS
!quiz [aula ou tema]: 5 perguntas, uma por vez, misturando múltipla escolha, completar o comando e "o que acontece se". No fim, gabarito comentado e nota.
!quebra [tema]: incidente simulado. Descreva só o sintoma. O aluno pede comandos e você responde com saídas realistas de Rocky ou Debian, sem revelar a causa, até ele diagnosticar e propor a correção. No fim, explique a causa e como evitar.
!simulado [prova] [n]: n questões no estilo da prova. Nas provas da LPI, múltipla escolha e completar; nas da Red Hat, tarefas práticas com critério de verificação. Marque o tempo, corrija no fim e liste os pontos fracos.
!revisao [cartões ou aula]: pergunte os cartões que vencem hoje, um por vez, sem mostrar a resposta antes. No fim, diga quais avançam para o próximo intervalo e quais voltam para D+1.
!cartoes [aula]: gere de 5 a 10 flashcards de pergunta e resposta curtas para a revisão espaçada.
!explica [conceito]: explique em camadas: analogia, o essencial, o aprofundamento e o que cai na prova.
!feynman [tema]: o aluno explica o tema; você avalia clareza, precisão e lacunas, com nota de 0 a 10.
!erro: o aluno cola uma mensagem de erro; você guia o diagnóstico com perguntas antes de sugerir qualquer correção.
```

Para testar, mande `!quiz 1.1`: o tutor deve fazer uma pergunta por vez e esperar a sua resposta antes de corrigir.
