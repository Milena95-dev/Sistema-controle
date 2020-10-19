# -*- encoding: utf-8 -*-


import Clientes as clientes
import Produtos as produtos
import Funcionarios as funcionarios
import Fornecedores as fornecedores
import Pagamento as pagamento

def cabecalho():
    print("*" * 16, "FACULDADE CESUSC", "*" * 16)
    print("* Curso: Análise e Desenvolvimento de Sistemas    *")
    print("* Aluno: Milena Pereira Torres ")
    print("* Professor: Roberto Fabiano Fernandes      *")
    print("*" * 40)

def menu():
    print("""Escolha a opção:
            CLIENTES
          1 - Cadastrar Clientes
          2 - Listar Clientes
          3 - Alterar dados dos Clientes
          4 - Excluir Clientes
          5 - Realizar Cópia do arquivo dos Clientes
            PRODUTOS
          6-  Cadastrar de produtos
          7-  Consultar Produtos
          8-  Mudar Produtos
          9-  Deletar Produtos
          10- Copiar dados dos Produtos
            FUNCIONÁRIOS
          11- Cadastrar de Funcionários
          12- Consultar de Funcionários
          13- Alterar Funcionários
          14- Excluir Funcionários
          15- Copiar dados dos Funcionários
            FORNECEDORES
          16- Cadastrar de Fornecedores
          17- Buscar de dados dos Fornecedores
          18- Alteração de Fornecedores
          19- Excluir Fornecedores
          20- Copiar dados dos Fornecedores
          21 - Cadastrar pagamento
          22- Consultar pagamento e emissão de nota fiscal
          0 - Sair"
          Digite a opção escolhida: """)
    return input()

def menu_opcoes():
    while True:
            opcao = menu()
            if opcao == '1':
                clientes.cadastrar_cliente()
                menu_opcoes()
            elif opcao == '2':
                cpf = input("digite o CPF do cliente para buscar: ")
                clientes.buscar_cliente(cpf)
                menu_opcoes()
            elif opcao == '3':
                cpf = input("digite o CPF do cliente para alteração: ")
                clientes.editar_cliente(cpf)
                menu_opcoes()
            elif opcao == '4':
                cpf = input("digite o CPF do cliente para excluir: ")
                clientes.excluir_cliente(cpf)
                menu_opcoes()
            elif opcao == '5':
                clientes.copia_dados_dos_clientes()
                menu_opcoes()
            elif opcao == '6':
                produtos.cadastrar_produto()
            elif opcao == '7':
                codigo = input("Digite o Código do Produto que deseja buscar: ")
                produtos.buscar_produto(codigo)
                menu_opcoes()
            elif opcao == '8':
                codigo = input("Digite o Código do Produto que deseja alterar: ")
                produtos.editar_produto(codigo)
                menu_opcoes()
            elif opcao == '9':
                codigo = input("Digite o Código do Produto que deseja excluir: ")
                produtos.excluir_produto(codigo)
                menu_opcoes()
            elif opcao == '10':
                produtos.copia_dados_dos_produtos()
                menu_opcoes()
            elif opcao == '11':
                funcionarios.cadastrar_funcionario()
                menu_opcoes()
            elif opcao == '12':
                codigo = input("Digite o Código do Funcionário que deseja consultar: ")
                funcionarios.buscar_funcionario(codigo)
                menu_opcoes()
            elif opcao == '13':
                codigo = input("Digite o Código do Funcionário que deseja alterar: ")
                funcionarios.editar_funcionario(codigo)
                menu_opcoes()
            elif opcao == '14':
                codigo = input("Digite o Código do Funcionário que deseja excluir:  ")
                funcionarios.excluir_funcionario(codigo)
                menu_opcoes()
            elif opcao == '15':
                funcionarios.copia_dados_dos_funcionario()
                menu_opcoes()
            elif opcao == '16':
                fornecedores.cadastrar_fornecedores()
                menu_opcoes()
            elif opcao == '17':
                codigo= input("Digite o código da Marca do fornecedor que deseja buscar: ")
                fornecedores.buscar_fornecedor(codigo)
                menu_opcoes()
            elif opcao == '18':
                codigo = input("Digite o código da Marca do fornecedor que deseja alterar: ")
                fornecedores.editar_fornecedor(codigo)
                menu_opcoes()
            elif opcao == '19':
                codigo= input("Digite o código da Marca do fornecedor que deseja excluir: ")
                fornecedores.excluir_fornecedor(codigo)
                menu_opcoes()
            elif opcao == '20':
                fornecedores.copia_dados_dos_fornecedor()
                menu_opcoes()
            elif opcao == '21':
                pagamento.cadastrar_pagamento()
                menu_opcoes()
            elif opcao == '22':
                codigo = input("Digite o código para verificar o pagamento: ")
                pagamento.conslultar_pagamento_NF(codigo)
                menu_opcoes()
            else:
                print("Programa Encerrado.")
                break


cabecalho()
menu_opcoes()
