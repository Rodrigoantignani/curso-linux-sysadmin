# Aulas

Índice das **61 aulas publicadas**, do M0 à Aula 11.5. Cada título leva direto ao arquivo da aula; a coluna Semana segue o cronograma do [plano do curso](00-plano-do-curso.md).

**Cobertura atual:** 56 de 188 aulas · semanas 1 a 15 de 48.

## Como estudar uma aula

1. Leia a **Ficha** e responda o **Aquecimento** de cabeça, sem consultar nada. Errar aqui faz parte: a pergunta prepara a memória para receber a resposta.
2. Leia o **Modelo mental** e o **Conceito em camadas**. Onde aparecer **Preveja**, escreva sua aposta no diário de bordo antes de rodar o comando.
3. Faça o **Lab guiado** com o snapshot de início tirado, digitando os comandos em vez de colar.
4. **Quebre e conserte.** Depois responda o **Quiz** sem olhar a aula e só então abra o **Gabarito** comentado, no fim do arquivo.
5. Marque o **Checklist de saída**, tire o snapshot de fim e abra o **DeepTutor** com os comandos da seção Com o DeepTutor.
6. Revise cada aula no DeepTutor com `!revisao` 1, 3, 7 e 21 dias depois de estudá-la.

## Fase 1 · Fundamentos · 20 aulas · semanas 1 a 6

Meta da fase: usar o terminal com segurança e entender o que cada comando faz por baixo, nas duas distros. A fase fecha com um dia de incidente nas duas VMs.

### M0 · Laboratório · 2 aulas · semana 1

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [0.1 · Montar o laboratório](aulas/0.1-montar-o-laboratorio.md) | 1 | Criar as VMs 201 e 202 com `qm create`, instalar Rocky 9 e Debian 13 entendendo cada tela e conferir o resultado em cinco comandos |
| [0.2 · Acesso e proteção](aulas/0.2-acesso-e-protecao.md) | 1 | Entrar por SSH com chave Ed25519, usar `sudo`, falar com o guest agent, tirar snapshots e fazer backup no PBS com teste de restauração |

**Desafio do módulo:** quebrar uma VM de propósito e voltar pelo snapshot em menos de dois minutos.

### M1 · Linha de comando · 10 aulas · semanas 1 a 3

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [1.1 · O que é Linux](aulas/1.1-o-que-e-linux.md) | 1 | Kernel, distribuição e famílias; identificar qualquer Linux em 30 segundos; Proxmox, NethServer 8 e NethSecurity no mapa |
| [1.2 · O shell e a ajuda](aulas/1.2-o-shell-e-a-ajuda.md) | 1 | Anatomia de um comando, `PATH`, `man` e suas seções, `apropos`, `info`, `/usr/share/doc`, histórico e atalhos |
| [1.3 · Caminhos e navegação](aulas/1.3-caminhos-e-navegacao.md) | 2 | Árvore de diretórios, caminhos absolutos e relativos, `cd`, `ls`, curingas e arquivos ocultos |
| [1.4 · Criar, copiar, mover e apagar](aulas/1.4-criar-copiar-mover-e-apagar.md) | 2 | `mkdir`, `touch`, `cp`, `mv` e `rm` com segurança; por que o terminal não tem lixeira |
| [1.5 · Ler e procurar texto](aulas/1.5-ler-e-procurar-texto.md) | 2 | `cat`, `less`, `head`, `tail -f`, `wc` e `grep` básico; ler log sem abrir editor |
| [1.6 · Redirecionamentos e pipes](aulas/1.6-redirecionamentos-e-pipes.md) | 2 | `stdin`, `stdout`, `stderr`, `>`, `>>`, `2>`, `2>&1`, pipe e `tee`; montar um comando por partes |
| [1.7 · Arquivar e compactar](aulas/1.7-arquivar-e-compactar.md) | 3 | `tar` com gzip, bzip2 e xz, `zip`; listar e testar antes de extrair |
| [1.8 · Primeiro script](aulas/1.8-primeiro-script.md) | 3 | Shebang, variáveis, aspas, argumentos `$1` e `$#`, permissão de execução |
| [1.9 · Decidir e repetir](aulas/1.9-decidir-e-repetir.md) | 3 | Código de saída, `test` e `[ ]`, `if`, `for`, `while` e `$(comando)` |
| [1.10 · Software livre na prática](aulas/1.10-software-livre-na-pratica.md) | 3 | Licenças GPL, MIT e Apache, aplicações open source, modelos de negócio e Linux na nuvem |

**Desafio do módulo:** um script `inventario.sh` que mostra nome, distro, kernel, IP, memória e disco livre, com a mesma saída nas duas VMs.

