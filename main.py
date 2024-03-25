import os
from subprocess import PIPE, run


def ChangeDirectory(comando): #  função para mudar o diretorio atual
  if len(comando) < 2:
    raise ValueError("Argumento de diretorio ausente")
  
  os.chdir(comando[1])
  print(f'Diretorio mudado para: {os.getcwd()}\n')

def RemoveDirectory(comando): #  função para remover algum diretorio
  if len(comando) < 2:
    raise ValueError("Argumento de diretorio ausente")

  os.rmdir(comando[1])
  print(f'Diretorio {comando[1]} removido\n')

def Manual(comando): #  comando para mostrar o manual de algum comando (man man)
  if len(comando) < 2:
    raise ValueError("Argumento de comando ausente")

  os.system(f'man {comando[1]}')

def pythonShell():
  while True:
    x = input(">>> ")
    if x == "exit":
      break

    try:
      y = eval(x)
      if y:
        print(y)
    except Exception:
      try:
        exec(x)
      except Exception as e:
        print("Erro:", e)
    

while True:
  DirAtual = os.getcwd() #  recupera o caminho do diretorio atual
  comando = input(f"C:{DirAtual}$ ").split() #  Recebe o comando e divide em argumentos

  if 'exit' in comando: # verifica se é um exit e sai
    print("finalizando...")
    break

  try:
    if comando[0] == 'cd':
      ChangeDirectory(comando) #  chama a função para mudar diretorio
    elif comando[0] == 'man':
      Manual(comando) # chama a função para mostrar o manual de algum comando
    elif comando[0] == 'rm':
      RemoveDirectory(comando) #  chama a função para remover diretorio
    elif comando[0] == 'clear':
      os.system('clear') #  limpa o terminal
    elif comando[0] == 'python' and len(comando) == 1:
      pythonShell() #  shell python interativo

    else:
      execucao = run(comando, stdout=PIPE, stderr=PIPE)
      print(execucao.stdout.decode('utf-8'))  

  except Exception as e:
    print(f'Erro de execução {e}')