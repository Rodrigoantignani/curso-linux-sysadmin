#!/usr/bin/env python3
"""Gera os diagramas SVG das aulas 2.3 a 6.5.

Uso: python tools/gerar-diagramas.py
Saida: img/<aula>-<assunto>.svg
"""
import html
import pathlib
import textwrap

W = 1400
BG = "#f6f4ee"
INK = "#14213d"
MUTED = "#5b6472"
CARD = "#ffffff"
STROKE = "#d8d5cc"
FONT = "'Segoe UI', Arial, sans-serif"
MONO = "'Cascadia Code', Consolas, monospace"

STYLE = """
    .bg { fill: #f6f4ee; }
    .title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 40px; font-weight: 700; fill: #14213d; }
    .subtitle { font-family: 'Segoe UI', Arial, sans-serif; font-size: 19px; fill: #5b6472; }
    .h2 { font-family: 'Segoe UI', Arial, sans-serif; font-size: 21px; font-weight: 700; fill: #14213d; }
    .card { fill: #ffffff; stroke: #d8d5cc; stroke-width: 1.5; }
    .step-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 21px; font-weight: 700; fill: #14213d; }
    .step-sub { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; fill: #5b6472; }
    .small { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #5b6472; }
    .body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; fill: #2b3240; }
    .mono { font-family: 'Cascadia Code', Consolas, monospace; font-size: 14px; fill: #2563eb; }
    .term { font-family: 'Cascadia Code', Consolas, monospace; font-size: 15px; fill: #e2e8f0; }
    .term-title { font-family: 'Cascadia Code', Consolas, monospace; font-size: 17px; font-weight: 700; fill: #ffffff; }
    .num { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; font-weight: 700; fill: #ffffff; }
    .foot { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; fill: #5b6472; }
    .foot-strong { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; font-weight: 700; fill: #14213d; }
    .arrow { stroke: #8b93a1; stroke-width: 2.5; fill: none; }
    .tag { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #ffffff; }
"""

DEFS = """
  <defs>
    <marker id="seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#8b93a1"/>
    </marker>
  </defs>
"""


def esc(text):
    return html.escape(str(text), quote=True)


def wrap(text, width):
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False) or [""]


def head(title, subtitle, height):
    return (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" role="img" aria-labelledby="titulo desc">\n'
        f'  <title id="titulo">{esc(title)}</title>\n'
        f'  <desc id="desc">{esc(subtitle)}</desc>\n'
        f'  <style>{STYLE}  </style>\n'
        f'{DEFS}\n'
        f'  <rect class="bg" x="0" y="0" width="{W}" height="{height}"/>\n'
        f'  <text class="title" x="60" y="62">{esc(title)}</text>\n'
        f'  <text class="subtitle" x="60" y="98">{esc(subtitle)}</text>\n'
    )


def foot(text, height):
    lines = wrap(text, 150)
    y = height - 30 - (len(lines) - 1) * 20
    parts = [f'  <line x1="60" y1="{height-64}" x2="1340" y2="{height-64}" stroke="#d8d5cc" stroke-width="1"/>']
    for i, line in enumerate(lines):
        parts.append(f'  <text class="foot" x="60" y="{y + i*20}">{esc(line)}</text>')
    parts.append("</svg>\n")
    return "\n".join(parts)


def side_panel(x, y, w, h, title, items, accent):
    out = [f'  <rect class="card" x="{x}" y="{y}" width="{w}" height="{h}" rx="16"/>',
           f'  <rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{accent}"/>',
           f'  <text class="h2" x="{x+28}" y="{y+38}">{esc(title)}</text>']
    cy = y + 74
    for lead, text in items:
        out.append(f'  <circle cx="{x+34}" cy="{cy-5}" r="6" fill="{accent}"/>')
        out.append(f'  <text class="body" x="{x+52}" y="{cy}" style="font-weight:700">{esc(lead)}</text>')
        cy += 24
        for line in wrap(text, max(24, int((w - 60) / 7.1))):
            out.append(f'  <text class="small" x="{x+52}" y="{cy}">{esc(line)}</text>')
            cy += 20
        cy += 16
    return "\n".join(out)


def flow_v(title, subtitle, steps, side_title, side_items, footer, accent):
    top = 148
    gap = 24
    wrapped = [wrap(sub, 74)[:3] for _, sub in steps]
    step_h = 108 + max(0, max(len(lines) for lines in wrapped) - 2) * 21
    left_h = len(steps) * (step_h + gap) - gap
    side_h = 74 + sum(24 + len(wrap(t, 62)) * 20 + 16 for _, t in side_items) + 16
    height = max(top + left_h, top + side_h) + 110
    out = [head(title, subtitle, height)]
    y = top
    for i, (st, sub) in enumerate(steps):
        out.append(f'  <rect class="card" x="60" y="{y}" width="720" height="{step_h}" rx="14"/>')
        out.append(f'  <rect x="60" y="{y}" width="8" height="{step_h}" rx="4" fill="{accent}"/>')
        out.append(f'  <circle cx="102" cy="{y+step_h/2}" r="19" fill="{accent}"/>')
        out.append(f'  <text class="num" x="102" y="{y+step_h/2+5}" text-anchor="middle">{i+1}</text>')
        out.append(f'  <text class="step-title" x="136" y="{y+38}">{esc(st)}</text>')
        for j, line in enumerate(wrapped[i]):
            out.append(f'  <text class="step-sub" x="136" y="{y+64+j*21}">{esc(line)}</text>')
        if i < len(steps) - 1:
            out.append(f'  <line class="arrow" x1="420" y1="{y+step_h}" x2="420" y2="{y+step_h+gap}" marker-end="url(#seta)"/>')
        y += step_h + gap
    out.append(side_panel(820, top, 520, min(side_h, height - top - 80), side_title, side_items, accent))
    out.append(foot(footer, height))
    return "\n".join(out)


def flow_h(title, subtitle, cards, footer, accent):
    top = 176
    ch = 300
    gap = 26
    n = len(cards)
    cw = (1280 - gap * (n - 1)) / n
    height = top + ch + 120
    out = [head(title, subtitle, height)]
    for i, card in enumerate(cards):
        st, sub, tag = card
        x = 60 + i * (cw + gap)
        out.append(f'  <rect class="card" x="{x:.0f}" y="{top}" width="{cw:.0f}" height="{ch}" rx="14"/>')
        out.append(f'  <rect x="{x:.0f}" y="{top}" width="{cw:.0f}" height="10" rx="5" fill="{accent}"/>')
        out.append(f'  <circle cx="{x+30:.0f}" cy="{top+46}" r="17" fill="{accent}"/>')
        out.append(f'  <text class="num" x="{x+30:.0f}" y="{top+51}" text-anchor="middle">{i+1}</text>')
        ty = top + 46
        for line in wrap(st, max(10, int((cw - 54) / 8.6)))[:2]:
            out.append(f'  <text class="step-title" x="{x+56:.0f}" y="{ty}" style="font-size:18px">{esc(line)}</text>')
            ty += 23
        ty = max(ty + 8, top + 96)
        for line in wrap(sub, max(12, int((cw - 30) / 6.6)))[:6]:
            out.append(f'  <text class="small" x="{x+16:.0f}" y="{ty}">{esc(line)}</text>')
            ty += 19
        if tag:
            out.append(f'  <rect x="{x+16:.0f}" y="{top+ch-42}" width="{cw-32:.0f}" height="26" rx="13" fill="{accent}" opacity="0.12"/>')
            out.append(f'  <text class="small" x="{x+28:.0f}" y="{top+ch-24}" style="font-weight:700;fill:{accent}">{esc(tag)}</text>')
        if i < n - 1:
            ax1 = x + cw
            out.append(f'  <line class="arrow" x1="{ax1+2:.0f}" y1="{top+ch/2}" x2="{ax1+gap-4:.0f}" y2="{top+ch/2}" marker-end="url(#seta)"/>')
    out.append(foot(footer, height))
    return "\n".join(out)


def split(title, subtitle, left, right, footer, accent):
    top = 156
    left_title, left_sub, left_items = left
    right_title, right_sub, right_items = right
    rows = max(len(left_items), len(right_items))
    panel_h = 96 + rows * 92
    height = top + panel_h + 110
    out = [head(title, subtitle, height)]
    for x, (pt, ps, items) in ((60, left), (720, right)):
        out.append(f'  <rect class="card" x="{x}" y="{top}" width="620" height="{panel_h}" rx="16"/>')
        out.append(f'  <rect x="{x}" y="{top}" width="620" height="64" rx="16" fill="{accent}" opacity="0.10"/>')
        out.append(f'  <rect x="{x}" y="{top+48}" width="620" height="16" fill="{accent}" opacity="0.10"/>')
        out.append(f'  <text class="h2" x="{x+24}" y="{top+40}">{esc(pt)}</text>')
        out.append(f'  <text class="small" x="{x+24}" y="{top+88}">{esc(ps)}</text>')
        cy = top + 116
        for it, txt in items:
            out.append(f'  <circle cx="{x+30}" cy="{cy-5}" r="5" fill="{accent}"/>')
            out.append(f'  <text class="body" x="{x+46}" y="{cy}" style="font-weight:700">{esc(it)}</text>')
            cy += 22
            for line in wrap(txt, 78):
                out.append(f'  <text class="small" x="{x+46}" y="{cy}">{esc(line)}</text>')
                cy += 19
            cy += 14
    out.append(foot(footer, height))
    return "\n".join(out)


