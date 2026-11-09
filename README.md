# Curso Linux Sysadmin

Curso em português (PT-BR) para sair do zero e trabalhar com fluência em Linux, com laboratórios práticos em Proxmox VE. As duas VMs do curso rodam **Rocky Linux 9** (a `rocky-lab`, 201) e **Debian 13** (a `debian-lab`, 202), para que você aprenda o mesmo conceito nas duas famílias. O curso cobre tudo o que um sysadmin usa e chega a Proxmox, NethServer 8 e NethSecurity. As provas LPI e Red Hat servem só como lista de assuntos.

O material foi escrito para ser estudado com as VMs ligadas: cada aula parte de um case real, e cada conceito termina em um comando que você digita, quebra e conserta.

## Situação do curso

**37 de 188 aulas publicadas**, de M0 a M6, cobrindo as semanas 1 a 11 do cronograma de 48 semanas.

| Fase | Módulos publicados | Aulas | Semanas | Fecha com |
| --- | --- | --- | --- | --- |
| 1 · Fundamentos | M0 Laboratório · M1 Linha de comando · M2 Sistema, usuários e permissões | 20 | 1–6 | Dia de incidente (semana 6) |
| 2 · Administrador | M3 Texto e editor · M4 Boot e systemd · M5 Hardware, kernel e virtualização · M6 Software | 17 | 7–11 | Incidente com relógio no Rocky 10 e no Debian 13 (semana 22) |

O restante da Fase 2 (M7 a M16) e as fases 3 e 4 estão detalhados no [plano do curso](00-plano-do-curso.md).

## Por onde começar

1. Leia o [plano do curso](00-plano-do-curso.md): as quatro fases, os critérios de fluência e o cronograma.
2. Monte o laboratório na [Aula 0.1 · Montar o laboratório](aulas/0.1-montar-o-laboratorio.md).
3. Proteja o acesso na [Aula 0.2 · Acesso e proteção](aulas/0.2-acesso-e-protecao.md).
4. Siga o [índice de aulas](01-aulas.md), na ordem dos módulos.

## Aulas publicadas

### M0 · Laboratório · 2 aulas · semana 1

- [Aula 0.1 · Montar o laboratório](aulas/0.1-montar-o-laboratorio.md)
- [Aula 0.2 · Acesso e proteção](aulas/0.2-acesso-e-protecao.md)

### M1 · Linha de comando · 10 aulas · semanas 1 a 3

- [Aula 1.1 · O que é Linux](aulas/1.1-o-que-e-linux.md)
- [Aula 1.2 · O shell e a ajuda](aulas/1.2-o-shell-e-a-ajuda.md)
- [Aula 1.3 · Caminhos e navegação](aulas/1.3-caminhos-e-navegacao.md)
- [Aula 1.4 · Criar, copiar, mover e apagar](aulas/1.4-criar-copiar-mover-e-apagar.md)
- [Aula 1.5 · Ler e procurar texto](aulas/1.5-ler-e-procurar-texto.md)
- [Aula 1.6 · Redirecionamentos e pipes](aulas/1.6-redirecionamentos-e-pipes.md)
- [Aula 1.7 · Arquivar e compactar](aulas/1.7-arquivar-e-compactar.md)
- [Aula 1.8 · Primeiro script](aulas/1.8-primeiro-script.md)
- [Aula 1.9 · Decidir e repetir](aulas/1.9-decidir-e-repetir.md)
- [Aula 1.10 · Software livre na prática](aulas/1.10-software-livre-na-pratica.md)

### M2 · Sistema, usuários e permissões · 8 aulas · semanas 4 e 5

- [Aula 2.1 · Instalação e provisionamento](aulas/2.1-instalacao-e-provisionamento.md)
- [Aula 2.2 · Hardware e dispositivos](aulas/2.2-hardware-e-dispositivos.md)
- [Aula 2.3 · Processos e logs](aulas/2.3-processos-e-logs.md)
- [Aula 2.4 · Rede no dia a dia](aulas/2.4-rede-no-dia-a-dia.md)
- [Aula 2.5 · Acesso remoto e privilégios](aulas/2.5-acesso-remoto-e-privilegios.md)
- [Aula 2.6 · Usuários e grupos](aulas/2.6-usuarios-e-grupos.md)
- [Aula 2.7 · Permissões e dono](aulas/2.7-permissoes-e-dono.md)
- [Aula 2.8 · Diretórios e arquivos especiais](aulas/2.8-diretorios-e-arquivos-especiais.md)

**Semana 6:** revisão de M0 a M2 e um dia de incidente nas duas VMs, sem consulta.

### M3 · Texto e editor · 5 aulas · semanas 7 e 8