### M2 · Sistema, usuários e permissões · 8 aulas · semanas 4 e 5

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [2.1 · Instalação e provisionamento](aulas/2.1-instalacao-e-provisionamento.md) | 4 | Instalação manual, imagem de nuvem com cloud-init e a diferença entre VM e contêiner |
| [2.2 · Hardware e dispositivos](aulas/2.2-hardware-e-dispositivos.md) | 4 | `/dev`, `lsblk`, `lspci`, `lsusb` e `dmesg`; como o Linux enxerga disco, rede e USB |
| [2.3 · Processos e logs](aulas/2.3-processos-e-logs.md) | 4 | `ps`, `top`, `kill`, `systemctl status` e `journalctl`; quem está usando a CPU e por quê |
| [2.4 · Rede no dia a dia](aulas/2.4-rede-no-dia-a-dia.md) | 4 | `ip`, `ss`, `ping`, `getent`, `dig` e `/etc/hosts`; o caminho de um pacote até a internet |
| [2.5 · Acesso remoto e privilégios](aulas/2.5-acesso-remoto-e-privilegios.md) | 5 | `ssh`, `scp`, `sftp`, `su` e `sudo`; transferir arquivos com segurança |
| [2.6 · Usuários e grupos](aulas/2.6-usuarios-e-grupos.md) | 5 | `/etc/passwd`, `/etc/group`, `id`, `useradd` e `passwd`; grupo primário e suplementar |
| [2.7 · Permissões e dono](aulas/2.7-permissoes-e-dono.md) | 5 | `rwx` em arquivo e em diretório, `chmod` simbólico e octal, `chown` e `umask` |
| [2.8 · Diretórios e arquivos especiais](aulas/2.8-diretorios-e-arquivos-especiais.md) | 5 | `/tmp` e sticky bit, SUID e SGID, links simbólicos, `/proc`, `/sys` e `/dev` |

**Desafio do módulo:** uma pasta `/srv/equipe` onde dois usuários criam e editam arquivos, mas nenhum apaga o arquivo do outro, nas duas VMs.

**Fechamento da fase (semana 6):** revisão espaçada de M0 a M2 e um dia de incidente nas duas VMs, sem consulta.

## Fase 2 · Administrador · 36 aulas publicadas de 63 · semanas 7 a 15

Meta da fase: administrar sozinho um servidor Linux de ponta a ponta, nas duas famílias, com tudo sobrevivendo ao reboot. Todo lab termina com reboot e verificação.

### M3 · Texto e editor · 5 aulas · semanas 7 e 8

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [3.1 · Fluxos a fundo](aulas/3.1-fluxos-a-fundo.md) | 7 | `tee`, `xargs`, here-doc, substituição de processo e `/dev/null`; pipelines que não escondem erro |
| [3.2 · Filtros de texto](aulas/3.2-filtros-de-texto.md) | 7 | `cut`, `sort`, `uniq`, `tr`, `paste`, `nl`, `split`, `od` e `sha256sum`; transformar log em relatório |
| [3.3 · Regex e grep](aulas/3.3-regex-e-grep.md) | 7 | BRE e ERE, âncoras, classes e grupos; `grep -E`, `-v`, `-o` e `-r` |
| [3.4 · sed e awk](aulas/3.4-sed-e-awk.md) | 8 | Substituir, apagar e extrair linhas com `sed`; colunas, filtros e somas com `awk` |
| [3.5 · vi e vim de verdade](aulas/3.5-vi-e-vim-de-verdade.md) | 8 | Modos, movimentos, busca, substituição e desfazer; editar configuração sem medo |

**Desafio do módulo:** os 10 IPs que mais erraram senha no SSH, numa linha de comando, nas duas VMs.

### M4 · Boot e systemd · 4 aulas · semanas 8 e 9

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [4.1 · Como o Linux liga](aulas/4.1-como-o-linux-liga.md) | 8 | UEFI, GRUB 2, kernel, initramfs e systemd; ler o boot com `journalctl -b` e `systemd-analyze` |
| [4.2 · systemd: serviços e units](aulas/4.2-systemd-servicos-e-units.md) | 8 | `start`, `stop`, `enable` e `mask`; dependências e overrides com `systemctl edit` |
| [4.3 · Targets, desligar e reiniciar](aulas/4.3-targets-desligar-e-reiniciar.md) | 9 | `multi-user` e `graphical`, target padrão, `rescue` e `emergency`, `shutdown` e `wall` |
| [4.4 · GRUB e acesso de emergência](aulas/4.4-grub-e-acesso-de-emergencia.md) | 9 | Parâmetros do kernel com `grubby` e `update-grub`; interromper o boot e recuperar a senha de root |