def layers(title, subtitle, bars, side_title, side_items, footer, accent):
    top = 156
    bar_h = 86
    gap = 12
    n = len(bars)
    left_h = n * (bar_h + gap) - gap
    side_h = 74 + sum(24 + len(wrap(t, 56)) * 20 + 16 for _, t in side_items) + 16
    height = max(top + left_h, top + side_h) + 110
    out = [head(title, subtitle, height)]
    y = top
    for i, (st, sub) in enumerate(bars):
        out.append(f'  <rect class="card" x="60" y="{y}" width="780" height="{bar_h}" rx="12"/>')
        out.append(f'  <rect x="60" y="{y}" width="10" height="{bar_h}" rx="5" fill="{accent}"/>')
        out.append(f'  <text class="step-title" x="90" y="{y+32}" style="font-size:19px">{esc(st)}</text>')
        for j, line in enumerate(wrap(sub, 88)[:2]):
            out.append(f'  <text class="small" x="90" y="{y+55+j*18}">{esc(line)}</text>')
        if i < n - 1:
            out.append(f'  <line class="arrow" x1="450" y1="{y+bar_h}" x2="450" y2="{y+bar_h+gap}" marker-end="url(#seta)"/>')
        y += bar_h + gap
    out.append(side_panel(880, top, 460, min(side_h, height - top - 80), side_title, side_items, accent))
    out.append(foot(footer, height))
    return "\n".join(out)


def grid(title, subtitle, cards, footer, accent, cols=3):
    top = 156
    gap = 26
    cw = (1280 - gap * (cols - 1)) / cols
    ch = 230
    rows = (len(cards) + cols - 1) // cols
    height = top + rows * (ch + gap) - gap + 110
    out = [head(title, subtitle, height)]
    for i, (st, sub) in enumerate(cards):
        r, c = divmod(i, cols)
        x = 60 + c * (cw + gap)
        y = top + r * (ch + gap)
        out.append(f'  <rect class="card" x="{x:.0f}" y="{y}" width="{cw:.0f}" height="{ch}" rx="14"/>')
        out.append(f'  <rect x="{x:.0f}" y="{y}" width="{cw:.0f}" height="10" rx="5" fill="{accent}"/>')
        out.append(f'  <circle cx="{x+34:.0f}" cy="{y+48}" r="17" fill="{accent}"/>')
        out.append(f'  <text class="num" x="{x+34:.0f}" y="{y+53}" text-anchor="middle">{i+1}</text>')
        ty = y + 48
        for line in wrap(st, int((cw - 70) / 8.4))[:2]:
            out.append(f'  <text class="step-title" x="{x+62:.0f}" y="{ty}" style="font-size:19px">{esc(line)}</text>')
            ty += 23
        ty = max(ty + 8, y + 92)
        for line in wrap(sub, int((cw - 34) / 6.6))[:6]:
            out.append(f'  <text class="small" x="{x+17:.0f}" y="{ty}">{esc(line)}</text>')
            ty += 19
    out.append(foot(footer, height))
    return "\n".join(out)


def terminal(title, subtitle, term_title, lines, side_title, side_items, footer, accent):
    top = 156
    line_h = 27
    card_h = 74 + len(lines) * line_h
    side_h = 74 + sum(24 + len(wrap(t, 56)) * 20 + 16 for _, t in side_items) + 16
    height = max(top + card_h, top + side_h) + 110
    out = [head(title, subtitle, height)]
    out.append(f'  <rect class="card" x="60" y="{top}" width="700" height="{card_h}" rx="14"/>')
    out.append(f'  <path d="M60 {top+14} a14 14 0 0 1 14 -14 h672 a14 14 0 0 1 14 14 v46 h-700 z" fill="{INK}"/>')
    out.append(f'  <text class="term-title" x="86" y="{top+36}">{esc(term_title)}</text>')
    out.append(f'  <rect x="60" y="{top+60}" width="700" height="4" fill="{accent}"/>')
    y = top + 92
    for line in lines:
        style = ' style="fill:#7dd3fc"' if line.strip().startswith("$") else ""
        out.append(f'  <text class="term" x="88" y="{y}"{style}>{esc(line)}</text>')
        y += line_h
    out.append(side_panel(800, top, 540, min(side_h, height - top - 80), side_title, side_items, accent))
    out.append(foot(footer, height))
    return "\n".join(out)


def ladder(title, subtitle, levels, footer, accent):
    top = 160
    row_h = 96
    gap = 10
    n = len(levels)
    height = top + n * (row_h + gap) - gap + 120
    out = [head(title, subtitle, height)]
    out.append(f'  <path class="arrow" d="M46 {top+n*(row_h+gap)-gap} V{top+18}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="18" y="{top-12}" style="font-weight:700">sobe</text>')
    for i, (name, cmd, question) in enumerate(reversed(levels)):
        y = top + i * (row_h + gap)
        lvl = n - 1 - i
        out.append(f'  <rect class="card" x="70" y="{y}" width="1300" height="{row_h}" rx="12"/>')
        out.append(f'  <rect x="70" y="{y}" width="10" height="{row_h}" rx="5" fill="{accent}"/>')
        out.append(f'  <circle cx="112" cy="{y+row_h/2}" r="20" fill="{accent}"/>')
        out.append(f'  <text class="num" x="112" y="{y+row_h/2+5}" text-anchor="middle">{lvl}</text>')
        out.append(f'  <text class="step-title" x="150" y="{y+34}" style="font-size:20px">{esc(name)}</text>')
        out.append(f'  <text class="mono" x="150" y="{y+62}">{esc(cmd)}</text>')
        out.append(f'  <text class="step-sub" x="470" y="{y+40}">{esc(question)}</text>')
        out.append(f'  <text class="small" x="470" y="{y+66}">{esc("depende dos degraus de baixo" if lvl > 0 else "a base: se falhar, tudo acima falha")}</text>')
    out.append(foot(footer, height))
    return "\n".join(out)


def state_vim(title, subtitle, footer, accent):
    height = 860
    out = [head(title, subtitle, height)]
    top = 200
    # normal
    out.append(f'  <rect x="520" y="{top}" width="360" height="150" rx="18" fill="{accent}"/>')
    out.append(f'  <text x="700" y="{top+52}" text-anchor="middle" style="font-family:{FONT};font-size:30px;font-weight:700;fill:#fff">NORMAL</text>')
    out.append(f'  <text x="700" y="{top+86}" text-anchor="middle" style="font-family:{FONT};font-size:15px;fill:#dbeafe">cada tecla é um comando</text>')
    out.append(f'  <text x="700" y="{top+112}" text-anchor="middle" style="font-family:{MONO};font-size:14px;fill:#bfdbfe">x  d  y  p  u  /</text>')
    # insert
    out.append(f'  <rect x="1010" y="{top-10}" width="330" height="150" rx="18" fill="#059669"/>')
    out.append(f'  <text x="1175" y="{top+42}" text-anchor="middle" style="font-family:{FONT};font-size:28px;font-weight:700;fill:#fff">INSERÇÃO</text>')
    out.append(f'  <text x="1175" y="{top+76}" text-anchor="middle" style="font-family:{FONT};font-size:15px;fill:#d1fae5">as teclas viram texto</text>')
    out.append(f'  <text x="1175" y="{top+102}" text-anchor="middle" style="font-family:{MONO};font-size:14px;fill:#a7f3d0">-- INSERT --</text>')
    out.append(f'  <line class="arrow" x1="884" y1="{top+50}" x2="1002" y2="{top+40}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="898" y="{top+32}">i  a  o  I  A  O</text>')
    out.append(f'  <line class="arrow" x1="1002" y1="{top+100}" x2="884" y2="{top+100}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="918" y="{top+120}">Esc</text>')
    # command
    out.append(f'  <rect x="520" y="540" width="360" height="150" rx="18" fill="#d97706"/>')
    out.append(f'  <text x="700" y="592" text-anchor="middle" style="font-family:{FONT};font-size:28px;font-weight:700;fill:#fff">LINHA DE COMANDO</text>')
    out.append(f'  <text x="700" y="626" text-anchor="middle" style="font-family:{FONT};font-size:15px;fill:#fef3c7">roda quando você aperta Enter</text>')
    out.append(f'  <text x="700" y="652" text-anchor="middle" style="font-family:{MONO};font-size:14px;fill:#fde68a">:wq  :%s/a/b/g  /regex</text>')
    out.append(f'  <line class="arrow" x1="700" y1="{top+150}" x2="700" y2="532" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="714" y="{top+190}">:  /  ?</text>')
    out.append(f'  <line class="arrow" x1="720" y1="532" x2="720" y2="{top+158}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="734" y="520">Enter ou Esc</text>')
    # visual
    out.append(f'  <rect x="70" y="{top-10}" width="330" height="150" rx="18" fill="#7c3aed"/>')
    out.append(f'  <text x="235" y="{top+42}" text-anchor="middle" style="font-family:{FONT};font-size:28px;font-weight:700;fill:#fff">VISUAL</text>')
    out.append(f'  <text x="235" y="{top+76}" text-anchor="middle" style="font-family:{FONT};font-size:15px;fill:#ede9fe">seleciona texto ou linhas</text>')
    out.append(f'  <text x="235" y="{top+102}" text-anchor="middle" style="font-family:{MONO};font-size:14px;fill:#ddd6fe">v  V  Ctrl-v</text>')
    out.append(f'  <line class="arrow" x1="516" y1="{top+50}" x2="404" y2="{top+40}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="424" y="{top+32}">v  V  Ctrl-v</text>')
    out.append(f'  <line class="arrow" x1="404" y1="{top+100}" x2="516" y2="{top+100}" marker-end="url(#seta)"/>')
    out.append(f'  <text class="small" x="430" y="{top+120}">Esc</text>')
    # grammar strip
    out.append(f'  <rect class="card" x="70" y="730" width="1270" height="66" rx="12"/>')
    out.append(f'  <text class="body" x="94" y="760" style="font-weight:700">A gramática do modo normal:</text>')
    out.append(f'  <text class="mono" x="432" y="760" style="font-size:16px">[contagem] operador [contagem] movimento</text>')
    out.append(f'  <text class="small" x="94" y="783">dw apaga até a próxima palavra · c$ troca até o fim da linha · 3dd apaga três linhas · yy copia a linha · p cola</text>')
    out.append(foot(footer, height))
    return "\n".join(out)


