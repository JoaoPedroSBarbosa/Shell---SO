import os
import sys


def main():
    while True:
        DirAtual = os.getcwd()
        print(f"\n{DirAtual}$ ", end="", flush=True)

        # Ler o comando digitado
        comando = input(f"{DirAtual}$ ").strip().split()

        if not comando:
            continue

        if comando[0] == 'exit':  # sai do loop
            break
        elif comando[0] == 'cd':  # muda o diretorio atual
            if len(comando) == 1:
                print("Uso: cd <diretório>", file=sys.stderr)
            else:
                try:
                    os.chdir(comando[1])
                except FileNotFoundError as e:
                    print(f"Erro ao alterar diretório: {e}", file=sys.stderr)
        else:
            pid = os.fork()

            if pid < 0:  # se o retorno for negativo é pq deu erro
                print("Erro ao criar processo filho", file=sys.stderr)
            elif pid == 0:  # processo filho é iniciado com 0
                try:
                    os.execvp(comando[0], comando)  # execução de comando por exemplo: mkdir e rmdir
                except FileNotFoundError as e:
                    print(f"Erro ao executar comando: {e}", file=sys.stderr)
                sys.exit(1)  # Em caso de falha na execução do comando
            else:
                os.waitpid(pid, 0)  # processo pai espera o filho ser encerrado


main()
