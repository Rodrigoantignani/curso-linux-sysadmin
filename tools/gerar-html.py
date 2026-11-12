#!/usr/bin/env python3
"""Gera o site do curso em html/: português (padrão) com opção em italiano.

Fontes:
  aulas/*.md      aulas em português
  aulas-it/*.md   tradução italiana, com o mesmo nome de arquivo

Uma lição sem tradução em aulas-it/ mantém o .it.html que já existir.
Uso: python tools/gerar-html.py
"""
import html
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
AULAS_PT = ROOT / "aulas"
AULAS_IT = ROOT / "aulas-it"
SAIDA = ROOT / "html"
GITHUB = "https://github.com/Rodrigoantignani/curso-linux-sysadmin/blob/master/"

# (código, nome PT, nome IT, [(arquivo, título PT, título IT), ...])
CATALOGO = [
    ("M0", "Laboratório", "Laboratorio", [
        ("0.1-montar-o-laboratorio", "Montar o laboratório", "Allestire il laboratorio"),
        ("0.2-acesso-e-protecao", "Acesso e proteção", "Accesso e protezione"),
    ]),
    ("M1", "Linha de comando", "Riga di comando", [
        ("1.1-o-que-e-linux", "O que é Linux", "Che cos'è Linux"),
        ("1.2-o-shell-e-a-ajuda", "O shell e a ajuda", "La shell e la guida"),
        ("1.3-caminhos-e-navegacao", "Caminhos e navegação", "Percorsi e navigazione"),
        ("1.4-criar-copiar-mover-e-apagar", "Criar, copiar, mover e apagar", "Creare, copiare, spostare ed eliminare"),
        ("1.5-ler-e-procurar-texto", "Ler e procurar texto", "Leggere e cercare testo"),
        ("1.6-redirecionamentos-e-pipes", "Redirecionamentos e pipes", "Reindirizzamenti e pipe"),
        ("1.7-arquivar-e-compactar", "Arquivar e compactar", "Archiviare e comprimere"),
        ("1.8-primeiro-script", "Primeiro script", "Primo script"),
        ("1.9-decidir-e-repetir", "Decidir e repetir", "Decidere e ripetere"),
        ("1.10-software-livre-na-pratica", "Software livre na prática", "Il software libero in pratica"),
    ]),
    ("M2", "Sistema, usuários e permissões", "Sistema, utenti e permessi", [
        ("2.1-instalacao-e-provisionamento", "Instalação e provisionamento", "Installazione e provisioning"),
        ("2.2-hardware-e-dispositivos", "Hardware e dispositivos", "Hardware e dispositivi"),
        ("2.3-processos-e-logs", "Processos e logs", "Processi e log"),
        ("2.4-rede-no-dia-a-dia", "Rede no dia a dia", "La rete di tutti i giorni"),
        ("2.5-acesso-remoto-e-privilegios", "Acesso remoto e privilégios", "Accesso remoto e privilegi"),
        ("2.6-usuarios-e-grupos", "Usuários e grupos", "Utenti e gruppi"),
        ("2.7-permissoes-e-dono", "Permissões e dono", "Permessi e proprietario"),
        ("2.8-diretorios-e-arquivos-especiais", "Diretórios e arquivos especiais", "Directory e file speciali"),
    ]),
    ("M3", "Texto e editor", "Testo ed editor", [
        ("3.1-fluxos-a-fundo", "Fluxos a fundo", "I flussi in profondità"),
        ("3.2-filtros-de-texto", "Filtros de texto", "Filtri di testo"),
        ("3.3-regex-e-grep", "Regex e grep", "Regex e grep"),
        ("3.4-sed-e-awk", "sed e awk", "sed e awk"),
        ("3.5-vi-e-vim-de-verdade", "vi e vim de verdade", "vi e vim sul serio"),
    ]),
    ("M4", "systemd e boot", "systemd e boot", [
        ("4.1-como-o-linux-liga", "Como o Linux liga", "Come si avvia Linux"),
        ("4.2-systemd-servicos-e-units", "systemd: serviços e units", "systemd: servizi e unit"),
        ("4.3-targets-desligar-e-reiniciar", "Targets: desligar e reiniciar", "Target: spegnere e riavviare"),
        ("4.4-grub-e-acesso-de-emergencia", "GRUB e acesso de emergência", "GRUB e accesso di emergenza"),
    ]),
    ("M5", "Kernel, módulos e VM", "Kernel, moduli e VM", [
        ("5.1-hardware-pelo-kernel", "Hardware pelo kernel", "L'hardware visto dal kernel"),
        ("5.2-modulos-e-parametros", "Módulos e parâmetros", "Moduli e parametri"),
        ("5.3-linux-como-convidado", "Linux como convidado", "Linux come guest"),
    ]),
    ("M6", "Pacotes e repositórios", "Pacchetti e repository", [
        ("6.1-pacotes-no-debian", "Pacotes no Debian", "Pacchetti su Debian"),
        ("6.2-pacotes-na-rocky", "Pacotes na Rocky", "Pacchetti su Rocky"),
        ("6.3-repositorios", "Repositórios", "Repository"),
        ("6.4-flatpak", "Flatpak", "Flatpak"),
        ("6.5-bibliotecas-compartilhadas", "Bibliotecas compartilhadas", "Librerie condivise"),
    ]),
    ("M7", "Processos e desempenho", "Processi e prestazioni", [
        ("7.1-processos-e-sinais", "Processos e sinais", "Processi e segnali"),
        ("7.2-jobs-e-sessoes", "Jobs e sessões", "Job e sessioni"),
        ("7.3-prioridade-e-perfis", "Prioridade e perfis", "Priorità e profili"),
    ]),
    ("M8", "Arquivos a fundo", "File a fondo", [
        ("8.1-fhs-e-onde-cada-coisa-mora", "FHS e onde cada coisa mora", "FHS e dove sta ogni cosa"),
        ("8.2-find-a-fundo", "find a fundo", "find a fondo"),
        ("8.3-arquivamento-avancado", "Arquivamento avançado", "Archiviazione avanzata"),
        ("8.4-links", "Links", "Link"),
        ("8.5-permissoes-avancadas", "Permissões avançadas", "Permessi avanzati"),
    ]),
    ("M9", "Armazenamento", "Storage", [
        ("9.1-discos-e-layout", "Discos e layout", "Dischi e layout"),
        ("9.2-particionar", "Particionar", "Partizionare"),
        ("9.3-sistemas-de-arquivos", "Sistemas de arquivos", "File system"),
        ("9.4-montar-e-persistir", "Montar e persistir", "Montare e rendere persistente"),
        ("9.5-integridade-e-espaco", "Integridade e espaço", "Integrità e spazio"),
        ("9.6-lvm", "LVM", "LVM"),
        ("9.7-crescer-sem-destruir", "Crescer sem destruir", "Crescere senza distruggere"),
    ]),
    ("M10", "Usuários e acesso privilegiado", "Utenti e accesso privilegiato", [
        ("10.1-contas", "Contas", "Account"),
        ("10.2-senhas-e-validade", "Senhas e validade", "Password e scadenza"),
        ("10.3-grupos-e-trabalho-em-equipe", "Grupos e trabalho em equipe", "Gruppi e lavoro di squadra"),
        ("10.4-sudo-de-verdade", "sudo de verdade", "sudo sul serio"),
    ]),
    ("M11", "Rede", "Rete", [
        ("11.1-tcp-ip-para-quem-administra", "TCP/IP para quem administra", "TCP/IP per chi amministra"),
        ("11.2-networkmanager-e-nmcli", "NetworkManager e nmcli", "NetworkManager e nmcli"),
        ("11.3-rede-no-debian", "Rede no Debian", "Rete su Debian"),
    ]),
]

