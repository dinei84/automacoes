import os

import send2trash


def get_screenshots_path():
    home = os.path.expanduser("~")

    possible_origins = [
        os.path.join(home, "OneDrive", "Imagens", "Screenshots"),
        os.path.join(home, "OneDrive", "Imagens", "Capturas de Tela"),
        os.path.join(home, "OneDrive", "Pictures", "Screenshots"),
        os.path.join(home, "Pictures", "Screenshots"),
        os.path.join(home, "Imagens", "Capturas de tela"),
    ]

    for p in possible_origins:
        if os.path.exists(p):
            return p

    return possible_origins[0]


PASTA_ORIGEM = get_screenshots_path()


def organizar_prints():
    try:
        if not os.path.exists(PASTA_ORIGEM):
            print(f"A pasta de origem não existe: {PASTA_ORIGEM}")
            return

        arquivos = os.listdir(PASTA_ORIGEM)
        arquivos_removidos = 0

        for arquivo in arquivos:
            if arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
                caminho_arquivo = os.path.join(PASTA_ORIGEM, arquivo)

                try:
                    # Envia para a Lixeira real do Windows
                    send2trash.send2trash(caminho_arquivo)
                    arquivos_removidos += 1
                    print(f"Enviado para a lixeira: {arquivo}")
                except Exception as e_trash:
                    print(f"Erro ao enviar {arquivo} para a lixeira: {e_trash}")

        print(f"Total de arquivos enviados para a lixeira: {arquivos_removidos}")

    except Exception as e:
        print(f"Erro ao organizar prints: {e}")


if __name__ == "__main__":
    organizar_prints()