**Desafio do módulo:** recuperar a senha de root das duas VMs sem rollback, incluindo o relabel do SELinux na Rocky.

### M5 · Hardware, kernel e virtualização · 3 aulas · semana 9

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [5.1 · Hardware pelo kernel](aulas/5.1-hardware-pelo-kernel.md) | 9 | `/proc`, `/sys`, `udev`, `lspci -k`, `lsusb`, `lsblk` e `dmesg`; o que é um driver |
| [5.2 · Módulos e parâmetros](aulas/5.2-modulos-e-parametros.md) | 9 | `lsmod`, `modinfo`, `modprobe`, blacklist e `sysctl` persistente |
| [5.3 · Linux como convidado](aulas/5.3-linux-como-convidado.md) | 9 | virtio, guest agent, cloud-init, clones e `machine-id`; VM e contêiner lado a lado |

**Desafio do módulo:** clonar a VM 202 e dar ao clone identidade própria: hostname, `machine-id` e chaves SSH do host.

### M6 · Software · 5 aulas · semanas 10 e 11

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [6.1 · Pacotes no Debian](aulas/6.1-pacotes-no-debian.md) | 10 | `dpkg` e `apt`: instalar, remover, purgar e descobrir qual pacote trouxe um arquivo; fontes no formato deb822 |
| [6.2 · Pacotes na Rocky](aulas/6.2-pacotes-na-rocky.md) | 10 | `rpm` e `dnf`: instalar, remover, consultar, verificar integridade e desfazer pelo histórico |
| [6.3 · Repositórios](aulas/6.3-repositorios.md) | 10 | Arquivos `.repo`, chaves GPG, EPEL e repositório local a partir da ISO |
| [6.4 · Flatpak](aulas/6.4-flatpak.md) | 11 | Remotes, instalar e remover aplicações, Flathub; quando faz sentido num servidor |
| [6.5 · Bibliotecas compartilhadas](aulas/6.5-bibliotecas-compartilhadas.md) | 11 | `ldd`, `ldconfig` e `/etc/ld.so.conf.d`; o erro `cannot open shared object file` |

**Desafio do módulo:** a VM 201 instala pacotes sem internet, só com a ISO como repositório.

### M7 · Processos e desempenho · 3 aulas · semana 11

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [7.1 · Processos e sinais](aulas/7.1-processos-e-sinais.md) | 11 | `ps`, `top`, `pgrep`, `pkill`, `kill` e os sinais; estados e zumbis |
| [7.2 · Jobs e sessões](aulas/7.2-jobs-e-sessoes.md) | 11 | `&`, `jobs`, `fg`, `bg`, `nohup` e `tmux`; tarefa longa que sobrevive à queda do SSH |
| [7.3 · Prioridade e perfis](aulas/7.3-prioridade-e-perfis.md) | 11 | `nice`, `renice` e `tuned-adm`; achar e conter o processo que devora CPU ou memória |

**Desafio do módulo:** um processo misterioso devora CPU e memória. Ache, rebaixe a prioridade e encerre, sem reiniciar nada.

### M8 · Arquivos a fundo · 5 aulas · semanas 12 e 13

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [8.1 · FHS e onde cada coisa mora](aulas/8.1-fhs-e-onde-cada-coisa-mora.md) | 12 | `/etc`, `/var`, `/usr`, `/opt` e `/srv`; `which`, `type`, `whereis` e `locate` |
| [8.2 · find a fundo](aulas/8.2-find-a-fundo.md) | 12 | Por nome, tipo, dono, tamanho, data e permissão; `-exec` e `xargs` com segurança |
| [8.3 · Arquivamento avançado](aulas/8.3-arquivamento-avancado.md) | 12 | `tar` com seleção e exclusão, `cpio` e `dd`; imagem de disco e checksum |
| [8.4 · Links](aulas/8.4-links.md) | 13 | Inodes, links físicos e simbólicos; o que acontece quando o original some |
| [8.5 · Permissões avançadas](aulas/8.5-permissoes-avancadas.md) | 13 | SUID, SGID, sticky, `umask` e ACL; diagnosticar `Permission denied` passo a passo |

**Desafio do módulo:** três `Permission denied` com causas diferentes; achar cada uma.

