# Curso Linux Sysadmin

Curso em português (PT-BR) para sair do zero e trabalhar com fluência em Linux, com laboratórios práticos em Proxmox VE. As duas VMs do curso rodam **Rocky Linux 9** (a `rocky-lab`, 201) e **Debian 13** (a `debian-lab`, 202), para que você aprenda o mesmo conceito nas duas famílias. O curso cobre tudo o que um sysadmin usa e chega a Proxmox, NethServer 8 e NethSecurity.

O material foi escrito para ser estudado com as VMs ligadas: cada aula parte de um case real, e cada conceito termina em um comando que você digita, quebra e conserta.

## Situação do curso

**111 aulas publicadas**, de M0 a M20, em português e italiano (`aulas-it/`). O índice completo, módulo por módulo, está em [01-aulas.md](01-aulas.md).

## Por onde começar

1. Leia o [plano do curso](00-plano-do-curso.md): as quatro fases, os critérios de fluência e o cronograma.
2. Monte o laboratório na [Aula 0.1 · Montar o laboratório](aulas/0.1-montar-o-laboratorio.md).
3. Proteja o acesso na [Aula 0.2 · Acesso e proteção](aulas/0.2-acesso-e-protecao.md).
4. Siga o [índice de aulas](01-aulas.md), na ordem dos módulos.

## Aulas publicadas

Todas as aulas, com semana e objetivo, estão no [índice de aulas](01-aulas.md).

## Tradução (PT/IT)

As 111 aulas também existem em **italiano**: o Markdown fica em `aulas-it/` e as páginas em `html/*.it.html` (índice em `html/index.it.html`). No cabeçalho de cada página há um seletor **PT / IT** que alterna entre as duas versões. Os comandos Linux continuam em inglês nas duas línguas.

- As aulas foram traduzidas com o opencode e conferidas por `tools/validar-traducao.py`.
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

- `img/` guarda **404 imagens** (infográficos do NotebookLM e diagramas) e revisados comando por comando, com nomes que dizem a que aula pertencem (por exemplo, `1.2-escada-da-ajuda.jpg`).
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
