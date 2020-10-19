pagamento = 0
def cadastrar_pagamento():
    try:
      pagamento = input("Digite a quantia de pagamento: ")
      cliente_nome = input("Nome do cliente para nota fiscal: ")
      with open("emissão.txt", 'r+') as arquivo:
          linhas = arquivo.readlines()
          for linha in linhas:
              if linha.casefold() == 'CPF={}\n'.format(pagamento).casefold():
                  print('Já existe um cliente com o CPF {}'.format(pagamento))
                  return
          linhas.append("CPF={}\n".format(pagamento))
          linhas.append("Nome={}\n".format(cliente_nome))
          arquivo = open("emissão.txt", 'w')
          arquivo.writelines(linhas)
          print("Pagamento feito!")
          arquivo.close()
    except IOError as error:
        print("ERRO:", error)


def consultar_pagamento(pagamento):
    try:
        with open("emissão.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
               if linha.casefold() == 'Pagamento={}\n'.format(pagamento).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos+1])
                    print(linhas[pos+2])
                    return
            print('Cliente não encontrado para busca')
    except IOError as error:
        print("ERRO:", error)

def emissão_nota_fiscal():
    with open ('emissão.txt', 'r') as arquivo:
        arquivo.readlines()
        arquivo.close()
    return


cadastrar_pagamento()
consultar_pagamento(pagamento)
emissão_nota_fiscal()