# (arquivo, titulo, subtitulo, layout, dados, legenda)
DIAGRAMS = []


def add(filename, title, subtitle, layout, data, footer, accent):
    DIAGRAMS.append((filename, title, subtitle, layout, data, footer, accent))


ACC = {"blue": "#2563eb", "purple": "#7c3aed", "green": "#059669", "amber": "#d97706", "cyan": "#0891b2", "red": "#dc2626"}

# ---------------- M2 ----------------
add("2.3-arvore-processos", "A árvore de processos", "Todo processo é filho de outro: PID, PPID, dono, estado e uma caixa de sinais", "terminal",
    {"term": "systemd (PID 1)", "lines": [
        "systemd (PID 1)          <- o avô de todos; adota os órfãos",
        " ├─ sshd                 <- serviço",
        " │   └─ sshd: rodrigo    <- a sua conexão",
        " │       └─ bash         <- o seu shell",
        " │           ├─ sleep 600 &",
        " │           └─ ps -ef --forest",
        " ├─ chronyd",
        " └─ crond"], "side": ("Quatro ideias", [
        ("Árvore", "Todo processo nasce de outro (fork); o primeiro é o systemd, PID 1. Matar o pai pode levar os filhos junto ou deixá-los órfãos."),
        ("Estado", "R rodando, S dormindo, D preso no disco (nem o -9 resolve), T parado, Z zumbi."),
        ("Sinal", "15 pede para sair, 9 mata, 1 avisa que o terminal sumiu. O processo pode tratar 15 e 1; o 9 o kernel aplica direto."),
        ("Registro", "O que o processo escreve na saída de erro e o que o kernel e o systemd veem vai para o journal. Sem disco, sumiu no boot.")])},
    "Se o boot parou ou o serviço caiu, olhe a árvore e o estado antes de matar: o PID certo e o sinal certo resolvem; o -9 esconde a causa.", "blue")

add("2.4-escada-da-rede", "A escada da rede", "Teste de baixo para cima: o primeiro degrau que falha é o problema; os de cima falham por consequência", "ladder",
    {"levels": [
        ("Placa", "ip -br link", "A placa existe e está UP?"),
        ("Endereço", "ip -br addr", "Tenho IP? Estou na rede certa?"),
        ("Rota", "ip route · ping <gateway>", "Sei sair da minha rede?"),
        ("Nome", "getent hosts nome", "O nome vira IP?"),
        ("Porta", "ss -tlnp (servidor) · nc (fora)", "Alguém escuta? Consigo chegar até a porta?"),
        ("Aplicação", "curl -v", "O serviço responde direito?")]},
    "Cada degrau depende dos de baixo. Teste sempre na ordem: um DNS 'fora' pode ser apenas uma rota errada.", "cyan")

add("2.5-duas-portas", "Duas portas: entrar e mandar", "O SSH decide se você entra; o sudo decide o que você pode fazer depois", "flow_h",
    {"cards": [
        ("Chave privada", "Fica no seu computador e nunca sai. Assina o desafio que o servidor manda.", "seu lado"),
        ("sshd", "Confere a assinatura com a pública do authorized_keys e aplica o sshd_config.", "porta 22"),
        ("Sessão rodrigo", "Você entrou. O journal e o /var/log/secure registram o método e a origem.", "UID comum"),
        ("sudoers", "Uma lista separada decide quais comandos rodrigo pode rodar como root.", "visudo"),
        ("root", "Só agora o comando roda com UID 0. Cada porta grava por que disse não.", "UID 0")]},
    "As duas portas têm listas e logs próprios. Entrar não é o mesmo que mandar: um usuário pode entrar por SSH e não ter sudo nenhum.", "purple")

add("2.6-tres-listas", "Uma conta são três listas", "O nome é para você; o sistema guarda e confere só os números (UID e GID)", "grid",
    {"cards": [
        ("/etc/passwd · todos leem", "ana:x:2001:2001:Ana Lima:/home/ana:/bin/bash — nome, UID, GID, descrição, pasta e shell. O 'x' manda a senha para o shadow."),
        ("/etc/shadow · só o root", "ana:$6$...:20395:0:90:7::: — hash, última troca, mínimo, máximo e aviso. É aqui que a validade da senha mora."),
        ("/etc/group · todos leem", "equipe:x:2000:ana,bruno — nome, GID e membros extras. O grupo principal não aparece aqui: ele está no 4º campo do passwd.")]},
    "Apagar a conta não apaga os arquivos dela. O próximo usuário com o mesmo UID herda tudo: por isso UID de sistema não se reutiliza.", "amber")

add("2.7-tres-trincas", "Quem pergunta primeiro vence", "O kernel usa uma trinca só: dono, senão grupo, senão outros — e para na primeira que casa", "split",
    {"left": ("Anatomia de -rwxr-x---", "um arquivo, lido da esquerda para a direita", [
        ("Tipo", "— arquivo · d pasta · l link"),
        ("Dono: rwx = 7", "ler, escrever e executar"),
        ("Grupo: r-x = 5", "ler e executar, sem escrever"),
        ("Outros: --- = 0", "ninguém de fora entra"),
        ("Octal: 750", "4+2+1 · 4+0+1 · 0"),
        ("Sufixos", ". = contexto SELinux · + = ACL")]),
     "right": ("Quem está pedindo?", "a primeira pergunta que casa decide", [
        ("É o dono?", "usa rwx e para aqui."),
        ("Está no grupo?", "usa r-x e para aqui."),
        ("Não é nenhum dos dois?", "usa --- e para aqui."),
        ("Numa pasta", "r lista nomes, w cria/apaga/renomeia, x deixa atravessar."),
        ("Numa pasta, w manda", "apagar depende da permissão da pasta, não do arquivo.")])},
    "A primeira trinca que casa decide; as outras nem são olhadas. As mesmas letras significam coisas diferentes em arquivo e em pasta.", "green")

add("2.8-bits-especiais", "Os três bits especiais", "O modo tem quatro dígitos em octal: o primeiro guarda setuid, setgid e sticky", "grid",
    {"cards": [
        ("setuid (4)", "Num executável, roda com o UID do dono. Em pasta, o Linux ignora. No ls -l aparece como s no lugar do x: rws (bit + x) ou rwS (bit sem x)."),
        ("setgid (2)", "Num executável, roda com o GID do grupo. Numa pasta, todo arquivo novo herda o grupo dela. Aparece como s na trinca do grupo."),
        ("sticky (1)", "Numa pasta, só o dono do arquivo apaga ou renomeia. É o /tmp. Aparece como t (bit + x) ou T (bit sem x) na trinca dos outros.")]},
    "3770 = especiais 3 (setgid + sticky), dono 7, grupo 7, outros 0. E o link é só um nome que aponta para um inode; o inode aponta para os dados.", "purple")

