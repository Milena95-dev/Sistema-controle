# -*- encoding: utf-8 -*-

def cadastrar_produto():
    try:
      novo_codigo = input("Digite o codigo de produto: ")
      novo_nome = input("Digite o nome do produto: ")
      with open("produtos.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'Código={}\n'.format(novo_codigo).casefold():
                  print('Já existe um produto com este código {}'.format(novo_codigo))
                  return

          linhas.append("Código={}\n".format(novo_codigo))
          linhas.append("Nome={}\n".format(novo_nome))

          arquivo = open("produtos.txt", 'w')
          arquivo.writelines(linhas)
          print('cadastro de produto feito!')
          return
    except IOError as error:
        print("ERRO:", error)


def buscar_produto(codigo):
    try:
        with open("produtos.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos + 1])
                    return
            print('Produto não encontrado para busca')
    except IOError as error:
        print("ERRO:", error)


def editar_produto(codigo):
    try:
        with open("produtos.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    novo_codigo = input("Digite o codigo do produto para alteração: ")
                    novo_nome = input("Digite o nome do produto novo: ")

                    linhas.pop(pos)
                    linhas.pop(pos)

                    linhas.append("Código={}\n".format(novo_codigo))
                    linhas.append("Nome={}\n".format(novo_nome))

                    arquivo = open("produtos.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Produto alterado!")
                    return
            print('Produto não encontrado para alteração')
    except IOError as error:
        print("ERRO:", error)


def excluir_produto(codigo):
    try:
        with open("produtos.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    linhas.pop(pos)
                    linhas.pop(pos)

                    arquivo = open("produtos.txt", 'w')
                    arquivo.writelines(linhas)
                    print("Produto excluído")
                    return
            print('Produto não encontrado para exclusão')
    except IOError as error:
        print("ERRO:", error)

def copia_dados_dos_produtos():
    try:
        arquivo1produtos = open('produtos.txt', 'r')
        arquivo2produtos = open('cópia_de_dados_dos_produtos.txt', 'w')
        for texto in arquivo1produtos:
            arquivo2produtos.writelines(texto)
        arquivo1produtos.close()
        arquivo2produtos.close()
        print("Cópia de dados dos produtos feita.")
    except IOError as error:
        print("ERRO:", error)