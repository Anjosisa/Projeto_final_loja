from Classes import *

import os


def main():
    sair = False
    menu_adm = 0
    menu_cli = 0
    pdtID = 0
    contID = 0
    admID = 0

    while sair == False:
        menu_adm = 0
        loginCorreto = False
        try:
            os.system("cls")
            print(" --- BEM VINDO(A) AO VS STORE --- \n[1] - LOGIN ADM \n[2] - LOGIN CLIENTE \n[3] - SAIR")
            menu = int(input("\nDigite a opção desejada: "))
            os.system("cls")
                

            match menu:
                case 1:
                    print("--- ADM LOGIN ---")
                    user_login = input("Digite o user: ")
                    senha_login = input("Digite a senha: ")

                    for vetor, user in loja.adm.items():
                        if user.user == user_login and user.senha == senha_login:
                            loginCorreto = True

                    if loginCorreto == True:
                        os.system("cls")
                        
                        while menu_adm == 0:
                            print("--- MENU DO ADM --- \n[1] - CADASTRAR CLIENTE \n[2] - CADASTRAR ADM \n[3] - CADASTRAR PRODUTO \n[4] - EXCLUIR PRODUTO \n[5] - EXCLUIR CLIENTE \n[6] - LISTAR CLIENTE \n[7] - LISTAR PRODUTO \n[8] - VOLTAR")
                            op_adm = int(input("\nDigite a opção desejada: "))

                            match op_adm:
                                case 1:
                                    os.system("cls")
                                    contID += 1
                                    idc = contID
                                        
                                    print("--- CADASTRO DE CLIENTE --- \nPreencha as informações:\n")
                                    nome = input("NOME: ")
                                    cpf = int(input("CPF: "))
                                    idade = int(input("IDADE: "))
                                    endereco = input("ENDEREÇO: ")
                                    senha = input("SENHA: ")

                                    cliente = Cliente(nome, cpf, idade, endereco, senha, idc)
                                    loja.inserir_cliente(cliente, idc)
                                    print("\nCliente cadastrado com sucesso!\n")
                                    os.system("pause")
                                    os.system("cls")

                                case 2:
                                    os.system("cls")
                                    print("--- CADASTRO ADM--- \nPreencha as informações:\n")
                                    admID +=1
                                    ida = admID
                                        
                                    user = input("USER: ")
                                    senhaa = input("SENHA: ")

                                    adm = Adm(user, senhaa, 0)
                                    loja.inserir_adm(adm)
                                    print("\nADM cadastrado com sucesso!\n")
                                    os.system("pause")
                                    os.system("cls")


                                case 3:
                                    os.system("cls")
                                    pdtID += 1
                                    idp = pdtID
                                        
                                    print("--- CADASTRO DE PRODUTO --- \nPreencha as informações:\n")
                                    nome_produto = input("NOME DO PRODUTO: ")
                                    descricao = input("DESCRIÇÃO DO PRODUTO: ")
                                    valor = float(input("VALOR: "))
                                    qtd = int(input("QUANTIDADE: "))

                                    produto = Produto(nome_produto, descricao, valor, idp, qtd)
                                    loja.inserir_produto(produto, idp)
                                
                                    print("\nProduto cadastrado com sucesso!\n")
                                    os.system("pause")
                                    os.system("cls")

                                case 4:
                                    os.system("cls")
                                    print("---  EXCLUIR PRODUTO ---\n")
                                    loja.listarProdutos()
                                    excluir = int(input("\nDigite o ID do produto que deseja excluir: "))
                                    print("")
                                    os.system("pause")
                                    os.system("cls")
                                    
                                case 5:
                                    os.system("cls")
                                    print("---  EXCLUIR CLIENTE ---\n")
                                    loja.listarClientes()
                                    excluirc = int(input("Digite o ID do cliente que deseja excluir: "))
                                    loja.excluir_cliente(excluirc)
                                    print("")
                                    os.system("pause")
                                    os.system("cls")
                                case 6:
                                    os.system("cls")
                                    print("--- LISTA DE CLIENTES ---\n")
                                    loja.listarClientes()
                                    print("")
                                    os.system("pause")
                                    os.system("cls")
                                        
                                case 7:
                                    os.system("cls")
                                    print("--- LISTA DE PRODUTOS ---\n")
                                    loja.listarProdutos()
                                    print("")
                                    os.system("pause")
                                    os.system("cls")
                                case 8:
                                    os.system("cls")
                                    menu_adm = 1

                                case _:
                                    print("Opção inválida.")
                                    os.system("pause")
                                    os.system("cls")
                                
                    else:
                        print("Credenciais inválidas. Tente novamente.")
                case 2:
                    loginCorreto = False
                    os.system("cls")
                    print("--- LOGIN CLIENTE ---")
                    cpf_cliente = int(input("Digite o CPF: "))
                    senha_cliente = input("Digite a senha: ")

                    for vetor, cpf in loja.clientes.items():
                        if cpf.getCpf() == cpf_cliente and cpf.get_Senha() == senha_cliente:
                            LoginCorreto = True
                            cliente_atual = nome
                            print("")
                            os.system("pause")
                        
                        if LoginCorreto == True:
                            while menu_cli == 0:
                                os.system("cls")
                                print("--- MENU DO CLIENTE --- \n[1] - LISTA DE PRODUTOS \n[2] - ADICIONAR PRODUTO AO CARRINHO \n[3] - EXCLUIR PRODUTO DO CARRINHO \n[4] - MEU CARRINHO \n[5] - VOLTAR")
                                op_cli = int(input("\nDigite a opção desejada: ")) 

                            match op_cli:
                                case 1:
                                    pass

                                case 2:
                                    os.system("cls")
                                    loja.listarProdutos()
                                    vetor_produto = int(input("Digite o ID do produto que deseja adicionar ao carrinho: "))
                                    quantidade = int(input("Digite a quantidade desejada: "))
                                    cliente_atual.adicionar_ao_carrinho(vetor_produto, quantidade)
                                    os.system("pause")
                                    os.system("cls")
                                    
                                case 3:
                                    pass

                                case 4:
                                    
                                    pass

                                case 5:
                                    pass

                                case _:
                                    print("Opção inválida")
                                        
                case 3:  
                    sair = True
                        
                case _:
                    print("Opção inválida.")
                        
        except Exception as erro:
                print("Opção inválida.")
                print("Erro:", erro.__class__.__name__)
                os.system("pause")
                os.system("cls")