# ---------------- M3 ----------------
add("3.1-tres-canais", "Os três canais e a ordem do redirecionamento", "O shell troca o destino antes de o comando começar, da esquerda para a direita", "terminal",
    {"term": "ordem importa", "lines": [
        "$ cmd > f 2>&1",
        "  1 -> f          depois 2 -> f          tudo no arquivo",
        "$ cmd 2>&1 > f",
        "  2 -> tela       depois 1 -> f          erros na tela",
        "$ sudo echo oi > /etc/teste.conf",
        "  o shell abre o arquivo ANTES do sudo: Permission denied",
        "$ echo oi | sudo tee /etc/teste.conf > /dev/null",
        "  o tee, como root, abre o arquivo; o shell só abre /dev/null"], "side": ("O essencial", [
        ("Três canais", "0 é stdin, 1 é stdout e 2 é stderr. Todo processo nasce com os três."),
        ("O comando não vê o >", "Ele só escreve no 1 e no 2, sem saber se é tela, arquivo ou pipe."),
        ("2>&1 copia", "Ele copia para onde o 1 aponta agora, não para o arquivo por nome."),
        ("tee e xargs", "tee mostra e grava; xargs transforma linhas em argumentos.")])},
    "Leia da esquerda para a direita: trocar a ordem de 2>&1 muda o resultado. Antes de um rm, use echo para ver o que o shell montou.", "amber")

add("3.2-linha-de-producao", "Uma linha de produção de filtros", "Cada filtro lê linhas, faz uma coisa só e entrega o resultado ao próximo", "flow_h",
    {"cards": [
        ("acesso.log", "O arquivo bruto: 15 linhas de log.", "entrada"),
        ("cut -d' ' -f1", "Separa pelo espaço e guarda só o primeiro campo: o IP.", "só o IP"),
        ("sort", "Junta os iguais em blocos, para o uniq contar de verdade.", "iguais juntos"),
        ("uniq -c", "Conta cada bloco de linhas iguais.", "conta vizinhos"),
        ("sort -rn", "Ordena pelo número, do maior para o menor.", "maior primeiro"),
        ("head -3", "Corta os três primeiros.", "os 3 IPs")]},
    "Sem sort antes do uniq, o mesmo valor aparece em blocos separados e a contagem sai errada. Nenhum filtro altera o arquivo original.", "cyan")

add("3.3-regex", "O padrão casa um pedaço, não a linha toda", "O grep pergunta 'existe algum trecho desta linha que casa?' e imprime a linha inteira", "split",
    {"left": ("O que o padrão casa", "o susto vem de esquecer que ele casa em qualquer lugar", [
        ("10.1.0.2", "Casa dentro de 10.1.0.20: o 0 que sobra não importa."),
        ("O ponto é coringa", "10a1b0c2 também casa, porque . aceita qualquer caractere."),
        ("A linha sai inteira", "O grep não recorta o trecho: ele mostra a linha completa."),
        ("Pode casar com nada", "Um * ou uma linha vazia casam com toda linha.")]),
     "right": ("Como dizer exatamente", "três jeitos de fechar o cerco", [
        ("-F '10.1.0.2'", "Texto fixo: o ponto vira ponto e deixa de ser coringa."),
        ("-w", "Palavra inteira: 10.1.0.20 não serve para o padrão 10.1.0.2."),
        ("'^10\\.1\\.0\\.2 '", "Âncora no começo, pontos escapados e um espaço no fim."),
        ("Teste sempre", "Uma linha que deve casar e outra que não deve.")])},
    "Antes de confiar no padrão, pergunte onde ele pode casar, o que cada caractere especial significa e se ele pode casar com nada.", "purple")

add("3.4-sed-awk", "Dois laços sobre as linhas", "sed aplica comandos e imprime; awk separa em campos, testa e executa a ação", "split",
    {"left": ("sed · o editor de linha", "lê uma linha, aplica os comandos em ordem e imprime", [
        ("s/yes/no/", "Troca a primeira ocorrência na linha."),
        ("s/yes/no/g", "Com g, troca todas as ocorrências."),
        ("-n e p", "Com -n, só imprime quando você manda com p."),
        ("-i", "A saída vira um arquivo novo que toma o lugar do original."),
        ("$ e endereços", "1d apaga a primeira linha; /regex/d apaga as que casam.")]),
     "right": ("awk · o processador de campos", "lê uma linha, separa em campos e testa cada padrão", [
        ("$1, $9, $NF", "Campos por número; NF é o total e $NF é o último."),
        ("BEGIN e END", "Rodam uma vez, antes da primeira e depois da última linha."),
        ("padrão { ação }", "Se o padrão é verdadeiro, a ação roda naquela linha."),
        ("$9 >= 400 {print $1, $9}", "Os IPs com erro, lado a lado."),
        ("NR", "O número da linha atual; no END, o total de linhas.")])},
    "Pergunte 'o que acontece com cada linha?', não 'o que acontece com o arquivo?'. Nenhum dos dois volta atrás nem olha a linha seguinte.", "green")

add("3.5-modos-do-vim", "Os modos do vim", "No modo normal cada tecla é um comando; para escrever, entre no modo de inserção e saia com Esc", "state",
    {}, "Na dúvida, aperte Esc duas vezes: você volta ao modo normal, de onde tudo começa. A gramática é [contagem] operador [contagem] movimento.", "green")

add("4.1-corrida-do-boot", "A corrida de revezamento do boot", "Cinco corredores passam o bastão; se o boot parou, pergunte quem estava com ele", "flow_h",
    {"cards": [
        ("Firmware", "UEFI ou BIOS acha o disco e carrega o GRUB.", "No bootable device"),
        ("GRUB 2", "Põe o kernel e o initramfs na memória e entrega a linha de comando.", "grub> ou grub rescue>"),
        ("Kernel", "Liga o hardware e executa o initramfs.", "Kernel panic"),
        ("initramfs", "Acha e monta o disco raiz de verdade e chama o systemd.", "dracut:/# ou (initramfs)"),
        ("systemd (PID 1)", "Sobe os serviços até o target padrão.", "modo de emergência")]},
    "Cada etapa tem uma cara diferente na tela. Guarde a tabela: ela é o mapa de toda emergência de boot do resto do curso.", "blue")

add("4.2-dois-interruptores", "Dois interruptores e uma tomada tapada", "start/stop mudam agora; enable/disable decidem o próximo boot; mask tapa a tomada", "grid",
    {"cards": [
        ("start · stop", "Ligam e desligam o processo neste momento. O efeito some no próximo reboot. É o interruptor de agora."),
        ("enable · disable", "Decidem se o serviço sobe sozinho no próximo boot. Não mexem no processo que está rodando agora. É o interruptor do boot."),
        ("mask", "Tapa a tomada: ninguém liga o serviço, nem você, nem o boot, nem outra unit. É diferente de disable.")]},
    "Leia sempre Loaded: e Active:. active + disabled é o serviço que some no próximo boot; inactive + enabled é o que só sobe no próximo boot, ou caiu.", "amber")

add("4.3-regua-dos-targets", "A régua dos targets", "Da menos para a mais coisa ligada: cada target é uma lista do que precisa estar de pé", "ladder",
    {"levels": [
        ("emergency", "emergency.target", "Raiz só de leitura, shell de root, sem rede e sem sshd."),
        ("rescue", "rescue.target", "Discos do fstab montados, shell de root, sem rede."),
        ("multi-user", "multi-user.target", "Rede, sshd e todos os serviços. O padrão de um servidor."),
        ("graphical", "graphical.target", "Tudo do multi-user mais a tela gráfica.")]},
    "set-default muda o próximo boot, como enable; isolate muda agora, como start. runlevel 3 = multi-user; runlevel 1 = rescue.", "purple")

add("4.4-cardapio-do-grub", "O cardápio do GRUB e as duas receitas de resgate", "Cada entrada é uma receita: kernel, initramfs e a linha linux que o kernel repassa ao systemd", "split",
    {"left": ("O cardápio", "mexer na receita de dois jeitos", [
        ("Cada entrada", "Diz qual kernel, qual initramfs e quais parâmetros passar."),
        ("Na hora: e, Ctrl+X", "A edição vale só para este boot."),
        ("De vez na Rocky", "grubby altera a entrada e regenera a configuração."),
        ("De vez na Debian", "/etc/default/grub seguido de update-grub."),
        ("Parâmetro útil", "systemd.unit=rescue.target sobe direto no modo de manutenção.")]),
     "right": ("As duas receitas", "parar antes do sistema normal é o que dá root sem senha", [
        ("Rocky: rd.break", "Para no fim do initramfs. Depois: remount rw, chroot, passwd, touch /.autorelabel, reboot."),
        ("Debian: init=/bin/bash", "Troca o systemd por um bash como PID 1. Depois: remount rw, passwd, reboot."),
        ("Por que funciona", "Ainda não existe ninguém pedindo senha: o shell já é root."),
        ("A defesa", "Quem tem o console tem o root. Proteja o GRUB ou cifre o disco.")])},
    "O parâmetro certo para no ponto certo: rd.break no fim do initramfs; init=/bin/bash troca o systemd por um bash como primeiro processo.", "red")