### M9 · Armazenamento · 7 aulas · semanas 13 e 14

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [9.1 · Discos e layout](aulas/9.1-discos-e-layout.md) | 13 | MBR e GPT, nomes de dispositivo, planejar partições e LVM |
| [9.2 · Particionar](aulas/9.2-particionar.md) | 13 | `fdisk`, `gdisk` e `parted` em discos novos adicionados pelo Proxmox |
| [9.3 · Sistemas de arquivos](aulas/9.3-sistemas-de-arquivos.md) | 13 | ext4, XFS e VFAT: criar, rotular e comparar |
| [9.4 · Montar e persistir](aulas/9.4-montar-e-persistir.md) | 14 | `mount`, `/etc/fstab` por UUID e LABEL, `nofail`, units de montagem |
| [9.5 · Integridade e espaço](aulas/9.5-integridade-e-espaco.md) | 14 | `df`, `du`, `fsck`, `xfs_repair` e `tune2fs`; disco cheio de verdade |
| [9.6 · LVM](aulas/9.6-lvm.md) | 14 | PV, VG e LV: criar, estender, reduzir e remover |
| [9.7 · Crescer sem destruir](aulas/9.7-crescer-sem-destruir.md) | 14 | Nova partição, novo LV e swap sem perder dados; aumentar o disco no Proxmox até o sistema de arquivos |

**Desafio do módulo:** um `fstab` com erro impede o boot. Conserte pelo modo de emergência.

**Fechamento do bloco A (semana 14):** dia de incidente misturando M3 a M9 e revisão do caderno de erros.

### M10 · Usuários e acesso privilegiado · 4 aulas · semana 15

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [10.1 · Contas](aulas/10.1-contas.md) | 15 | `getent`, faixas de UID, contas de serviço, renomear e renumerar sem deixar arquivo órfão |
| [10.2 · Senhas e validade](aulas/10.2-senhas-e-validade.md) | 15 | PAM, `pwquality`, `faillock`, `login.defs` e `chage` |
| [10.3 · Grupos e trabalho em equipe](aulas/10.3-grupos-e-trabalho-em-equipe.md) | 15 | Grupo principal e suplementares, `gpasswd -A`, pasta com SGID, `umask` e ACL de grupo |
| [10.4 · sudo de verdade](aulas/10.4-sudo-de-verdade.md) | 15 | `Cmnd_Alias`, argumentos exatos, `sudo -l -U`, `sudoedit`, curingas perigosos e auditoria |

**Desafio do módulo:** uma equipe de três pessoas, senhas que vencem em 90 dias e uma pessoa que só pode reiniciar o nginx, tudo por um script que roda de novo sem estragar nada.

### M11 · Rede · 5 aulas · semanas 16 e 17

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [11.1 · TCP/IP para quem administra](aulas/11.1-tcp-ip-para-quem-administra.md) | 16 | IPv4 e IPv6, prefixos, rotas, portas, TCP, UDP e ICMP; `ip` e `ss`; testes locais e três quebras nas duas distros |
| [11.2 · NetworkManager e nmcli](aulas/11.2-networkmanager-e-nmcli.md) | 16 | Dispositivos e perfis, IPv4 fixo, IPv6, DNS salvo e efetivo, keyfiles e persistência; laboratório interno nas duas distros |
| [11.3 · Rede no Debian](aulas/11.3-rede-no-debian.md) | 16 | ifupdown, interfaces e inclusões; auto e allow-hotplug; comparação com NetworkManager e systemd-networkd; aplicação interna e três quebras nas duas distros |
| [11.4 · Nomes e resolução](aulas/11.4-nomes-e-resolucao.md) | 17 | hostnamectl, hosts, NSS e getent; origem de resolv.conf; resolução por fonte e resposta HTTP; três quebras nas duas distros |
| [11.5 · Diagnóstico de rede](aulas/11.5-diagnostico-de-rede.md) | 17 | `ping`, `tracepath`, `ss`, `dig`, `nc` e `tcpdump`; localizar falhas com evidências |

**Desafio do módulo:** IPv4 e IPv6 fixos na VM 201 após reboot, em interface de exercício; diagnosticar e recuperar um DNS quebrado.

## O que vem depois

As 130 aulas restantes já estão planejadas no [plano do curso](00-plano-do-curso.md):

| Módulos | Semanas | Foco | Fecha com |
| --- | --- | --- | --- |
| M11 a M15 | 16 a 21 | Rede, segurança do host, armazenamento em rede, agendamento, e-mail local, impressão, shell e interfaces gráficas | Dia de incidente |
| M16 | 21 e 22 | Rocky 10 e incidentes com relógio | Incidente cronometrado com reboot |
| M17 a M21 | 22 a 31 | Proxmox, Podman, serviços de rede, proxy, NethServer 8, Mail, WebTop, Nextcloud e NethVoice | Incidente combinado no NS8 |
| M22 a M34 | 31 a 48 | NethSecurity, Git, Ansible, monitoramento, logs, backup, desempenho, alta disponibilidade, hardening, cluster e troubleshooting | Dia inteiro de incidentes |