TEXTOS = {
    "pt": {
        "lang": "pt-BR", "curso": "Curso Linux Sysadmin", "indice": "Índice",
        "idioma": "Idioma", "aulas": "Aulas", "aula": "Aula", "anterior": "Anterior",
        "proxima": "Próxima", "pular": "Pular para o conteúdo",
        "meta": "{autor} · {n} aulas · {img} imagens",
        "stats": "<strong>{n} aulas publicadas</strong> · M0 a M9 · Semanas 1 a 14 de 48 · <strong>{img} imagens</strong>",
        "rodape": "Gerado a partir do Markdown do curso · Imagens em <code translate=\"no\">img/</code>",
    },
    "it": {
        "lang": "it", "curso": "Corso Linux Sysadmin", "indice": "Indice",
        "idioma": "Lingua", "aulas": "Lezioni", "aula": "Lezione", "anterior": "Precedente",
        "proxima": "Successiva", "pular": "Vai al contenuto",
        "meta": "{autor} · {n} lezioni · {img} immagini",
        "stats": "<strong>{n} lezioni pubblicate</strong> · Da M0 a M9 · Settimane da 1 a 14 di 48 · <strong>{img} immagini</strong>",
        "rodape": "Generato dal Markdown del corso · Immagini in <code translate=\"no\">img/</code>",
    },
}