- [Aula 3.1 · Fluxos a fundo](aulas/3.1-fluxos-a-fundo.md)
- [Aula 3.2 · Filtros de texto](aulas/3.2-filtros-de-texto.md)
- [Aula 3.3 · Regex e grep](aulas/3.3-regex-e-grep.md)
- [Aula 3.4 · sed e awk](aulas/3.4-sed-e-awk.md)
- [Aula 3.5 · vi e vim de verdade](aulas/3.5-vi-e-vim-de-verdade.md)

### M4 · Boot e systemd · 4 aulas · semanas 8 e 9

- [Aula 4.1 · Como o Linux liga](aulas/4.1-como-o-linux-liga.md)
- [Aula 4.2 · systemd: serviços e units](aulas/4.2-systemd-servicos-e-units.md)
- [Aula 4.3 · Targets, desligar e reiniciar](aulas/4.3-targets-desligar-e-reiniciar.md)
- [Aula 4.4 · GRUB e acesso de emergência](aulas/4.4-grub-e-acesso-de-emergencia.md)

### M5 · Hardware, kernel e virtualização · 3 aulas · semana 9

- [Aula 5.1 · Hardware pelo kernel](aulas/5.1-hardware-pelo-kernel.md)
- [Aula 5.2 · Módulos e parâmetros](aulas/5.2-modulos-e-parametros.md)
- [Aula 5.3 · Linux como convidado](aulas/5.3-linux-como-convidado.md)

### M6 · Software · 5 aulas · semanas 10 e 11

- [Aula 6.1 · Pacotes no Debian](aulas/6.1-pacotes-no-debian.md)
- [Aula 6.2 · Pacotes na Rocky](aulas/6.2-pacotes-na-rocky.md)
- [Aula 6.3 · Repositórios](aulas/6.3-repositorios.md)
- [Aula 6.4 · Flatpak](aulas/6.4-flatpak.md)
- [Aula 6.5 · Bibliotecas compartilhadas](aulas/6.5-bibliotecas-compartilhadas.md)

## Tradução (PT/IT)

As 37 aulas publicadas também existem em **italiano**: o Markdown fica em `aulas-it/` e as páginas em `html/*.it.html` (índice em `html/index.it.html`). No cabeçalho de cada página há um seletor **PT / IT** que alterna entre as duas versões. Os comandos Linux continuam em inglês nas duas línguas.

- As aulas foram traduzidas com o opencode e conferidas por `tools/validar-traducao.py`.
- Imagens italianas geradas até a aula **2.2** (arquivos `img/*.it.jpg`) já estão integradas; as demais aulas usam temporariamente as imagens originais.
- Os SVGs/diagramas ainda estão em português e podem ser traduzidos depois (ex.: Google Flow).

## Como cada aula funciona

Todas as aulas seguem o mesmo roteiro, para você criar o hábito e medir o próprio progresso:

1. **Aquecimento** · três perguntas das aulas anteriores, respondidas de memória.
2. **Modelo mental** · uma imagem que explica o assunto antes dos comandos.
3. **Conceito em camadas** · o essencial para o trabalho e para a emergência, depois o aprofundamento.
4. **Lab guiado** · o mesmo procedimento na `rocky-lab` e na `debian-lab`, com snapshot no início.
5. **Quebre e conserte** · um erro provocado de propósito, para aprender o diagnóstico.
6. **Quiz, gabarito e checklist** · a prova de que você aprendeu, e o snapshot de fim.

As aulas a partir da 4.1 seguem o **formato núcleo**: o essencial para resolver sem internet e sem consulta, com uma seção final de tópicos para aprofundar no DeepTutor.

## As imagens

- `img/` guarda **32 infográficos gerados no NotebookLM** e revisados comando por comando, com nomes que dizem a que aula pertencem (por exemplo, `1.2-escada-da-ajuda.jpg`).
- Os **diagramas em SVG** são editáveis e substituem os antigos placeholders: ficha da VM 201, chaves do SSH, famílias Linux e a ordem de busca do bash.
- O [mapa das imagens](img/README.md) lista cada arquivo, a aula em que aparece e o que ele mostra.

## Requisitos do laboratório

- Proxmox VE, em nó único com storage local ou em cluster com Ceph.
- As ISOs do Rocky Linux 9 e do Debian 13.
- Windows 10 ou 11 com o cliente OpenSSH, para as aulas de acesso remoto.

## Estrutura do repositório

```text
.
├── 00-plano-do-curso.md   plano completo: 4 fases, 188 aulas, 48 semanas
├── 01-aulas.md            índice das aulas publicadas, com semana e conteúdo
├── README.md              este arquivo
├── aulas/                 uma aula por arquivo Markdown
├── aulas-it/              as mesmas aulas em italiano
├── html/                  páginas geradas a partir das aulas (PT e IT)
├── tools/                 scripts que validam a tradução e geram o HTML
└── img/                   infográficos do NotebookLM e diagramas SVG
```