# ---------------- M5 ----------------
add("5.1-portaria-do-kernel", "O kernel como portaria do prédio", "Cada peça é um morador; o driver é o funcionário que sabe falar com ela", "layers",
    {"bars": [
        ("Hardware", "A peça física: disco, placa de rede, USB. O morador que chega."),
        ("Kernel e driver", "A portaria registra a chegada e escala um funcionário que fala a língua da peça."),
        ("udev", "A cada chegada, cria a plaquinha na porta e nomes estáveis em /dev/disk/by-id."),
        ("/dev", "O arquivo que o programa abre: /dev/sdb, /dev/sda, /dev/ttyUSB0."),
        ("Programas", "Falam com a peça através do arquivo em /dev, sem saber qual driver está atrás.")], "side": ("Onde olhar", [
        ("dmesg", "O livro de ocorrências: o que chegou e o que o driver reclamou."),
        ("/sys", "O cadastro organizado por andar e por tipo."),
        ("/proc", "O quadro de avisos com números do dia: memória, CPU e processos."),
        ("lspci -k · lsusb · lsblk", "Jeitos bonitos de ler o cadastro e ver qual driver está em uso.")])},
    "Sem driver, a peça existe mas ninguém conversa com ela. dmesg e journalctl -k contam a história da chegada e do erro.", "blue")

add("5.2-canivete", "O kernel é um canivete com lâminas de encaixe", "O cabo sobe no boot; cada lâmina é um módulo .ko que você encaixa e tira", "layers",
    {"bars": [
        ("O cabo: kernel básico", "O que sobe no boot e sustenta o resto."),
        ("As lâminas: módulos", "Arquivos .ko em /lib/modules/$(uname -r)/. modprobe encaixa; modprobe -r tira."),
        ("As dependências", "Algumas lâminas precisam de outras. O modprobe encaixa a família; o insmod não."),
        ("As regulagens", "Parâmetros do módulo, escolhidos ao encaixar ou anotados em /etc/modprobe.d/."),
        ("O painel: sysctl", "O comportamento geral do kernel, visível em /proc/sys/ e persistido em /etc/sysctl.d/.")], "side": ("Comandos", [
        ("lsmod", "O que está encaixado agora."),
        ("modinfo", "O que a lâmina é, quais parâmetros aceita e de quem depende."),
        ("blacklist", "Impede o carregamento automático. install ... /bin/false bloqueia também o carregamento manual."),
        ("sysctl -w e -p", "Muda agora e grava a regulagem para o próximo boot.")])},
    "Prefira blacklist a install /bin/false: o primeiro deixa o módulo disponível para carregar à mão; o segundo bloqueia também o carregamento manual.", "amber")

add("5.3-vm-ou-container", "VM e contêiner: sala alugada ou divisória", "A VM tem kernel próprio; o contêiner usa o kernel do nó", "split",
    {"left": ("VM · sala com portaria", "o hipervisor finge ser o hardware", [
        ("Kernel próprio", "Cada VM sobe o seu kernel e os seus drivers."),
        ("virtio", "O interfone com o síndico: em vez de fingir hardware antigo, fala a língua do hipervisor."),
        ("Guest agent", "O zelador: responde ao Proxmox quando ele pergunta o IP ou pede para desligar."),
        ("cloud-init", "O kit de mudança do primeiro boot: nome, usuários e chaves."),
        ("Clone", "Precisa de hostname, machine-id e chaves SSH novos.")]),
     "right": ("Contêiner · divisória", "isolamento sem outro kernel", [
        ("Sem kernel próprio", "Usa o kernel do nó; compartilha a portaria."),
        ("Isolamento", "Namespaces e cgroups separam processos, rede e limites."),
        ("Leve", "Sobe em segundos e gasta pouco, porque não carrega outro sistema."),
        ("Quando usar", "Aplicação isolada, sem precisar de outro kernel nem de outro sistema."),
        ("Cuidado", "Kernel compartilhado: uma falha no kernel afeta todos.")])},
    "A pergunta de decisão é sempre a mesma: preciso de outro kernel, de outro sistema ou de isolamento forte? Se não, o contêiner basta.", "cyan")

# ---------------- M6 ----------------
add("6.1-almoxarifado-debian", "O almoxarifado do Debian", "O apt compra e resolve dependências; o dpkg guarda, desempacota e anota no inventário", "flow_v",
    {"steps": [
        ("Fontes", "Os fornecedores ficam em /etc/apt/sources.list.d/*.sources, no formato deb822."),
        ("apt update", "Baixa os catálogos para /var/lib/apt/lists/. Não instala nada."),
        ("apt install", "Resolve as dependências e baixa os .deb para /var/cache/apt/archives/."),
        ("dpkg", "Desempacota, roda os scripts e anota tudo em /var/lib/dpkg/status."),
        ("Inventário", "dpkg -S acha o dono de um arquivo; dpkg -L lista o conteúdo; apt purge remove a configuração.")], "side": ("O que confunde", [
        ("apt compra, dpkg guarda", "O dpkg não sai para buscar dependência: se falta uma caixa, ele reclama e para."),
        ("remove x purge", "remove apaga os arquivos e mantém a configuração; purge apaga tudo."),
        ("manual x automático", "apt-mark showmanual separa o que você pediu do que veio de dependência."),
        ("deb822", "O formato novo usa campos URIs, Suites e Components; o antigo é uma linha só.")])},
    "O apt só atualiza os catálogos com update. Quem entrega a caixa ao almoxarife é o install, na ordem que as dependências exigem.", "amber")

add("6.2-almoxarifado-rocky", "O almoxarifado da Rocky", "O dnf compra, resolve e anota a transação; o rpm instala e confere o que mudou", "flow_v",
    {"steps": [
        ("Repositórios", "Os /etc/yum.repos.d/*.repo dizem de onde comprar."),
        ("dnf", "Baixa os metadados para /var/cache/dnf/ e resolve as dependências."),
        ("Transação", "O dnf monta a lista do que entra e do que sai antes de tocar no sistema."),
        ("rpm", "Instala e registra arquivo por arquivo no banco rpm."),
        ("Histórico", "dnf history mostra o livro numerado; dnf history undo desfaz uma transação.")], "side": ("O que a Rocky tem de bom", [
        ("rpm -V", "Diz exatamente quais arquivos de um pacote foram alterados."),
        ("dnf history undo", "Devolve a transação inteira, não um pacote por vez."),
        (".rpmnew e .rpmsave", "O que fazer quando a configuração local e a do pacote divergem."),
        ("Banco rpm", "Em versões novas mora em /usr/lib/sysimage/rpm; /var/lib/rpm aponta para lá.")])},
    "O rpm instala um pacote por vez e não resolve dependências. Quem resolve e guarda o histórico é o dnf. Para desfazer, use o número da transação.", "blue")

add("6.3-loja-com-catalogo", "O repositório é uma loja com catálogo", "O cliente baixa o catálogo, confere o selo e só então pega o pacote", "split",
    {"left": ("Rocky · dnf", "cada pacote carrega a própria assinatura", [
        ("O endereço", "baseurl, mirrorlist ou metalink no arquivo .repo."),
        ("O catálogo", "repodata/repomd.xml e os arquivos que ele aponta."),
        ("O selo", "gpgcheck=1 e a chave em /etc/pki/rpm-gpg/."),
        ("A assinatura", "Está no próprio .rpm: o dnf confere antes de instalar."),
        ("EPEL e CRB", "Repositórios extras com regras próprias de habilitação.")]),
     "right": ("Debian · apt", "o índice é assinado; os .deb são conferidos pelo hash", [
        ("O endereço", "URIs, Suites e Components no sources.list ou no .sources."),
        ("O catálogo", "dists/<suite>/InRelease, assinado, e Packages com os hashes."),
        ("O selo", "Signed-By: aponta a chave em /usr/share/keyrings ou /etc/apt/keyrings."),
        ("A assinatura", "O .deb solto não carrega assinatura: vale o hash do índice."),
        ("Repositório local", "A ISO montada vira uma loja com file:// e o mesmo contrato.")])},
    "No RPM, cada pacote é assinado; no Debian, o índice é assinado e os pacotes são conferidos pelo hash. Sem selo conhecido, o cliente não compra.", "green")

add("6.4-apartamento", "O Flatpak é um apartamento mobiliado", "O prédio é a distro; o runtime é a mobília compartilhada; o app traz só o que é dele", "layers",
    {"bars": [
        ("Remote", "A imobiliária: o Flathub ou outro repositório de aplicações."),
        ("Download OSTree", "Baixa só o que mudou, em vez do aplicativo inteiro."),
        ("Runtime e app", "O runtime traz as bibliotecas básicas; o app traz só o próprio programa."),
        ("Sandbox", "Dentro da caixa, /usr é o do runtime e /app é o app. Kernel e usuários são do host."),
        ("Permissões", "Rede, home e X11/Wayland só funcionam se a permissão deixar.")], "side": ("No dia a dia", [
        ("flatpak run", "Roda o app dentro do sandbox, sem enxergar as bibliotecas da distro."),
        ("flatpak override", "Ajusta as portas do apartamento, por app."),
        ("Sistema ou usuário", "A instalação vai para /var/lib/flatpak ou ~/.local/share/flatpak."),
        ("Quando faz sentido", "Aplicativo gráfico e de desktop; num servidor, quase nunca.")])},
    "O app nunca enxerga o /usr da Rocky: é isso que o faz rodar igual em qualquer distro. Num servidor, o pacote nativo continua sendo a escolha.", "purple")

