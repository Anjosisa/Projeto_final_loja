class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm
    
    def getUser(self):
        return self.user
    def getSenha(self):
        return self.senha
    def getIDadm(self):
        return self.id_adm
    
    def cadastrar_adm(self, user, senha):
        adm = Adm(user, senha)
        loja.inserir_adm(adm)

    
class Cliente:
    def __init__(self, nome, cpf, idade, endereço, senha, idc):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereço
        self.senhacli = senha
        self.id = idc
        self.carrinho = []
    
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCpf(self):
        return self.cpf

    def getEndereco(self):
        return self.endereco

    def get_Senha(self):
        return self.senhacli

    def getId(self):
        return self.id

    


class Produto:
    def __init__(self, nome_produto, descricao, valor, idp, qtd):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.idp = idp
        self.qtd = qtd

    def get_nome_produto(self):
        return self.nome_produto

    def get_descricao(self):
        return self.descricao

    def get_valor(self):
        return self.valor

    def get_idp(self):
        return self.idp

    def getQTd(self):
        return self.qtdp
    
    def setQtd(self, new_qtd):
        self.qtd = new_qtd


class Loja:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome 
        self.endereco = endereco
        self.cnpj = cnpj
        self.adm = {}
        self.produtos = {}
        self.clientes = {}
    
    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

    def get_cnpj(self):
        return self.cnpj

    def inserir_cliente(self, valor, vetor):
        self.clientes[vetor] = valor
    
    def inserir_produto(self, valor, vetor):
        self.produtos[vetor] = valor

    def inserir_adm(self, valor):
        vetor = len(self.adm) + 1
        self.adm[vetor] = valor

    def listarClientes(self):
        for chave, cliente in self.clientes.items():
            print(f"ID:{chave} - Nome: {cliente.getNome()} - CPF: {cliente.getCpf()} - Idade: {cliente.getIdade()} - Endereço: {cliente.getEndereco()}")

    def listarProdutos(self):
        for chave, produto in self.produtos.items():
            print(f"ID:{chave} - Nome: {produto.get_nome_produto()} - Descrição: {produto.get_descricao()} - Valor: R${produto.get_valor()}")
    
    def excluir_produto(self, vetor):
        self.vetor = vetor-1
        return self.produtos.pop(vetor)

    def excluir_cliente(self, vetorc):
        self.vetorc = vetorc-1
        return self.clientes.pop(vetorc)
    
    def adicionar_ao_carrinho(self, produto, qtd):
        self.produto = produto
        self.qtdp = qtd
        self.lista_compra.append(self.produto)
        print(f"{produto.get_nome_produto()} foi adicionado ao carrinho.")

    def listar_produtos(self):
        cont = 0
        if len(self.carrinho) == 0:
            print("Seu carrinho está vazio.")
        else:
            print("Itens no carrinho:\n")
            for produto in self.carrinho:
                cont += 1
                print(f"Nome: {produto.get_nome_produto()} | Valor: R${produto.get_valor()}")
        

    def getLista(self, vetor):
        return self.lista_compra[vetor]

    def delProduto(self, vetor):
        self.vetor_lista = vetor - 1
        self.lista_compra.pop(self.vetor_lista)
    


loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
master = Adm("adm", "admin123",0)
loja.inserir_adm(master)