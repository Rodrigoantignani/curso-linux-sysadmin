#!/usr/bin/env python3
"""Substitui todas as referências de SVG por PNG do NotebookLM nos Markdowns."""
import pathlib
import re

MAPEAMENTO = {
    "0.1-montar-o-laboratorio": "0.1-resumo",
    "0.2-acesso-e-protecao": "0.2-resumo",
    "1.1-o-que-e-linux": "1.1-resumo",
    "1.2-o-shell-e-a-ajuda": "1.2-resumo",
    "1.3-caminhos-e-navegacao": "1.3-resumo",
    "1.4-criar-copiar-mover-e-apagar": "1.4-resumo",
    "1.5-ler-e-procurar-texto": "1.5-resumo",
    "1.6-redirecionamentos-e-pipes": "1.6-resumo",
    "1.7-arquivar-e-compactar": "1.7-resumo",
    "1.8-primeiro-script": "1.8-resumo",
    "1.9-decidir-e-repetir": "1.9-resumo",
    "1.10-software-livre-na-pratica": "1.10-resumo",
    "2.1-instalacao-e-provisionamento": "2.1-resumo",
    "2.2-hardware-e-dispositivos": "2.2-resumo",
    "2.3-processos-e-logs": "2.3-resumo",
    "2.4-rede-no-dia-a-dia": "2.4-resumo",
    "2.5-acesso-remoto-e-privilegios": "2.5-resumo",
    "2.6-usuarios-e-grupos": "2.6-resumo",
    "2.7-permissoes-e-dono": "2.7-resumo",
    "2.8-diretorios-e-arquivos-especiais": "2.8-resumo",
    "3.1-fluxos-a-fundo": "3.1-resumo",
    "3.2-filtros-de-texto": "3.2-resumo",
    "3.3-regex-e-grep": "3.3-resumo",
    "3.4-sed-e-awk": "3.4-resumo",
    "3.5-vi-e-vim-de-verdade": "3.5-resumo",
    "4.1-como-o-linux-liga": "4.1-resumo",
    "4.2-systemd-servicos-e-units": "4.2-resumo",
    "4.3-targets-desligar-e-reiniciar": "4.3-resumo",
    "4.4-grub-e-acesso-de-emergencia": "4.4-resumo",
    "5.1-hardware-pelo-kernel": "5.1-resumo",
    "5.2-modulos-e-parametros": "5.2-resumo",
    "5.3-linux-como-convidado": "5.3-resumo",
    "6.1-pacotes-no-debian": "6.1-resumo",
    "6.2-pacotes-na-rocky": "6.2-resumo",
    "6.3-repositorios": "6.3-resumo",
    "6.4-flatpak": "6.4-resumo",
    "6.5-bibliotecas-compartilhadas": "6.5-resumo",
}

def main():
    aulas_dir = pathlib.Path("aulas")
    alterados = 0
    
    for aula_stem, novo_nome in MAPEAMENTO.items():
        p = aulas_dir / f"{aula_stem}.md"
        if not p.exists():
            print(f"NÃO ENCONTRADO: {p}")
            continue
        
        t = p.read_text(encoding="utf-8")
        original = t
        
        # Substitui TODAS as referências de imagem desta aula
        for img_ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", t):
            nome_arquivo = img_ref.split("/")[-1]
            nome_sem_ext = nome_arquivo.rsplit(".", 1)[0]
            # Só substitui se for uma imagem desta aula (começa com o número da aula)
            if nome_sem_ext.startswith(aula_stem.split("-")[0] + "-" + aula_stem.split("-")[1]):
                novo_ref = f"../img/{novo_nome}.png"
                t = t.replace(img_ref, novo_ref)
        
        if t != original:
            p.write_text(t, encoding="utf-8", newline="\n")
            alterados += 1
            print(f"OK: {p.name}")
        else:
            print(f"SEM MUDANÇAS: {p.name}")
    
    print(f"\n{alterados} arquivos alterados")

if __name__ == "__main__":
    main()