CSS = """
:root{color-scheme:light dark;--bg:#f6f1e7;--card:#fffdf8;--ink:#201c16;--muted:#5e564a;--accent:#9a3412;--accent-2:#1f5f4a;--tint:#efe6d4;--line:#ddd2bc;--code:#f1eadb;--shadow:0 1px 2px rgba(60,40,10,.08);--serif:Georgia,"Iowan Old Style","Palatino Linotype",Palatino,serif;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:"Cascadia Code",Consolas,"DejaVu Sans Mono",monospace}
@media (prefers-color-scheme:dark){:root{--bg:#16130f;--card:#201b15;--ink:#f1eadb;--muted:#b9ad98;--accent:#f0a070;--accent-2:#7fd0b0;--tint:#2a231a;--line:#3d3427;--code:#191510;--shadow:none}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-padding-top:5.5rem}
body{margin:0;background:var(--bg);color:var(--ink);font:1rem/1.6 var(--sans)}
a{color:inherit}
:focus-visible{outline:3px solid var(--accent-2);outline-offset:2px;border-radius:4px}
.pular{position:absolute;left:-999px;top:0;background:var(--card);padding:.5rem 1rem;z-index:20}
.pular:focus{left:.5rem;top:.5rem}
.wrap{width:100%;max-width:84rem;margin:0 auto;padding-inline:max(1rem,env(safe-area-inset-left))}
.top{background:var(--card);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10;border-top:6px solid var(--accent)}
.top-in{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding-block:.6rem}
.titles{min-width:0}
.marca{margin:0;font:700 clamp(1.15rem,1rem + 1vw,1.6rem)/1.15 var(--serif);letter-spacing:-.01em}
.marca a{text-decoration:none}
.marca a:hover{color:var(--accent)}
.meta{margin:.1rem 0 0;color:var(--muted);font-size:.85rem}
.acoes{display:flex;align-items:center;gap:.9rem;flex:none}
.acoes>a{font-size:.9rem;font-weight:600;color:var(--muted);text-decoration:none}
.acoes>a:hover{color:var(--accent);text-decoration:underline}
.idioma{display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:var(--tint)}
.idioma>*{padding:.35rem .9rem;font-size:.8rem;font-weight:700;letter-spacing:.06em;text-decoration:none;color:var(--muted);min-width:2.75rem;text-align:center}
.idioma a:hover{color:var(--accent);text-decoration:underline}
.idioma span{background:var(--accent);color:#fff}
@media (prefers-color-scheme:dark){.idioma span{color:#16130f}}
code{font-family:var(--mono);font-size:.9em;background:var(--tint);padding:.1rem .35rem;border-radius:4px;overflow-wrap:anywhere}
/* índice */
.capa{max-width:70rem;padding-block:2rem 3rem}
.stats{border-left:4px solid var(--accent-2);background:var(--card);border-radius:0 10px 10px 0;padding:1rem 1.25rem;margin:0 0 2.5rem;box-shadow:var(--shadow);color:var(--muted)}
.stats strong{color:var(--ink)}
.modulo{display:grid;grid-template-columns:15rem minmax(0,1fr);gap:1rem 2rem;padding:1.75rem 0;border-top:1px solid var(--line)}
.modulo h2{margin:0;font:700 1.25rem/1.25 var(--serif);align-self:start;position:sticky;top:6rem}
.mn{display:block;font:700 .8rem var(--mono);letter-spacing:.12em;color:var(--accent);margin-bottom:.25rem}
.sep{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.modulo ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:.75rem}
.modulo li{margin:0}
.modulo a{display:flex;gap:.45rem;align-items:baseline;height:100%;padding:.85rem 1rem;background:var(--card);border:1px solid var(--line);border-radius:10px;text-decoration:none;font-weight:600;line-height:1.35;box-shadow:var(--shadow);transition:border-color .15s,transform .15s}
.modulo a:hover{border-color:var(--accent);color:var(--accent)}
.num{font:700 .85rem var(--mono);color:var(--accent);white-space:nowrap}
/* aula */
.doc{display:grid;grid-template-columns:17rem minmax(0,1fr);gap:2.5rem;align-items:start;padding-block:2rem 3rem}
.lateral{position:sticky;top:5.5rem;max-height:calc(100vh - 6.5rem);overflow:auto;font-size:.875rem;padding-right:.5rem}
.lateral h2{margin:0 0 .25rem;font:700 .95rem var(--serif);color:var(--muted)}
.lateral h3{margin:1rem 0 .25rem;font:700 .75rem var(--mono);letter-spacing:.06em;color:var(--accent)}
.lateral ul{list-style:none;margin:0;padding:0}
.lateral a{display:flex;gap:.45rem;padding:.25rem .5rem;border-radius:6px;text-decoration:none;color:var(--muted);line-height:1.3}
.lateral a:hover{background:var(--tint);color:var(--ink)}
.lateral a[aria-current]{background:var(--tint);color:var(--ink);font-weight:700;box-shadow:inset 3px 0 0 var(--accent)}
.lateral .num{font-size:.75rem}
.aula{min-width:0;max-width:56rem;overflow-wrap:break-word;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:clamp(1.25rem,1rem + 2vw,2.75rem);box-shadow:var(--shadow)}
.aula h1{margin:0 0 1.5rem;font:700 clamp(1.75rem,1.4rem + 1.6vw,2.5rem)/1.15 var(--serif);letter-spacing:-.015em;color:var(--ink)}
.aula h2{margin:2.5rem 0 .75rem;padding-top:1.25rem;border-top:1px solid var(--line);font:700 1.5rem/1.25 var(--serif)}
.aula h3{margin:2rem 0 .5rem;font:700 1.15rem/1.3 var(--serif);color:var(--accent)}
.aula h4,.aula h5,.aula h6{margin:1.5rem 0 .5rem;font-size:1rem}
.aula p,.aula ul,.aula ol{margin:1rem 0}
.aula ul,.aula ol{padding-left:1.5rem}
.aula li{margin:.35rem 0}
.aula li>ul,.aula li>ol{margin:.35rem 0}
.aula a{color:var(--accent);text-underline-offset:2px}
.aula hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
.tabela{overflow-x:auto;margin:1.25rem 0;border:1px solid var(--line);border-radius:10px}
.aula table{width:100%;border-collapse:collapse;font-size:.9rem}
.aula th,.aula td{padding:.55rem .75rem;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
.aula tr:last-child td{border-bottom:0}
.aula th{background:var(--tint);font-weight:700}
.aula pre{background:var(--code);border:1px solid var(--line);border-radius:10px;padding:.9rem 1rem;overflow-x:auto;font:.85rem/1.5 var(--mono);margin:1rem 0;tab-size:4}
.aula pre code{background:none;padding:0;font-size:inherit;overflow-wrap:normal}
.aula blockquote{margin:1.25rem 0;padding:.75rem 1.25rem;border-left:4px solid var(--accent-2);background:var(--tint);border-radius:0 10px 10px 0}
.aula blockquote>:first-child{margin-top:0}
.aula blockquote>:last-child{margin-bottom:0}
.aula figure{margin:1.75rem 0;text-align:center}
.aula figure img{display:block;margin:0 auto;max-width:100%;height:auto;border:1px solid var(--line);border-radius:10px;background:#fff}
.aula figcaption{margin-top:.5rem;color:var(--muted);font-size:.9rem;font-style:italic}
.paginas{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--line)}
.paginas a{display:block;padding:.75rem 1rem;border:1px solid var(--line);border-radius:10px;text-decoration:none;color:var(--ink);font-weight:600;line-height:1.3}
.paginas a:hover{border-color:var(--accent);color:var(--accent)}
.paginas small{display:block;color:var(--muted);font-weight:400}
.paginas .prox{grid-column:2;text-align:right}
footer{border-top:1px solid var(--line);padding-block:1.5rem;color:var(--muted);font-size:.85rem;text-align:center}
@media (hover:hover) and (prefers-reduced-motion:no-preference){.modulo a:hover{transform:translateY(-2px)}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media (max-width:980px){.doc{grid-template-columns:minmax(0,1fr);padding-top:1rem}.lateral{position:static;max-height:none;order:2}.aula{max-width:none}}
@media (max-width:860px){.modulo{grid-template-columns:minmax(0,1fr)}.modulo h2{position:static}.mn{display:inline;margin-right:.5rem}}
@media (max-width:420px){.meta{display:none}.top-in{gap:.5rem}.acoes{gap:.6rem}.capa{padding-top:1.25rem}.paginas{grid-template-columns:minmax(0,1fr)}.paginas .prox{grid-column:1}}
@media print{.top,.lateral,.paginas{display:none}.aula{border:0;box-shadow:none;padding:0;max-width:none}.doc{display:block}}
"""