add("6.5-loader", "A agenda do loader", "O binário pede pelo nome; o loader procura numa ordem fixa e desiste com 'cannot open shared object file'", "flow_v",
    {"steps": [
        ("O binário pede", "No ELF está gravado NEEDED libz.so.1: só o nome, sem endereço."),
        ("RUNPATH ou RPATH", "O caminho gravado no binário: o RPATH antigo vem antes do LD_LIBRARY_PATH; o RUNPATH moderno, depois."),
        ("LD_LIBRARY_PATH", "A variável de ambiente vem depois e vale só para aquela execução."),
        ("/etc/ld.so.cache", "A agenda que o ldconfig monta a partir de /etc/ld.so.conf.d."),
        ("Pastas padrão", "/lib64 e /usr/lib64 na Rocky; /lib/x86_64-linux-gnu na Debian."),
        ("Não achou", "error while loading shared libraries: libz.so.1: cannot open shared object file.")], "side": ("Os três nomes", [
        ("real name", "libfoo.so.1.4.2: o arquivo de verdade, criado pelo pacote."),
        ("soname", "libfoo.so.1: o nome gravado nos programas; o ldconfig cria o link."),
        ("linker name", "libfoo.so: serve para compilar com -lfoo; vem no pacote -devel ou -dev."),
        ("ldd x readelf", "ldd pode executar o binário; readelf -d só lê o arquivo, com segurança.")])},
    "Se a pasta não está na lista e ninguém rodou ldconfig, o loader não acha, mesmo com o arquivo lá. Soname diferente significa interface diferente.", "red")


# ---------------- M1 ----------------
add("1.5-fluxo-ler-texto", "Como ler um arquivo sem travar o terminal", "Medir o tamanho, escolher a lupa certa e nunca usar cat em log gigante", "split",
    {"left": ("O arquivo dita a ferramenta", "tamanho do arquivo → comando certo", [
        ("Até 20 linhas", "cat ou cat n — cabe na tela"),
        ("Dezenas a centenas", "head n 20 / tail n 20 — só o começo ou o fim"),
        ("Qualquer coisa maior", "less — lê só o que está na tela"),
        ("Acompanhar ao vivo", "tail -f — fica olhando o fim"),
        ("Log rotacionado", "tail -F — reabre se o arquivo for trocado")]),
     "right": ("O que o grep deixa passar", "a linha exista, mas o padrão não casa", [
        ("maiúsculas × minúsculas", "ERROR ≠ error; use -i para ignorar caixa"),
        ("não está no fim", "$ é antes do \\n, não do caractere; cat -A mostra o invisível"),
        ("veio do Windows", "\\r no fim de cada linha; cat -A mostra ^M"),
        ("não existe de verdade", "o padrão pode casar com nada; teste com -c e com -v")])},
    "Cat desenrola tudo; less é a lupa; grep é a peneira. Meça antes de abrir: ls -lh diz se cabe num cat.", "blue")

add("1.8-fluxo-executar-script", "Como o shell decide rodar um script", "Três perguntas definem se a receita entra no forno", "flow_h",
    {"cards": [
        ("Shebang", "#!/bin/bash na primeira linha, sem espaço antes", "shebang"),
        ("Permissão x", "chmod +x; senão o arquivo é só texto", "executável"),
        ("Onde está", "./script ou pasta do PATH; o diretório atual não conta", "caminho"),
        ("Variável vazia", 'rm -rf "$PASTA"/* com PASTA="" vira rm -rf /*', "proteja")]},
    "Sem shebang, quem chama escolhe o interpretador. Sem permissão x, não executa. Sem aspas na variável, um vazio apaga tudo.", "amber")

# ---------------- M2 ----------------
add("2.3-roteiro-lento", "O roteiro 'está lento'", "Seis comandos, na ordem, e você já sabe onde olhar", "flow_v",
    {"steps": [
        ("1. uptime", "carga de 1, 5 e 15 min; compare com nproc"),
        ("2. top -bn1", "us, wa, st na linha %Cpu(s)"),
        ("3. free -h", "a coluna available, não a free"),
        ("4. vmstat 1 5", "r fila, b presos em D, si/so swap"),
        ("5. ps aux --sort", "o culpado de processador e de memória"),
        ("6. journalctl -p warning", "o que o sistema reclamou na última hora")], "side": ("O que cada número diz", [
        ("carga alta + processador parado", "o problema é disco ou rede (wa alto, processos em D)"),
        ("carga alta + processador cheio", "é processo mesmo; ache o topo com ps aux --sort=-%cpu"),
        ("si/so acima de zero o tempo todo", "memória curta: o sistema está swapando")])},
    "Leia da primeira à sexta linha, sem pular. Um ping que não responde não prova que a máquina está fora; um firewall pode estar bloqueando ICMP.", "red")

add("2.4-erros-de-rede", "Quatro erros de rede e em que degrau cada um mora", "A mensagem de erro já diz onde olhar", "split",
    {"left": ("Mensagem → degrau", "o que cada erro aponta", [
        ("No route to host", "degrau 2 (rota): não há caminho até o gateway"),
        ("Connection refused", "degrau 4 (porta): ninguém escuta nessa porta"),
        ("Name or service not known", "degrau 3 (nome): o nome não vira IP"),
        ("comando fica parado", "degrau 5 (aplicação): o serviço não responde")]),
     "right": ("O que testar em cada degrau", "da placa para cima", [
        ("0 · Placa", "ip -br link → UP ou NO-CARRIER"),
        ("1 · Endereço", "ip -br addr → tenho IP na rede certa?"),
        ("2 · Rota", "ip route; ping no gateway"),
        ("3 · Nome", "getent hosts nome"),
        ("4 · Porta", "ss -tlnp; nc ou /dev/tcp de fora"),
        ("5 · Aplicação", "curl -v")])},
    "Suba um degrau por vez. Se o servidor não tem IP, não adianta testar DNS. Se o nome não resolve, não adianta olhar o firewall do site.", "cyan")

add("2.5-quando-usar-sudo", "SSH decide se você entra; sudo decide o que você faz", "Duas portas, duas listas, dois logs", "split",
    {"left": ("Porta 1 · entrar (SSH)", "confere quem você é e de onde vem", [
        ("chave privada", "fica com você; nunca sai do seu computador"),
        ("chave pública", "vai para o ~/.ssh/authorized_keys do servidor"),
        ("known_hosts", "você confere a identidade do servidor"),
        ("sshd_config", "decide se aceita chave, senha ou root direto")]),
     "right": ("Porta 2 · mandar (sudo)", "confere o que você pode fazer como root", [
        ("sudo -l", "mostra suas regras antes de usar"),
        ("sudo comando", "roda só um comando como root e anota no log"),
        ("sudo -i", "vira root de verdade; o log diz 'root fez'"),
        ("/etc/sudoers.d", "regras novas, sempre com visudo")])},
    "Entrar não é o mesmo que mandar. Um usuário pode entrar por SSH e não ter sudo nenhum. Cada porta escreve no log por que disse não.", "purple")

add("2.6-colaboradora-sem-sudo", "O que fazer quando o sudo some", "A colega estava no wheel e saiu; descubra como e devolva", "flow_v",
    {"steps": [
        ("1. Confirmar", "sudo -l -U ana mostra que não há regra"),
        ("2. Ver grupos", "id ana → ela saiu do wheel/equipe"),
        ("3. Ver regras", "ls /etc/sudoers.d/; cat /etc/sudoers.d/ana"),
        ("4. Devolver", "usermod -aG wheel ana (Rocky) ou usermod -aG sudo ana (Debian)"),
        ("5. Testar", "sudo -l -U ana volta a mostrar (ALL) ALL")], "side": ("Por que sumiu", [
        ("usermod -G sem -a", "substituiu todos os grupos em vez de adicionar"),
        ("arquivo de sudo apagado", "alguém removeu /etc/sudoers.d/ana"),
        ("logout entre idades", "o grupo novo só vale no próximo login")])},
    "Editar sudoers à mão é perigoso: visudo confere a sintaxe antes de gravar. Um ponto no nome do arquivo faz a regra não valer.", "green")

# ---------------- M3 ----------------
add("3.1-fluxo-redirecionamento", "stdout, stderr e a ordem do redirecionamento", "O shell troca o destino antes do comando começar, da esquerda para a direita", "flow_h",
    {"cards": [
        ("> f", "stdout (1) vai para o arquivo f", "apenas o bom"),
        ("2> f", "stderr (2) vai para o arquivo f", "apenas o ruim"),
        ("2>&1", "stderr copia para onde o 1 aponta agora", "cópia de ponteiro"),
        ("sudo tee", "o tee, como root, abre o arquivo", "gravar como root")]},
    "2>&1 > f e > f 2>&1 dão resultados diferentes: a ordem é da esquerda para a direita. O comando não vê o >; ele só escreve no 1 e no 2.", "amber")

