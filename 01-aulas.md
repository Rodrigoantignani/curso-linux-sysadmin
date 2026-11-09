# Aulas

Índice das **37 aulas publicadas**, de M0 a M6. Cada título leva direto ao arquivo da aula; a coluna Semana segue o cronograma do [plano do curso](00-plano-do-curso.md).

**Cobertura atual:** 37 de 188 aulas · semanas 1 a 11 de 48.

## Como estudar uma aula

1. Leia a **Ficha** e responda o **Aquecimento** de cabeça, sem consultar nada. Errar aqui faz parte: a pergunta prepara a memória para receber a resposta.
2. Leia o **Modelo mental** e o **Conceito em camadas**. Onde aparecer **Preveja**, escreva sua aposta no diário de bordo antes de rodar o comando.
3. Faça o **Lab guiado** com o snapshot de início tirado, digitando os comandos em vez de colar.
4. **Quebre e conserte.** Depois responda o **Quiz** sem olhar a aula e só então abra o **Gabarito** comentado, no fim do arquivo.
5. Marque o **Checklist de saída**, tire o snapshot de fim e abra o **DeepTutor** com os comandos da seção Com o DeepTutor.
6. Revise cada aula no DeepTutor com `!revisao` 1, 3, 7 e 21 dias depois de estudá-la.

## Fase 1 · Fundamentos · 20 aulas · semanas 1 a 6

Meta da fase: usar o terminal com segurança e entender o que cada comando faz por baixo, nas duas distros. A fase fecha com o Linux Essentials 010-200.

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

**Fechamento da fase (semana 6):** revisão espaçada de M0 a M2, dois simulados de 40 questões em 60 minutos e a prova **Linux Essentials 010-200**.

## Fase 2 · Administrador · 17 aulas publicadas de 63 · semanas 7 a 11

Meta da fase: administrar sozinho um servidor Linux de ponta a ponta, nas duas famílias, com tudo sobrevivendo ao reboot. Todo lab termina com reboot e verificação, como na prova da Red Hat.

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

## O que vem depois

As 151 aulas restantes já estão planejadas no [plano do curso](00-plano-do-curso.md):

| Módulos | Semanas | Foco | Fecha com |
| --- | --- | --- | --- |
| M7 a M9 | 11 a 14 | Processos e desempenho, arquivos a fundo e armazenamento | Dia de incidente |
| M10 a M15 | 15 a 21 | Usuários e acesso privilegiado, rede, segurança do host, armazenamento em rede, agendamento, e-mail local, impressão, shell e interfaces gráficas | Dia de incidente |
| M16 | 21 e 22 | Rocky 10 e incidentes com relógio | Incidente cronometrado com reboot |
| M17 a M21 | 22 a 31 | Proxmox, Podman, serviços de rede, proxy, NethServer 8, Mail, WebTop, Nextcloud e NethVoice | Incidente combinado no NS8 |
| M22 a M34 | 31 a 48 | NethSecurity, Git, Ansible, monitoramento, logs, backup, desempenho, alta disponibilidade, hardening, cluster e troubleshooting | Dia inteiro de incidentes |
