# -*- encoding: utf-8 -*-

def cadastrar_funcionario():
    try:
      novo_codigo = input("Digite o novo Código de funcionário: ")
      novo_nome = input("Digite o novo nome: ")
      with open("emissão.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'Código={}\n'.format(novo_codigo).casefold():
                  print('Já existe um produto com o código {}'.format(novo_codigo))
                  return

          linhas.append("Código={}\n".format(novo_codigo))
          linhas.append("Nome={}\n".format(novo_nome))

          arquivo = open("emissão.txt", 'w')
          arquivo.writelines(linhas)
          print('cadastro feito!')
          return
    except IOError as error:
        print("ERRO:", error)


def buscar_funcionario(codigo):
    try:
        with open("emissão.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos + 1])
                    arquivo.close()
                    return
            print('Funcionario não encontrado')
    except IOError as error:
        print("ERRO:", error)


def editar_funcionario(codigo):
    try:
        with open("emissão.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    novo_codigo = input("Digite o novo codigo: ")
                    novo_nome = input("Digite o novo nome: ")

                    linhas.pop(pos)
                    linhas.pop(pos)

                    linhas.append("Código={}\n".format(novo_codigo))
                    linhas.append("Nome={}\n".format(novo_nome))

                    arquivo = open("emissão.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Funcionário alterado!")
                    return
            print('Funcionário não encontrado')
    except IOError as error:
        print("ERRO:", error)


def excluir_funcionario(codigo):
    try:
        with open("emissão.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    linhas.pop(pos)
                    linhas.pop(pos)

                    arquivo = open("emissão.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Funcionário excluído")
                    arquivo.close()
                    return
            print('Funcionário não encontrado')
    except IOError as error:
        print("ERRO:", error)

def copia_dados_dos_funcionario():
    try:
        arquivo1funcionarios = open('emissão.txt', 'r')
        arquivo2funcionarios = open('cópia_de_dados_dos_funcionarios.txt', 'w')
        for texto in arquivo1funcionarios:
            arquivo2funcionarios.writelines(texto)
        arquivo1funcionarios.close()
        arquivo2funcionarios.close()
        print("Cópia de dados feita.")
    except IOError as error:
        print("ERRO:", error)



