# Aulas

Índice das **111 aulas publicadas**, do M0 ao M20. Cada título leva direto ao arquivo da aula; a coluna Semana segue o cronograma do [plano do curso](00-plano-do-curso.md).

**Cobertura atual:** curso completo, M0 a M20, em português e italiano.

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

## Fase 2 · Administrador · 41 aulas publicadas de 63 · semanas 7 a 18

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

### M12 · Segurança do host · 5 aulas · semanas 17 e 18

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [12.1 · SSH a fundo](aulas/12.1-ssh-a-fundo.md) | 17 | Chaves, agente, configuração do cliente, salto, túnel local e validação segura do servidor |
| [12.2 · Firewall](aulas/12.2-firewall.md) | 17 | firewalld, zonas, origem e porta; nftables em tabela própria, contadores e persistência |
| [12.3 · SELinux: modos e contextos](aulas/12.3-selinux-modos-e-contextos.md) | 18 | Modos, domínios, tipos, `semanage fcontext` e `restorecon`; distinguir contexto e permissão |
| [12.4 · SELinux: portas e booleanos](aulas/12.4-selinux-portas-e-booleanos.md) | 18 | Tipos de porta, booleanos persistentes, AVC e perfil AppArmor nomeado |
| [12.5 · Auditoria e criptografia](aulas/12.5-auditoria-e-criptografia.md) | 18 | Inventário de privilégios, sessões, limites e GPG; desafio integrado com nginx, SELinux e firewall |

**Desafio do módulo:** nginx em porta e diretório próprios, persistente, com SELinux enforcing na Rocky e firewall ativo, comprovado a partir da outra VM e após reboot.

### M13 · Armazenamento em rede · 3 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [13.1 · Servidor NFS](aulas/13.1-servidor-nfs.md) | 18 | Você prepara a VM 203 e exporta conteúdo NFS de leitura para as VMs 201 e 202 |
| [13.2 · Cliente NFS](aulas/13.2-cliente-nfs.md) | 19 | Você monta NFSv4.2 em Rocky e Debian, valida fstab e distingue indisponibilidade, ocupação e referência obsoleta |
| [13.3 · autofs](aulas/13.3-autofs.md) | 19 | Você configura um mapa indireto, diagnostica o acesso sob demanda e monta uma home NFS nas duas famílias |

### M14 · Agendamento, logs e hora · 5 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [14.1 · cron e at](aulas/14.1-cron-e-at.md) | 19 | Você instala agendas sem apagar trabalhos alheios e verifica a execução pelo resultado |
| [14.2 · Timers do systemd](aulas/14.2-timers-do-systemd.md) | 19 | Você cria um par de units, verifica falhas e comprova persistência |
| [14.3 · journald e rsyslog](aulas/14.3-journald-e-rsyslog.md) | 20 | Você filtra eventos, comprova journal persistente e gira um log próprio com estado separado |
| [14.4 · Hora certa](aulas/14.4-hora-certa.md) | 20 | Você interpreta chrony, compara fusos e mede uma fonte sem ajustar o relógio |
| [14.5 · E-mail local e impressão](aulas/14.5-email-local-e-impressao.md) | 20 | Você verifica entrega local, administra uma fila virtual e integra aviso de falha |

### M15 · Shell e ambiente · 5 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [15.1 · Ambiente do shell](aulas/15.1-ambiente-do-shell.md) | 20 | Você explica herança do ambiente e diagnostica procura de comando e arquivos de início |
| [15.2 · Scripts robustos](aulas/15.2-scripts-robustos.md) | 20 | Você escreve um script de leitura com contrato de entrada e falha verificável |
| [15.3 · Scripts de administração](aulas/15.3-scripts-de-administracao.md) | 20 | Você coleta dados dos dois hosts autorizados e preserva erros individuais |
| [15.4 · Interfaces gráficas](aulas/15.4-interfaces-graficas.md) | 21 | Você identifica as camadas da sessão gráfica e recupera a base do servidor |
| [15.5 · Idioma, teclado e fuso](aulas/15.5-idioma-teclado-e-fuso.md) | 21 | Você converte texto conhecido e produz um coletor com critérios explícitos |

### M16 · Semana de incidentes no Rocky 10 · 4 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [16.1 · Rocky 10: o que muda](aulas/16.1-rocky-10-o-que-muda.md) | 21 | Você valida a CPU completa, instala a VM 205 e confirma identidade, rede e acesso após o boot |
| [16.2 · Incidentes por área](aulas/16.2-incidentes-por-area.md) | 21 | Você isola falhas de caminho, leitura e arquivo compactado e comprova cada reparo após o boot |
| [16.3 · Incidente com relógio](aulas/16.3-incidente-com-relogio.md) | 22 | Você investiga uma cadeia de falhas nas duas VMs, registra tentativas e comprova a correção após o boot |
| [16.4 · Correção e reforço](aulas/16.4-correcao-e-reforco.md) | 22 | Você revisa evidências, fecha os critérios das duas VMs e escolhe reforços para as lacunas observadas |

