import os
from subprocess import PIPE, run


def MakeDirectory(comando):  # função para criar um diretorio
    if len(comando) < 2:
        raise ValueError("Argumento de diretorio ausente")

    os.mkdir(comando[1])
    print(f'Diretorio criado: {comando[1]}\n')


def ChangeDirectory(comando):  # função para mudar o diretorio atual
    if len(comando) < 2:
        raise ValueError("Argumento de diretorio ausente")

    os.chdir(comando[1])
    print(f'Diretorio mudado para: {os.getcwd()}\n')


def RemoveDirectory(comando):  # função para remover algum diretorio
    if len(comando) < 2:
        raise ValueError("Argumento de diretorio ausente")

    os.rmdir(comando[1])
    print(f'Diretorio {comando[1]} removido\n')


def ListFiles(comando):  # função para listar arquivos e diretórios
    if len(comando) > 1:
        caminho = comando[1]
    else:
        caminho = os.getcwd()

    try:
        arquivos = os.listdir(caminho)
        for arquivo in arquivos:
            print(arquivo)
    except FileNotFoundError:
        print(f'O diretório {caminho} não foi encontrado.')
    except PermissionError:
        print(f'Você não tem permissão para acessar o diretório {caminho}.')
    except Exception as e:
        print(f'Erro ao listar arquivos: {e}')


def clear():
    if os.name == 'nt':
        os.system('cls')  # para windows
    else:
        os.system('clear')  # para unix/linux


def RunPython(script_name):  # Função para executar um arquivo Python no diretório atual
    if os.path.isfile(script_name) and script_name.endswith('.py'):
        try:
            execucao = run(['python', script_name], stdout=PIPE, stderr=PIPE)
            print(execucao.stdout.decode('utf-8', errors='replace'))
            if execucao.stderr:
                print(execucao.stderr.decode('utf-8', errors='replace'))
        except Exception as e:
            print(f'Erro ao executar o codigo Python: {e}')
    else:
        print(f'O arquivo {script_name} não é um .py ou não existe.')


while True:
    DirAtual = os.getcwd()  # recupera o caminho do diretorio atual
    comando = input(f"C:{DirAtual}$ ").split()  # Recebe o comando e divide em argumentos

    if 'exit' in comando:  # verifica se é um exit e sai
        print("finalizando...")
        break

    try:
        if comando[0] == 'cd':
            ChangeDirectory(comando)  # chama a função para mudar diretorio
        elif comando[0] == 'rm':
            RemoveDirectory(comando)  # chama a função para remover diretorio
        elif comando[0] == 'clear':
            clear()  # limpa o terminal
        elif comando[0] == 'mk':
            MakeDirectory(comando)  # chama a função para criar diretorio
        elif comando[0] == 'ls':
            ListFiles(comando)  # chama a função para listar arquivos
        elif comando[0].endswith('.py'):
            RunPython(comando[0])  # chama a função para executar algum codigo Python

    except Exception as e:
        print(f'Erro de execução {e}')
