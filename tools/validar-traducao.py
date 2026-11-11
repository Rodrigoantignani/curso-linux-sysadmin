#!/usr/bin/env python3
"""Confere aulas-it/*.md contra aulas/*.md, linha por linha.

Reprova se um comando, caminho, saída, imagem, link ou a estrutura mudar.
Comentários de código (# ...) podem ser traduzidos.

Uso:
  python tools/validar-traducao.py                confere todas as traduzidas
  python tools/validar-traducao.py 1.3-caminhos   confere as que começam assim
Saída: 0 sem erros, 1 com erros.
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PT_DIR, IT_DIR = ROOT / "aulas", ROOT / "aulas-it"

FENCE = re.compile(r"^(`{3,}|~{3,})\s*([\w+-]*)\s*$")
CODE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
LINK = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+)\)")
ITEM = re.compile(r"^( *)([-*+]|\d+[.)])\s")
TITULO = re.compile(r"^(#{1,6})\s")
SEP = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
COM_COMENTARIO = {"bash", "sh", "shell", "powershell", "ini", "yaml", "yml", "conf"}
# Marcas que não existem em italiano.
PORTUGUES = re.compile(r"[ãõçÃÕÇ]|\b(você|vocês|também|arquivo|arquivos|usuário|usuários|diretório|diretórios|aula|aulas)\b", re.I)


def linhas(p):
    t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    return t.rstrip("\n").split("\n")


def sem_comentario(l):
    """Remove o comentário de uma linha de código, respeitando aspas.

    Só conta como comentário '#' seguido de espaço. #!/bin/bash, #cloud-config,
    #include e linhas de configuração comentadas ficam intactas, assim como as
    teclas de vi ('# :wq Enter') e dumps ('# 0000000  o k').
    """
    tecla = re.match(r"^\s*#\s+:.*?\bEnter\b", l)
    if tecla:
        return tecla.group()
    if re.match(r"^\s*#\s+[0-9a-f]{2,7}\s", l):
        return l.rstrip()
    if re.match(r"^\s*#\s", l):
        return ""
    if re.match(r"^\s*#", l):
        return l.rstrip()
    aspas = None
    for i, c in enumerate(l):
        if aspas:
            if c == aspas:
                aspas = None
        elif c in "'\"":
            aspas = c
        elif c == "#" and i and l[i - 1] in " \t":
            return l[:i].rstrip()
    return l.rstrip()


def fora_de_codigo(l):
    return CODE.sub(" ", l)


def num_celulas(l):
    return len(re.findall(r"(?<!\\)\|", l))


def conferir(pt_path, it_path):
    erros, avisos = [], []
    pt, it = linhas(pt_path), linhas(it_path)
    if len(pt) != len(it):
        erros.append(f"número de linhas: PT {len(pt)}, IT {len(it)}. Mantenha uma linha traduzida para cada linha original.")
        for i, (a, b) in enumerate(zip(pt, it), 1):
            if (not a.strip()) != (not b.strip()) or bool(FENCE.match(a)) != bool(FENCE.match(b)):
                erros.append(f"L{i}: primeira linha fora de lugar. PT: {a[:90]!r} IT: {b[:90]!r}")
                break
        return erros, avisos

    cerca, lang = None, ""
    for i, (a, b) in enumerate(zip(pt, it), 1):
        m = FENCE.match(a)
        if cerca is None and m:
            cerca, lang = m.group(1), m.group(2).lower()
            if a != b:
                erros.append(f"L{i}: abertura de bloco de código alterada")
            continue
        if cerca is not None:
            if a.strip() == cerca:
                cerca = None
                if a != b:
                    erros.append(f"L{i}: fechamento de bloco de código alterado")
                continue
            if lang in COM_COMENTARIO:
                if sem_comentario(a) != sem_comentario(b):
                    erros.append(f"L{i}: comando alterado. PT: {a[:100]!r} IT: {b[:100]!r}")
                elif sem_comentario(a) != a.rstrip() and sem_comentario(b) == b.rstrip():
                    erros.append(f"L{i}: comentário removido. PT: {a[:100]!r}")
            elif a != b:
                erros.append(f"L{i}: saída/bloco alterado. PT: {a[:100]!r} IT: {b[:100]!r}")
            continue

        if not a.strip():
            if b.strip():
                erros.append(f"L{i}: deveria estar em branco")
            continue
        if a.startswith("<!--") or re.match(r"^\s*(-{3,}|\*{3,})\s*$", a) or SEP.match(a) and "-" in a and "|" in a:
            if a != b:
                erros.append(f"L{i}: linha estrutural alterada: {a[:60]!r}")
            continue

        for nome, r in (("título", TITULO), ("lista", ITEM)):
            ma, mb = r.match(a), r.match(b)
            if bool(ma) != bool(mb) or (ma and ma.group(1) != mb.group(1)):
                erros.append(f"L{i}: marcador de {nome} alterado")
        if a.startswith(">") != b.startswith(">"):
            erros.append(f"L{i}: citação (>) alterada")
        if a.lstrip().startswith("|") and num_celulas(a) != num_celulas(b):
            erros.append(f"L{i}: número de colunas alterado")

        ca = collections.Counter(m.group(2) for m in CODE.finditer(a))
        cb = collections.Counter(m.group(2) for m in CODE.finditer(b))
        if ca != cb:
            erros.append(f"L{i}: código inline alterado. Sumiu: {list((ca - cb))[:4]} Apareceu: {list((cb - ca))[:4]}")
        # A mesma imagem pode ter versão italiana (.it.jpg) ou ainda estar em outro formato.
        def alvos(linha):
            return [(m.group(1), re.sub(r"(\.it)?\.(jpg|png|svg)$", "", m.group(2)) if m.group(1) else m.group(2))
                    for m in LINK.finditer(linha)]
        if alvos(a) != alvos(b):
            erros.append(f"L{i}: link ou imagem alterado")

        texto = fora_de_codigo(b)
        if PORTUGUES.search(texto):
            if a == b:
                erros.append(f"L{i}: linha não traduzida: {a[:90]!r}")
            else:
                avisos.append(f"L{i}: pode ter português: {PORTUGUES.search(texto).group()!r}")
        if re.search(r"\bclass[ei]\b", texto, re.I):
            avisos.append(f"L{i}: use 'lezione', não 'classe', para aula")
    if cerca is not None:
        erros.append("bloco de código sem fechamento")
    h1 = next((l for l in it if l.startswith("# ")), "")
    if h1 and re.match(r"# Aula\b", next((l for l in pt if l.startswith("# ")), "")) and not h1.startswith("# Lezione "):
        erros.append(f"título deve começar com '# Lezione ': {h1[:70]!r}")
    return erros, avisos


def main():
    filtros = sys.argv[1:]
    if not IT_DIR.is_dir():
        print("aulas-it/ não existe: nenhuma tradução para conferir.")
        return 0
    arquivos = sorted(IT_DIR.glob("*.md"))
    if filtros:
        arquivos = [p for p in arquivos if any(p.name.startswith(f) for f in filtros)]
        if not arquivos:
            print(f"Nenhum arquivo em aulas-it/ começa com: {' '.join(filtros)}")
            return 1
    total = 0
    for p in arquivos:
        original = PT_DIR / p.name
        if not original.exists():
            print(f"ERRO {p.name}: não existe em aulas/. Use o mesmo nome do original.")
            total += 1
            continue
        erros, avisos = conferir(original, p)
        total += len(erros)
        print(f"{'OK  ' if not erros else 'ERRO'} {p.name}: {len(erros)} erros, {len(avisos)} avisos")
        for e in erros[:40]:
            print("   " + e)
        if len(erros) > 40:
            print(f"   ... e mais {len(erros) - 40} erros")
        for a in avisos[:10]:
            print("   aviso " + a)
    faltam = len(list(PT_DIR.glob("*.md"))) - len(list(IT_DIR.glob("*.md")))
    print(f"\nConferidas: {len(arquivos)} | Faltam traduzir: {faltam} | Erros: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