### M17 · Proxmox na prática · 7 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [17.1 · Proxmox por dentro](aulas/17.1-proxmox-por-dentro.md) | 22 | Relacionar host, API, configuração, storage e tarefa |
| [17.2 · VM pela linha de comando](aulas/17.2-vm-pela-linha-de-comando.md) | 22 | Criar template 210 e clone completo 211 com rede, chave e console conferidos |
| [17.3 · Contêiner LXC](aulas/17.3-conteiner-lxc.md) | 23 | Você cria um CT não privilegiado, lê sua configuração e demonstra o kernel compartilhado |
| [17.4 · Storage: capacidade, crescimento e movimento](aulas/17.4-storage.md) | 23 | Criar um disco de dados, ampliar o ext4 e conferir um movimento entre storages |
| [17.5 · Rede: bridge, VLAN, bond e SDN](aulas/17.5-rede.md) | 23 | Criar uma bridge isolada, conectar duas interfaces e localizar a camada de uma falha |
| [17.6 · Backup e restauração com PBS](aulas/17.6-backup-e-restauracao.md) | 23 | Recuperar um arquivo e uma VM isolada a partir de uma cópia identificada |
| [17.7 · Migração e quorum](aulas/17.7-migracao-e-quorum.md) | 24 | Avaliar migração e quorum e provar recuperação da bancada |

### M18 · Podman · 5 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [18.1 · Contêiner não é VM](aulas/18.1-conteiner-nao-e-vm.md) | 24 | Inspecionar imagem, camadas e digest sem confundir contêiner com VM |
| [18.2 · Rodar e persistir](aulas/18.2-rodar-e-persistir.md) | 24 | Executar nginx rootless e demonstrar persistência fora da instância |
| [18.3 · Contêiner como serviço](aulas/18.3-conteiner-como-servico.md) | 25 | Criar e conferir um serviço rootless persistente após boot sem login do dono |
| [18.4 · Diagnosticar contêiner rootless](aulas/18.4-diagnosticar-conteiner-rootless.md) | 25 | Localizar a camada de três falhas sem ampliar privilégios |
| [18.5 · Construir imagens](aulas/18.5-construir-imagens.md) | 25 | Construir, testar, publicar localmente e provar o serviço após reboot sem sessão do dono |

### M19 · Serviços de rede · 9 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [19.1 · DNS autoritativo](aulas/19.1-dns-autoritativo.md) | 25 | construa a VM 204 e prove respostas A, MX e PTR na rede isolada. |
| [19.2 · DNS recursivo e diagnóstico](aulas/19.2-dns-recursivo-e-diagnostico.md) | 25 | distinga autoridade, recursão e cache sem abrir um resolvedor para qualquer origem. |
| [19.3 · DHCP](aulas/19.3-dhcp.md) | 25 | entregue concessões Kea somente na rede isolada e prove endereço, DNS e restauração do cliente. |
| [19.4 · Servidor web: nome, arquivo e resposta](aulas/19.4-servidor-web.md) | 26 | separar escuta, seleção de site e acesso ao arquivo antes de corrigir uma resposta HTTP. |
| [19.5 · TLS e proxy reverso: identidade antes do cadeado](aulas/19.5-tls-e-proxy-reverso.md) | 26 | validar nome, cadeia e validade, preservando a chave privada e a separação entre proxy e backend. |
| [19.6 · Samba: a ponte com o cliente Windows](aulas/19.6-samba-a-ponte-windows.md) | 26 | separar autenticação Samba, autorização do share e permissão Unix ao testar um arquivo compartilhado. |
| [19.7 · Postfix e correio local](aulas/19.7-postfix-e-correio-local.md) | 27 | Entregar correio local e provar a recusa de relay não autorizado |
| [19.8 · Dovecot e leitura por IMAPS](aulas/19.8-dovecot-e-imaps.md) | 27 | Ler por IMAPS a mensagem entregue pelo Postfix |
| [19.9 · Squid e desafio integrado](aulas/19.9-squid-e-desafio-integrado.md) | 27 | Controlar proxy explícito e encadear DHCP, DNS, HTTPS e IMAPS num cliente novo |

### M20 · NethServer 8 por dentro · 7 aulas

| Aula | Semana | O que você aprende |
| --- | --- | --- |
| [20.1 · Instalar em uma VM limpa](aulas/20.1-instalar-nethserver-8.md) | 27 | criar a VM 240, preparar seus pré-requisitos e abrir um cluster NS8 identificado. |
| [20.2 · Cluster, nó e módulo](aulas/20.2-cluster-no-e-modulo.md) | 27 | localizar uma instância real e distinguir controle, execução e identidade. |
| [20.3 · Um módulo por dentro](aulas/20.3-modulo-por-dentro.md) | 28 | encontrar dono, serviço, contêiner, dados e logs da mesma instância. |
| [20.4 · Proxy e certificados](aulas/20.4-proxy-e-certificados.md) | 28 | separar resolução, rota, identidade TLS e alcance do backend. |
| [20.5 · Domínios de usuário: identidade com fronteiras](aulas/20.5-dominios-de-usuario.md) | 28 | criar um domínio de teste e separar identidade, autenticação e permissão. |
| [20.6 · Backup e restauração: provar o retorno](aulas/20.6-backup-e-restauracao.md) | 28 | restaurar a Wiki de teste com conteúdo, identidade e destino conferidos. |
| [20.7 · Atualizar, mover e falhar com prova](aulas/20.7-atualizar-mover-e-falhar.md) | 29 | mover a Wiki entre nós e recuperar uma falha controlada sem prometer HA automática. |

## Situação

O curso está completo: 111 aulas, do M0 ao M20, em português e italiano.