FENCE = re.compile(r"^(`{3,}|~{3,})\s*([\w+-]*)\s*$")
TITULO = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
IMAGEM = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)\s*$")
LEGENDA = re.compile(r"^\*(?!\*)(.+)\*\s*$")
LINHA_H = re.compile(r"^\s*(-{3,}|\*{3,})\s*$")
ITEM = re.compile(r"^( *)([-*+]|\d+[.)])\s+(.*)$")
SEPARADOR = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
NAVEGACAO = re.compile(r"\n-{3,}\s*\n+<!-- navegacao -->.*\Z", re.S)
TAG_CODE = '<code translate="no">'


def esc(texto):
    return html.escape(texto, quote=False)


def recuo(linha):
    return len(linha) - len(linha.lstrip(" "))


def vazia(linha):
    return not linha.strip()


def ancora(texto, usadas):
    sem_acento = unicodedata.normalize("NFKD", re.sub(r"[`*]", "", texto)).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-") or "secao"
    nome, n = base, 2
    while nome in usadas:
        nome, n = f"{base}-{n}", n + 1
    usadas.add(nome)
    return nome


def celulas(linha):
    s = linha.strip()
    s = s[1:] if s.startswith("|") else s
    s = s[:-1] if s.endswith("|") and not s.endswith("\\|") else s
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", s)]


