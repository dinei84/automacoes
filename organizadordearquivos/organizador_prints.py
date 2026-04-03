import os
import shutil


def get_default_paths():
    home = os.path.expanduser("~")
    
    # Try common OneDrive and local paths for Screenshots
    possible_origins = [
        os.path.join(home, "OneDrive", "Imagens", "Screenshots"),
        os.path.join(home, "OneDrive", "Imagens", "Capturas de tela"),
        os.path.join(home, "OneDrive", "Pictures", "Screenshots"),
        os.path.join(home, "Pictures", "Screenshots"),
        os.path.join(home, "Imagens", "Capturas de tela"),
    ]
    
    origem = None
    for p in possible_origins:
        if os.path.exists(p):
            origem = p
            break
    
    # Fallback to the first one if none exist for reporting
    if not origem:
        origem = possible_origins[0]

    # Try common OneDrive and local paths for Destination
    possible_destinations = [
        os.path.join(home, "OneDrive", "Documentos", "Organizador_Lixeira"),
        os.path.join(home, "OneDrive", "Documents", "Organizador_Lixeira"),
        os.path.join(home, "Documentos", "Organizador_Lixeira"),
        os.path.join(home, "Documents", "Organizador_Lixeira"),
    ]
    
    destino = None
    for p in possible_destinations:
        # We check the parent directory (Documentos) existence 
        # to decide where to place the folder if it doesn't exist yet
        parent = os.path.dirname(p)
        if os.path.exists(parent):
            destino = p
            break
    
    if not destino:
        destino = possible_destinations[0]

    return origem, destino

PASTA_ORIGEM, PASTA_DESTINO = get_default_paths()

def organizar_prints():
    try:
        if not os.path.exists(PASTA_ORIGEM):
            print(f"A pasta de origem não existe: {PASTA_ORIGEM}")
            return
        
        if not os.path.exists(PASTA_DESTINO):
            os.makedirs(PASTA_DESTINO)
            print(f"Pasta de destino criada: {PASTA_DESTINO}")
        
        arquivos = os.listdir(PASTA_ORIGEM)
        arquivos_ordenados = 0
        
        for arquivo in arquivos:
            # Verifica extensões comuns de imagens
            if arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
                caminho_arquivo = os.path.join(PASTA_ORIGEM, arquivo)
                caminho_destino = os.path.join(PASTA_DESTINO, arquivo)
                
                # Move o arquivo
                try:
                    shutil.move(caminho_arquivo, caminho_destino)
                    arquivos_ordenados += 1
                    print(f"Arquivo movido: {arquivo}")
                except Exception as e_move:
                    print(f"Erro ao mover {arquivo}: {e_move}")
        
        print(f"Total de arquivos movidos: {arquivos_ordenados}")
    
    except Exception as e:
        print(f"Erro ao organizar prints: {e}")

if __name__ == "__main__":
    organizar_prints()
