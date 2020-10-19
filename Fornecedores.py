# -*- encoding: utf-8 -*-

def cadastrar_fornecedores():
    try:
      novo_codigo = input("Digite código do fonecedor para cadastro: ")
      novo_nome = input("Digite o nome da marca do fornecedor: ")
      with open("fornecedores.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'Código={}\n'.format(novo_codigo).casefold():
                  print('Já existe uma Marca com o código {}'.format(novo_codigo))
                  return

          linhas.append("Código={}\n".format(novo_codigo))
          linhas.append("Nome da Marca={}\n".format(novo_nome))

          arquivo = open("fornecedores.txt", 'w')
          arquivo.writelines(linhas)
          print('cadastro de fornecedor feito!')
          return
    except IOError as error:
        print("ERRO:", error)


def buscar_fornecedor(codigo):
    try:
        with open("fornecedores.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos + 1])
                    return
            print('Fornecedor não encontrado para busca')
    except IOError as error:
        print("ERRO:", error)

def editar_fornecedor(codigo):
    try:
        with open("fornecedores.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    novo_codigo = input("Digite o codigo do fornecedor a ser alterado: ")
                    novo_nome = input("Digite o nome da Marca do fornecedor: ")

                    linhas.pop(pos)
                    linhas.pop(pos)

                    linhas.append("Código={}\n".format(novo_codigo))
                    linhas.append("Nome da Marca={}\n".format(novo_nome))

                    arquivo = open("fornecedores.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Fornecedor alterado!")
                    return
            print('Fornecedor não encontrado para alteração')
    except IOError as error:
        print("ERRO:", error)


def excluir_fornecedor(codigo):
    try:
        with open("fornecedores.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    linhas.pop(pos)
                    linhas.pop(pos)

                    arquivo = open("fornecedores.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Fornecedor excluído")
                    return
            print('Fornecedor não encontrado para exclusão')
    except IOError as error:
        print("ERRO:", error)

def copia_dados_dos_fornecedor():
    try:
        arquivo1 = open('fornecedores.txt', 'r')
        arquivo2 = open('cópia_de_dados_dos_fornecedores.txt', 'w')
        for texto in arquivo1:
            arquivo2.writelines(texto)
        arquivo1.close()
        arquivo2.close()
        print("Cópia de dados dos fornecedores feita.")
    except IOError as error:
        print("ERRO:", error)