class Conversor:
    """Markdown do curso para HTML, com links ajustados ao idioma."""

    def __init__(self, idioma, existe_it):
        self.idioma = idioma
        self.existe_it = existe_it
        self.usadas = set()

    def href(self, url):
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            return url
        caminho, _, frag = url.partition("#")
        frag = f"#{frag}" if frag else ""
        if not caminho.endswith(".md"):
            return url
        nome = caminho.rsplit("/", 1)[-1]
        if nome == "01-aulas.md":
            return ("index.it.html" if self.idioma == "it" else "index.html") + frag
        if caminho.startswith("../"):
            return GITHUB + caminho[3:] + frag
        slug = nome[:-3]
        if self.idioma == "it" and slug in self.existe_it:
            return f"{slug}.it.html{frag}"
        return f"{slug}.html{frag}"

    def inline(self, texto):
        guardados = []

        def guarda(trecho):
            guardados.append(trecho)
            return f"\x00{len(guardados) - 1}\x00"

        def codigo(m):
            c = m.group(2).replace("\n", " ")
            if len(c) > 2 and c[0] == " " and c[-1] == " " and c.strip():
                c = c[1:-1]
            return guarda(TAG_CODE + esc(c) + "</code>")

        def link(m):
            alvo = html.escape(self.href(m.group(2)), quote=True)
            return guarda(f'<a href="{alvo}">') + m.group(1) + guarda("</a>")

        t = re.sub(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", codigo, texto, flags=re.S)
        t = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~])", lambda m: guarda(esc(m.group(1))), t)
        t = esc(t)
        t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
        t = re.sub(r"\*\*\*(?=\S)(.+?)(?<=\S)\*\*\*", r"<strong><em>\1</em></strong>", t, flags=re.S)
        t = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", t, flags=re.S)
        t = re.sub(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", r"<em>\1</em>", t, flags=re.S)
        return re.sub(r"\x00(\d+)\x00", lambda m: guardados[int(m.group(1))], t)

    def inicia_bloco(self, linhas, i):
        l = linhas[i]
        if FENCE.match(l) or TITULO.match(l) or LINHA_H.match(l) or IMAGEM.match(l):
            return True
        if l.startswith(">") or l.startswith("<!--") or ITEM.match(l):
            return True
        return self.inicia_tabela(linhas, i)

    @staticmethod
    def inicia_tabela(linhas, i):
        return "|" in linhas[i] and i + 1 < len(linhas) and bool(SEPARADOR.match(linhas[i + 1])) and "-" in linhas[i + 1]

    def lista(self, linhas, i):
        n = len(linhas)
        m0 = ITEM.match(linhas[i])
        base = len(m0.group(1))
        ordenada = m0.group(2)[0].isdigit()
        itens = []
        while i < n:
            m = ITEM.match(linhas[i])
            if not m or len(m.group(1)) != base or m.group(2)[0].isdigit() != ordenada:
                break
            coluna = m.start(3)
            corpo = [m.group(3)]
            solta = False
            i += 1
            while i < n:
                l = linhas[i]
                if vazia(l):
                    j = i
                    while j < n and vazia(linhas[j]):
                        j += 1
                    if j < n and recuo(linhas[j]) >= base + 2:
                        corpo.append("")
                        solta = True
                        i += 1
                        continue
                    break
                if recuo(l) >= base + 2:
                    corpo.append(l[min(recuo(l), coluna):])
                elif self.inicia_bloco(linhas, i):
                    break
                else:
                    corpo.append(l.strip())
                i += 1
            blocos = self.blocos(corpo)
            if blocos and blocos[0].startswith("<p>") and not solta:
                blocos[0] = blocos[0][3:-4]
            itens.append("<li>" + "\n".join(blocos) + "</li>")
            j = i
            while j < n and vazia(linhas[j]):
                j += 1
            if j < n and j != i:
                seguinte = ITEM.match(linhas[j])
                if seguinte and len(seguinte.group(1)) == base and seguinte.group(2)[0].isdigit() == ordenada:
                    i = j
        tag = "ol" if ordenada else "ul"
        inicio = ""
        if ordenada:
            numero = int(re.match(r"\d+", m0.group(2)).group())
            inicio = f' start="{numero}"' if numero != 1 else ""
        return f"<{tag}{inicio}>" + "\n".join(itens) + f"</{tag}>", i

    def tabela(self, linhas, i):
        n = len(linhas)
        cab = celulas(linhas[i])
        i += 2
        corpo = []
        while i < n and "|" in linhas[i] and not vazia(linhas[i]):
            cs = celulas(linhas[i])
            cs += [""] * (len(cab) - len(cs))
            corpo.append("<tr>" + "".join(f"<td>{self.inline(c)}</td>" for c in cs) + "</tr>")
            i += 1
        ths = "".join(f'<th scope="col">{self.inline(c)}</th>' for c in cab)
        return f'<div class="tabela"><table><thead><tr>{ths}</tr></thead><tbody>' + "".join(corpo) + "</tbody></table></div>", i

    def blocos(self, linhas):
        saida = []
        i, n = 0, len(linhas)
        while i < n:
            l = linhas[i]
            if vazia(l):
                i += 1
                continue
            m = FENCE.match(l)
            if m:
                cerca, lang = m.group(1), m.group(2)
                i += 1
                buf = []
                while i < n and linhas[i].strip() != cerca:
                    buf.append(linhas[i])
                    i += 1
                i += 1
                classe = f' class="lang-{lang}"' if lang else ""
                saida.append(f'<pre translate="no"><code{classe}>{esc(chr(10).join(buf))}</code></pre>')
                continue
            if l.startswith("<!--"):
                while i < n and "-->" not in linhas[i]:
                    i += 1
                i += 1
                continue
            m = TITULO.match(l)
            if m:
                nivel = len(m.group(1))
                saida.append(f'<h{nivel} id="{ancora(m.group(2), self.usadas)}">{self.inline(m.group(2))}</h{nivel}>')
                i += 1
                continue
            if LINHA_H.match(l):
                saida.append("<hr>")
                i += 1
                continue
            m = IMAGEM.match(l)
            if m:
                alt, src = m.group(1), html.escape(m.group(2), quote=True)
                i += 1
                j = i
                if j < n and vazia(linhas[j]):
                    j += 1
                legenda = ""
                c = LEGENDA.match(linhas[j]) if j < n else None
                if c:
                    legenda = f"<figcaption>{self.inline(c.group(1))}</figcaption>"
                    i = j + 1
                saida.append(f'<figure><a href="{src}"><img src="{src}" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async"></a>{legenda}</figure>')
                continue
            if self.inicia_tabela(linhas, i):
                bloco, i = self.tabela(linhas, i)
                saida.append(bloco)
                continue
            if l.startswith(">"):
                buf = []
                while i < n and linhas[i].startswith(">"):
                    buf.append(re.sub(r"^> ?", "", linhas[i]))
                    i += 1
                saida.append("<blockquote>" + "\n".join(self.blocos(buf)) + "</blockquote>")
                continue
            if ITEM.match(l):
                bloco, i = self.lista(linhas, i)
                saida.append(bloco)
                continue
            buf = [l.strip()]
            i += 1
            while i < n and not vazia(linhas[i]) and not self.inicia_bloco(linhas, i):
                buf.append(linhas[i].strip())
                i += 1
            saida.append("<p>" + self.inline("\n".join(buf)) + "</p>")
        return saida


def ler_aula(caminho):
    """Devolve (título H1, linhas sem o H1 e sem o rodapé de navegação)."""
    texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
    texto = NAVEGACAO.sub("\n", texto)
    linhas = texto.split("\n")
    for i, l in enumerate(linhas):
        if l.startswith("# "):
            return l[2:].strip(), linhas[:i] + linhas[i + 1:]
    raise SystemExit(f"ERRO: {caminho.name} não tem título H1")


def rel(slug, idioma, existe_it):
    return f"{slug}.it.html" if idioma == "it" and slug in existe_it else f"{slug}.html"


def numero(slug):
    return slug.split("-", 1)[0]


def seletor(idioma, pt, it):
    if idioma == "pt":
        return f'<div class="idioma" role="group" aria-label="Idioma"><span aria-current="true">PT</span><a href="{it}" hreflang="it" lang="it">IT</a></div>'
    return f'<div class="idioma" role="group" aria-label="Lingua"><a href="{pt}" hreflang="pt-BR" lang="pt-BR">PT</a><span aria-current="true">IT</span></div>'


def documento(idioma, titulo, topo, corpo, alternativas):
    t = TEXTOS[idioma]
    links = "".join(f'<link rel="alternate" hreflang="{h}" href="{u}">' for h, u in alternativas)
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<title>{esc(titulo)}</title>
{links}
<style>{CSS}</style>
</head>
<body>
<a class="pular" href="#conteudo">{t['pular']}</a>
<header class="top"><div class="wrap top-in">{topo}</div></header>
{corpo}
<footer><div class="wrap">{t['rodape']}</div></footer>
</body>
</html>
"""


def lateral(idioma, atual, existe_it):
    t = TEXTOS[idioma]
    partes = [f'<aside class="lateral" aria-label="{t["aulas"]}"><h2>{t["aulas"]}</h2>']
    for cod, nome_pt, nome_it, aulas in CATALOGO:
        nome = nome_it if idioma == "it" else nome_pt
        partes.append(f"<h3>{cod} · {esc(nome)}</h3><ul>")
        for slug, tit_pt, tit_it in aulas:
            tit = tit_it if idioma == "it" else tit_pt
            marca = ' aria-current="page"' if slug == atual else ""
            partes.append(f'<li><a href="{rel(slug, idioma, existe_it)}"{marca}><span class="num">{numero(slug)}</span><span>{esc(tit)}</span></a></li>')
        partes.append("</ul>")
    partes.append("</aside>")
    return "".join(partes)


def pagina_aula(idioma, indice, fonte, existe_it, autor="Rodrigo Antignani"):
    t = TEXTOS[idioma]
    slug, tit_pt, tit_it = indice["aulas"][indice["i"]]
    titulo_h1, linhas = ler_aula(fonte)
    conv = Conversor(idioma, existe_it)
    corpo = "\n".join(conv.blocos(linhas))
    curto = tit_it if idioma == "it" else tit_pt

    def vizinho(k, rotulo, classe):
        if not 0 <= k < len(indice["aulas"]):
            return ""
        s, p, i = indice["aulas"][k]
        tit = i if idioma == "it" else p
        return f'<a class="{classe}" href="{rel(s, idioma, existe_it)}"><small>{rotulo}</small>{numero(s)} · {esc(tit)}</a>'

    paginas = vizinho(indice["i"] - 1, "← " + t["anterior"], "ant") + vizinho(indice["i"] + 1, t["proxima"] + " →", "prox")
    ind = "index.it.html" if idioma == "it" else "index.html"
    pt, it = f"{slug}.html", f"{slug}.it.html" if slug in existe_it else f"{slug}.html"
    topo = (
        f'<div class="titles"><p class="marca"><a href="{ind}">{t["curso"]}</a></p>'
        f'<p class="meta">{autor} · {t["aula"]} {numero(slug)}</p></div>'
        f'<div class="acoes"><a href="{ind}">{t["indice"]}</a>{seletor(idioma, pt, it)}</div>'
    )
    miolo = (
        f'<div class="wrap doc">{lateral(idioma, slug, existe_it)}'
        f'<main id="conteudo" class="aula"><article><h1>{conv.inline(titulo_h1)}</h1>\n{corpo}\n</article>'
        f'<nav class="paginas" aria-label="{t["aulas"]}">{paginas}</nav></main></div>'
    )
    return documento(idioma, f"{numero(slug)} · {curto} · {t['curso']}", topo, miolo, [("pt-BR", pt), ("it", it)])


def pagina_indice(idioma, total, imagens, existe_it, autor="Rodrigo Antignani"):
    t = TEXTOS[idioma]
    blocos = []
    for cod, nome_pt, nome_it, aulas in CATALOGO:
        nome = nome_it if idioma == "it" else nome_pt
        itens = "".join(
            f'<li><a href="{rel(s, idioma, existe_it)}"><span class="num">{numero(s)}</span><span>{esc(i if idioma == "it" else p)}</span></a></li>'
            for s, p, i in aulas
        )
        blocos.append(f'<section class="modulo"><h2><span class="mn">{cod}</span><span class="sep"> · </span>{esc(nome)}</h2><ul>{itens}</ul></section>')
    topo = (
        f'<div class="titles"><h1 class="marca">{t["curso"]}</h1>'
        f'<p class="meta">{t["meta"].format(autor=autor, n=total, img=imagens)}</p></div>'
        f'<div class="acoes">{seletor(idioma, "index.html", "index.it.html")}</div>'
    )
    miolo = (
        f'<main id="conteudo" class="wrap capa"><p class="stats">{t["stats"].format(n=total, img=imagens)}</p>'
        + "\n".join(blocos) + "</main>"
    )
    return documento(idioma, f"{t['curso']} · {t['indice']}", topo, miolo, [("pt-BR", "index.html"), ("it", "index.it.html")])


def main():
    SAIDA.mkdir(exist_ok=True)
    catalogadas = [a for _, _, _, aulas in CATALOGO for a in aulas]
    nomes = {a[0] for a in catalogadas}
    presentes = {p.stem for p in AULAS_PT.glob("*.md")}
    if nomes != presentes:
        raise SystemExit(f"ERRO: catálogo e aulas/ divergem: {sorted(nomes ^ presentes)}")

    traduzidas = {p.stem for p in AULAS_IT.glob("*.md")} if AULAS_IT.is_dir() else set()
    estranhas = traduzidas - nomes
    if estranhas:
        raise SystemExit(f"ERRO: aulas-it/ tem arquivos fora do catálogo: {sorted(estranhas)}")
    existe_it = traduzidas | {s for s in nomes if (SAIDA / f"{s}.it.html").exists()}

    imagens = set()
    for slug in nomes:
        imagens |= set(re.findall(r"\.\./img/([^)\s]+)", (AULAS_PT / f"{slug}.md").read_text(encoding="utf-8")))
    faltando = sorted(i for i in imagens if not (ROOT / "img" / i).exists())
    if faltando:
        raise SystemExit(f"ERRO: imagens citadas e inexistentes: {faltando}")

    grava = lambda nome, conteudo: (SAIDA / nome).write_text(conteudo, encoding="utf-8", newline="\n")
    n_it = 0
    for i, aula in enumerate(catalogadas):
        slug = aula[0]
        indice = {"aulas": catalogadas, "i": i}
        grava(f"{slug}.html", pagina_aula("pt", indice, AULAS_PT / f"{slug}.md", existe_it))
        if slug in traduzidas:
            grava(f"{slug}.it.html", pagina_aula("it", indice, AULAS_IT / f"{slug}.md", existe_it))
            n_it += 1
    grava("index.html", pagina_indice("pt", len(catalogadas), len(imagens), existe_it))
    grava("index.it.html", pagina_indice("it", len(catalogadas), len(imagens), existe_it))
    print(f"PT: {len(catalogadas)} aulas + índice | IT: {n_it} traduzidas de aulas-it/, {len(catalogadas) - n_it} pendentes + índice | {len(imagens)} imagens")


if __name__ == "__main__":
    sys.exit(main())