add("3.2-qual-filtro-usar", "Qual filtro usar para cada tarefa", "Cada filtro faz uma coisa só e entrega ao próximo", "grid",
    {"cards": [
        ("grep", "escolhe linhas que casam com um padrão — filtrar linhas"),
        ("sed", "troca, apaga ou mostra linhas — transformar linhas"),
        ("awk", "separa em campos e testa cada linha — colunas e contas"),
        ("cut", "pega colunas por delimitador — um campo por linha"),
        ("sort", "junta iguais em blocos — ordenar"),
        ("uniq", "conta ou remove repetições vizinhas — contar blocos")]},
    "Sem sort antes do uniq, o mesmo valor aparece em blocos separados e a contagem sai errada. Nenhum filtro altera o arquivo original.", "cyan")

add("3.3-qual-busca-usar", "Qual ferramenta de busca usar", "O padrão casa um pedaço, não a linha toda", "split",
    {"left": ("grep", "mostra a linha inteira que casa", [
        ("-F", "texto literal: o ponto vira ponto, não coringa"),
        ("-w", "palavra inteira: 10.1.0.20 não casa com 10.1.0.2"),
        ("-i", "ignora maiúsculas e minúsculas"),
        ("-r", "procura em todos os arquivos de uma pasta"),
        ("-n", "mostra o número da linha")]),
     "right": ("Quando o grep não é suficiente", "use outra ferramenta", [
        ("sed", "para trocar ou apagar linhas específicas"),
        ("awk", "para colunas, contas e somas"),
        ("locate / find", "para achar arquivos pelo nome, não pelo conteúdo"),
        ("rg (ripgrep)", "mais rápido que grep em pastas grandes")])},
    "Antes de confiar no padrão, pergunte onde ele pode casar, o que cada caractere especial significa e se ele pode casar com nada.", "purple")

add("3.4-sed-ou-awk", "sed ou awk?", "sed aplica comandos e imprime; awk separa em campos e executa ações", "split",
    {"left": ("Use sed quando", "quer editar texto linha por linha", [
        ("s/antigo/novo/g", "troca todas as ocorrências"),
        ("-n ... p", "mostra só as linhas que você manda"),
        ("-i", "grava a mudança no próprio arquivo"),
        ("/regex/d", "apaga as linhas que casam")]),
     "right": ("Use awk quando", "precisa de colunas, contas ou somas", [
        ("$1, $9, $NF", "campos por número; NF é o total"),
        ("padrão { ação }", "se o padrão é verdadeiro, a ação roda"),
        ("BEGIN e END", "rodam antes da primeira e depois da última linha"),
        ("soma de campos", "some o 9º campo de todas as linhas")])},
    "Pergunte 'o que acontece com cada linha?', não 'o que acontece com o arquivo?'. Nenhum dos dois volta atrás nem olha a linha seguinte.", "green")

# ---------------- 3.5 ----------------
add("3.5-como-sair-do-vim", "Como sair do vim sem perder nada", "Quatro caminhos de saída; só um grava se houver mudança", "grid",
    {"cards": [
        (":wq", "grava e sai — sempre grava"),
        (":x ou ZZ", "grava só se mudou e sai — o mais educado"),
        (":q!", "sai e descarta tudo — desiste das mudanças"),
        (":q", "sai, se não houver mudança — recusa com E37")]},
    "Na dúvida, aperte Esc duas vezes para voltar ao modo normal, de onde tudo começa. A gramática é [contagem] operador [contagem] movimento.", "red")

# ---------------- M1 extras ----------------
add("1.5-fluxo-grep", "Como o grep peneira um arquivo", "Passa o rolo inteiro e só deixa sair as linhas que casam", "flow_v",
    {"steps": [
        ("grep 'texto'", "mostra as linhas que contêm o texto"),
        ("grep -n", "acrescenta o número da linha"),
        ("grep -i", "ignora maiúsculas e minúsculas"),
        ("grep -c", "só conta, não mostra as linhas"),
        ("grep -v", "mostra as linhas que NÃO casam"),
        ("grep -C 3", "mostra 3 linhas antes e depois de cada achado")], "side": ("Quando o grep erra", [
        ("arquivo do Windows", "\r no fim de cada linha; cat -A mostra ^M"),
        ("última linha sem \n", "wc -l não conta a última linha"),
        ("padrão casa em qualquer lugar", "use -w para palavra inteira")])},
    "O grep não recorta o trecho: ele mostra a linha completa. Teste sempre com uma linha que deve casar e outra que não deve.", "blue")

# ---------------- M2 extras ----------------
add("2.7-decisao-permissao", "Quem pode ler, escrever ou executar", "A primeira trinca que casa decide; as outras nem são olhadas", "flow_v",
    {"steps": [
        ("1. É o dono?", "usa rwx e para aqui — dono do arquivo"),
        ("2. Está no grupo?", "usa r-x e para aqui — membro do grupo"),
        ("3. Não é nenhum?", "usa --- e para aqui — todos os outros"),
        ("4. É pasta?", "r lista, w cria/apaga, x atravessa — regras diferentes")], "side": ("Octal de cabeça", [
        ("r = 4, w = 2, x = 1", "some os que quer liberar"),
        ("750 = rwx r-x ---", "dono tudo, grupo ler+executar, outros nada"),
        ("640 = rw- r----", "dono lê e escreve, grupo só lê")])},
    "Em pasta, w manda: apagar depende da permissão da pasta, não do arquivo.", "green")

add("2.8-quando-usar-bits-especiais", "Os três bits especiais na prática", "O quarto dígito octal guarda setuid, setgid e sticky", "grid",
    {"cards": [
        ("setuid (4)", "executa com o UID do dono do arquivo — ex: /usr/bin/passwd"),
        ("setgid (2)", "arquivos novos herdam o grupo da pasta — ex: pastas compartilhadas"),
        ("sticky (1)", "só o dono apaga ou renomeia — ex: /tmp")]},
    "3770 = especiais 3 (setgid + sticky), dono 7, grupo 7, outros 0. O link é só um nome que aponta para um inode.", "purple")

# ---------------- M4 extra ----------------
add("4.1-analise-do-boot", "Medir o boot com systemd-analyze", "blame diz quem demorou; critical-chain diz quem fez esperar", "split",
    {"left": ("systemd-analyze blame", "quem consumiu mais tempo", [
        ("ordem decrescente", "o mais lento fica no topo"),
        ("seconds", "tempo em segundos desde o boot"),
        ("milhares de ms", "cada serviço conta")]),
     "right": ("systemd-analyze critical-chain", "a corrente que atrasa o boot", [
        ("quem espera quem", "A deve subir antes de B"),
        ("o ponto crítico", "o serviço mais lento no caminho"),
        ("tempo acumulado", "soma da cadeia inteira")])},
    "Compare o topo do blame com a corrente do critical-chain. Muitas vezes são units diferentes: o blame diz quem demorou, o critical-chain diz quem fez o boot esperar.", "blue")

add("4.2-start-enable-mask", "start/stop, enable/disable e mask", "Dois interruptores: o de agora e o do próximo boot", "grid",
    {"cards": [
        ("start · stop", "ligam e desligam o processo neste instante. Somem no reboot."),
        ("enable · disable", "decidem se sobe sozinho no próximo boot. Não mexem no que roda agora."),
        ("mask", "tapa a tomada: ninguém liga, nem você, nem o boot.")]},
    "active + disabled = some no próximo boot. inactive + enabled = só sobe no próximo boot, ou caiu.", "amber")

add("4.3-isolate-emergency", "isolate muda o target agora", "Emergency, rescue, multi-user e graphical: cada um desliga o que não precisa", "ladder",
    {"levels": [
        ("graphical", "tudo ligado, incluindo tela gráfica", "servidor de desktop"),
        ("multi-user", "rede, sshd, todos os serviços", "servidor padrão"),
        ("rescue", "discos montados, shell de root, sem rede", "manutenção"),
        ("emergency", "raiz só de leitura, shell de root, sem nada", "último recurso")]},
    "isolate muda agora (como start); set-default muda o próximo boot (como enable). Por SSH, nunca isole rescue ou emergency num servidor remoto.", "purple")

add("4.4-rd-break-init-bash", "Duas receitas de resgate no GRUB", "Parar antes do sistema normal é o que dá root sem senha", "split",
    {"left": ("Rocky: rd.break", "para no fim do initramfs", [
        ("remount rw", "mount -o remount,rw /sysroot"),
        ("chroot /sysroot", "entra no sistema real"),
        ("passwd", "muda a senha do root"),
        ("touch /.autorelabel", "força relabel SELinux no boot"),
        ("reboot", "volta ao sistema normal")]),
     "right": ("Debian: init=/bin/bash", "troca o systemd por um bash como PID 1", [
        ("remount rw", "mount -o remount,rw /"),
        ("passwd", "muda a senha do root"),
        ("reboot -f", "força a reinicialização"),
        ("não precisa de autorelabel", "o Debian não usa SELinux por padrão")])},
    "Ainda não existe ninguém pedindo senha: o shell já é root. Quem tem o console tem o root — proteja o GRUB ou cifre o disco.", "red")

