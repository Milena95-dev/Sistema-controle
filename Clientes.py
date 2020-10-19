# -*- encoding: utf-8 -*-

def cadastrar_cliente():
    try:
      novo_cpf = input("Digite o CPF do Cliente: ")
      novo_nome = input("Digite o nome do Cliente: ")
      nova_idade = input("Digite a idade do Cliente: ")
      with open("clientes.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'CPF={}\n'.format(novo_cpf).casefold():
                  print('Já existe um cliente com o CPF {}'.format(novo_cpf))
                  return
          linhas.append("CPF={}\n".format(novo_cpf))
          linhas.append("Nome={}\n".format(novo_nome))
          linhas.append("Idade={}\n".format(nova_idade))
          arquivo = open("clientes.txt", 'w')
          arquivo.writelines(linhas)
          print("Cadastro de Cliente feito!")
          arquivo.close()
    except IOError as error:
        print("ERRO:", error)



def buscar_cliente(cpf):
    try:
        with open("clientes.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
               if linha.casefold() == 'CPF={}\n'.format(cpf).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos+1])
                    print(linhas[pos+2])
                    return
            print('Cliente não encontrado para busca')
    except IOError as error:
        print("ERRO:", error)


def editar_cliente(cpf):
    try:
        with open("clientes.txt", 'r+') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold() == 'CPF={}\n'.format(cpf).casefold():
                    pos = linhas.index(linha)
                    novo_cpf = input("Digite o novo cpf: ")
                    novo_nome = input("Digite o novo nome: ")
                    nova_idade = input("Digite a nova idade: ")

                    linhas.pop(pos)
                    linhas.pop(pos)
                    linhas.pop(pos)

                    linhas.append("CPF={}\n".format(novo_cpf))
                    linhas.append("Nome={}\n".format(novo_nome))
                    linhas.append("Idade={}\n".format(nova_idade))

                    arquivo = open("clientes.txt", 'w')
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print('Cliente alterado!')
                    return
            print('Cliente não encontrado para alteração')
    except IOError as error:
        print("ERRO:", error)


def excluir_cliente(cpf):
    try:
      with open("clientes.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'CPF={}\n'.format(cpf).casefold():
                  pos = linhas.index(linha)
                  linhas.pop(pos)
                  linhas.pop(pos)
                  linhas.pop(pos)

                  arquivo = open("clientes.txt", 'w')
                  arquivo.writelines(linhas)
                  print("Cliente excluído")
                  return
          print('Cliente não encontrado para exclusão')
    except IOError as error:
        print("ERRO:", error)


def copia_dados_dos_clientes():
    try:
        arquivo1clientes = open('clientes.txt', 'r')
        arquivo2clientes = open('cópia_de_dados_dos_clientes.txt', 'w')
        for texto in arquivo1clientes:
            arquivo2clientes.writelines(texto)
        arquivo1clientes.close()
        arquivo2clientes.close()
        print("Cópia de dados dos clientes feita.")
    except IOError as error:
        print("ERRO:", error)



