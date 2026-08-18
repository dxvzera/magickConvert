from pathlib import Path
import subprocess
import os, sys

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main():
    ogFile = input("Caminho do arquivo de origem: ").strip().strip('"').strip("'")
    path = Path(ogFile)

    if not path.exists():
        print("Arquivo nao encontrado.")
        return

    fileType = input("Digite o formato de saida: ").strip().lower()

    # formatos_validos = {"png", "jpg", "jpeg", "webp", "gif", "pdf", "bmp"}
    # if fileType not in formatos_validos:
    #     print("Formato invalido.")
    #     return

    if fileType == "jpeg":
        fileType = "jpg"

    finalFile = path.with_suffix(f".{fileType}")

    command = ["magick", str(path), str(finalFile)]

    try:
        subprocess.run(command, check=True)
        print(f"Conversao concluida: {finalFile}")
    except subprocess.CalledProcessError:
        print("Erro na conversao.")

    end = input("Deseja executar o programa novamente? (S/N): ")
    if end == 'n' or end == 'N':
        exit()
    elif end == 's' or end == 'S':
        restart()
    else:
        print("Opção inválida. Encerrando o programa.")
        exit()

if __name__ == "__main__":
    main()