# ---------------- M5 extra ----------------
add("5.1-uuid-by-id", "Não confie em sda e sdb", "Use UUID ou /dev/disk/by-id; a ordem dos discos pode mudar", "terminal",
    {"term": "lsblk -f", "lines": [
        "NAME   FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS",
        "sda                                         3f1a2b4c-...   5.2G     12% /",
        "sdb                                         7e8f9a0b-...   1.0G      0% ",
        "sr0                                     iso9660 2026-11-05-...   0B   100% /run/media/rodrigo/ISO"],
     "side": ("Onde olhar", [
        ("lsblk -f", "lista discos, UUID e ponto de montagem"),
        ("/dev/disk/by-id", "nomes estáveis, independente da ordem"),
        ("/dev/disk/by-uuid", "acesso direto pelo UUID"),
        ("dmesg | tail", "o que o kernel viu na chegada do disco"),
        ("blkid", "mostra UUID e tipo de sistema de arquivos")])},
    "A ordem sda/sdb muda se você adicionar ou remover um disco. No fstab, use UUID ou by-id, nunca o nome do dispositivo.", "cyan")

add("5.2-modprobe-blacklist", "Módulos do kernel: encaixar e tirar", "modprobe respeita dependências; insmod não. blacklist só impede a carga automática", "layers",
    {"bars": [
        ("lsmod", "o que está encaixado agora."),
        ("modprobe nome", "encaixa o módulo e suas dependências."),
        ("modprobe -r nome", "tira o módulo (se ninguém precisar dele)."),
        ("blacklist nome", "impede a carga automática no boot."),
        ("install nome /bin/false", "bloqueia também o carregamento manual.")],
     "side": ("Onde fica", [
        ("/lib/modules/$(uname -r)/", "os arquivos .ko de cada lâmina"),
        ("/etc/modprobe.d/", "suas regras de blacklist e install"),
        ("/etc/sysctl.d/", "as regulagens do kernel para o próximo boot")])},
    "Prefira blacklist a install /bin/false: o primeiro deixa o módulo disponível para carregar à mão; o segundo bloqueia também o carregamento manual.", "amber")

add("5.3-cloud-init-guest-agent", "VM pronta para o dia a dia", "cloud-init no primeiro boot; guest agent responde ao hipervisor", "flow_h",
    {"cards": [
        ("cloud-init", "nome, usuários e chaves SSH no primeiro boot", "primeiro boot"),
        ("guest agent", "responde ao Proxmox: IP, desligar, informações", "interfone"),
        ("virtio", "fala a língua do hipervisor em vez de fingir hardware antigo", "desempenho"),
        ("clone", "precisa de hostname, machine-id e chaves SSH novos", "cuidado")]},
    "A VM tem kernel próprio; o contêiner usa o kernel do nó. A pergunta de decisão: preciso de outro kernel ou isolamento forte basta?", "cyan")

# ---------------- M6 extra ----------------
add("6.1-apt-dpkg-purge", "apt remove vs apt purge", "remove apaga os arquivos, purge apaga também a configuração", "flow_v",
    {"steps": [
        ("apt remove", "apaga os binários, mantém /etc — reinstala e mantém seus ajustes"),
        ("apt purge", "apaga binários e configuração — recomeça do zero"),
        ("dpkg -l | grep ^rc", "pacotes removidos com configuração sobrando — restos para limpar"),
        ("apt install -f", "conserta dependências quebradas — sempre rode depois de dpkg -i")], "side": ("O travão do apt", [
        ("Could not get lock", "outro apt está rodando; ache o PID no erro"),
        ("dpkg --configure -a", "termina configurações interrompidas"),
        ("sem sudo", "apt não grava em /var; use sudo ou root")])},
    "Quer recomeçar do zero? Use purge. Só remove? Use remove. dpkg -i sem dependências trava o apt: instale com apt instal ./pacote.deb.", "blue")

add("6.2-rpm-V-history", "rpm confere arquivo por arquivo", "dnf resolve e histórico; rpm instala e registra", "split",
    {"left": ("rpm -V pacote", "quais arquivos mudaram desde a instalação", [
        ("S", "tamanho diferente"),
        ("M", "modo/permissão diferente"),
        ("5", "checksum MD5 diferente"),
        ("D", "dispositivo diferente"),
        ("L", "caminho de leitura diferente")]),
     "right": ("dnf history", "o livro numerado de transações", [
        ("dnf history", "lista todas as transações com ID"),
        ("dnf history undo N", "desfaz a transação inteira de uma vez"),
        ("dnf history redo N", "refaz uma transação desfeita")])},
    "O rpm instala um pacote por vez e não resolve dependências. Quem resolve e guarda o histórico é o dnf. Para desfazer, use o número da transação.", "blue")

add("6.3-gpgcheck-repomd", "O selo do repositório", "Sem a chave assinada, o cliente não compra o pacote", "split",
    {"left": ("Rocky · dnf", "cada pacote carrega a própria assinatura", [
        ("gpgcheck=1", "confere a assinatura antes de instalar"),
        ("chave em /etc/pki/rpm-gpg/", "a confiança começa aqui"),
        ("repodata/repomd.xml", "o catálogo assinado")]),
     "right": ("Debian · apt", "o índice é assinado; os .deb são conferidos pelo hash", [
        ("Signed-By:", "aponta a chave em /usr/share/keyrings/"),
        ("InRelease", "o índice assinado que o apt baixa"),
        ("hash do .deb", "conferido contra o índice, não contra uma chave própria")])},
    "No RPM, cada pacote é assinado; no Debian, o índice é assinado e os pacotes são conferidos pelo hash. Sem selo conhecido, o cliente não compra.", "green")

add("6.4-flatpak-unused", "O Flatpak e os runtimes órfãos", "Remover o app não remove o runtime; use --unused", "flow_v",
    {"steps": [
        ("flatpak uninstall app", "apaga só o aplicativo — o runtime fica para trás"),
        ("flatpak uninstall --unused", "remove runtimes que nenhum app usa — libera disco"),
        ("flatpak info --show-permissions", "veja o que o app pode acessar — antes de confiar"),
        ("flatpak remotes", "confira o escopo: system ou user — onde o remote foi adicionado")], "side": ("Sandbox", [
        ("filesystem=host", "lê quase tudo do host; não é proteção total"),
        ("rede, home, X11/Wayland", "só funcionam se a permissão deixar"),
        ("runtime compartilhado", "várias apps usam a mesma mobília")])},
    "App com filesystem=host lê quase tudo. Antes de confiar, rode flatpak info --show-permissions.", "purple")

add("6.5-ldconfig-soname", "O loader procura pelo soname", "Não pelo arquivo com versão: ldconfig recria o symlink", "terminal",
    {"term": "ldd ./app", "lines": [
        "linux-vdso.so.1 =>  (0x0000...)",
        "libola.so.1 => /opt/ola/lib/libola.so.1 (0x0000...)",
        "libc.so.6 => /lib64/libc.so.6 (0x0000...)",
        "/lib64/ld-linux-x86-64.so.2 (0x0000...)"],
     "side": ("Os três nomes", [
        ("real name", "libola.so.1.1.0: o arquivo de verdade"),
        ("soname", "libola.so.1: o nome gravado no programa"),
        ("linker name", "libola.so: serve para compilar com -l")])},
    "Se a pasta não está na lista e ninguém rodou ldconfig, o loader não acha, mesmo com o arquivo lá. Soname diferente = interface diferente.", "red")

def build(name, title, subtitle, layout, data, footer, accent):
    if layout == "flow_v":
        return flow_v(title, subtitle, data["steps"], data["side"][0], data["side"][1], footer, accent)
    if layout == "flow_h":
        return flow_h(title, subtitle, data["cards"], footer, accent)
    if layout == "split":
        return split(title, subtitle, data["left"], data["right"], footer, accent)
    if layout == "layers":
        return layers(title, subtitle, data["bars"], data["side"][0], data["side"][1], footer, accent)
    if layout == "grid":
        return grid(title, subtitle, data["cards"], footer, accent)
    if layout == "terminal":
        return terminal(title, subtitle, data["term"], data["lines"], data["side"][0], data["side"][1], footer, accent)
    if layout == "ladder":
        return ladder(title, subtitle, data["levels"], footer, accent)
    if layout == "state":
        return state_vim(title, subtitle, footer, accent)
    raise ValueError(layout)


def main():
    out = pathlib.Path("img")
    out.mkdir(exist_ok=True)
    for stem, title, subtitle, layout, data, footer, accent_name in DIAGRAMS:
        accent = ACC[accent_name]
        svg = build(stem, title, subtitle, layout, data, footer, accent)
        (out / f"{stem}.svg").write_text(svg, encoding="utf-8", newline="\n")
        print("ok", stem)


if __name__ == "__main__":
    main()
