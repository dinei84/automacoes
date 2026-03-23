import os
import shutil

PASTA_ORIGEM = os.path.join(os.path.expanduser("~"), "Downloads")

MAPA_EXTENSOES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Executaveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"],
}


def organizar_pasta():
    arquivos = os.listdir(PASTA_ORIGEM)

    for arquivo in arquivos:
        caminho_completo = os.path.join(PASTA_ORIGEM, arquivo)

        if os.path.isfile(caminho_completo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()
            categoria_encontrada = False

            # Tenta encontrar em categorias conhecidas
            for categoria, extensoes in MAPA_EXTENSOES.items():
                if extensao in extensoes:
                    pasta_destino = os.path.join(PASTA_ORIGEM, categoria)
                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)

                    shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
                    print(f"✅ Movido: '{arquivo}' -> {categoria}")
                    categoria_encontrada = True
                    break

            # Se terminou o loop e NÃO encontrou categoria, vai para "Outros"
            if not categoria_encontrada:
                pasta_outros = os.path.join(PASTA_ORIGEM, "Outros")
                if not os.path.exists(pasta_outros):
                    os.makedirs(pasta_outros)

                shutil.move(caminho_completo, os.path.join(pasta_outros, arquivo))
                print(f"📦 '{arquivo}' não listado -> Movido para 'Outros'")


if __name__ == "__main__":
    try:
        organizar_pasta()
        # Cria um arquivo de texto para confirmar que rodou
        with open(os.path.join(PASTA_ORIGEM, "log_sucesso.txt"), "a") as f:
            f.write(f"Rodou com sucesso em: {os.path.abspath(PASTA_ORIGEM)}\n")
    except Exception as e:
        # Se der erro, ele salva o motivo aqui
        with open(os.path.join(PASTA_ORIGEM, "erro_automacao.txt"), "a") as f:
            f.write(f"Erro: {str(e)}\n")
