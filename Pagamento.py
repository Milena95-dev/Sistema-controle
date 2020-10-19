

def cadastrar_pagamento():
    try:
            novo_codigo = input("Digite o Código do produto: ")
            novo_nome = input("Digite o nome do cliente: ")
            pagamento = input("Digite o valor de pagamento: ")
            with open("emissão.txt", 'r+') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    if linha.casefold() == 'Código={}\n'.format(novo_codigo).casefold():
                        print('Já existe um produto com o código {}'.format(novo_codigo))
                        return

                linhas.append("Código={}\n".format(novo_codigo))
                linhas.append("Nome={}\n".format(novo_nome))
                linhas.append("Pagamento={}\n".format(pagamento))
                arquivo = open("emissão.txt", 'w')
                arquivo.writelines(linhas)
                print('Pagamento realizado!')
                return
    except IOError as error:
            print("ERRO:", error)


def conslultar_pagamento_NF(codigo):
    try:
        with open("emissão.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
               if linha.casefold() == 'Código={}\n'.format(codigo).casefold():
                    pos = linhas.index(linha)
                    print(linha)
                    print(linhas[pos+1])
                    print(linhas[pos+2])
                    return
            print('Pagamento não encontrado')
    except IOError as error:
        print("ERRO:", error)



