# PF_Ecommerce

---

**Tema do E-commerce:** Venda de produtos diversos

*Nosso E-commerce foi criado com o intuito de ser um local de Venda de produtos.*

Serão necessárias cinco classes:

## Classe Loja

- Atributos: Nome, Endereço e CNPJ
    
    <aside>
    - Para cadastrar a loja, foi passado informações como o nome da loja, o endereço da loja e seu CNPJ.
    
    </aside>
    
- Métodos: Dicionários de Cliente, Produto e ADMs.

---

## Classe Cliente

- Atributos: Nome, Data de Nascimento, CPF, Endereço e Senha.
    
    <aside>
    - Para cadastrar os clientes, foram passados o nome do cliente, sua data de nascimento, seu CPF, endereço e senha para login.
    
    </aside>
    
- Métodos: Dicionário de Adicionar Produto e a parte de Excluir Produto.

## Classe Produto

- Atributos: Nome, Descrição e Valor.
    - A partir dessa classe que os produtos podem ser criados.
    
    <aside>
    - Passando informações como o nome do produto, sua descrição e seu valor
    
    </aside>
    

## Classe ADM

- Atributos: User, Senha.
    
    <aside>
    - São passados user e senha para os ADMs poderem entrar no sistema da loja.
    
    </aside>
    
- Métodos: Cadastrar Cliente, Cadastrar ADM, Cadastrar Produto, Excluir Produto, Excluir Cliente, Excluir ADM, Listar Produtos, Listar Clientes, Listar ADMs.
    
    <aside>
    - Algumas das funções que o ADM pode executar são essas.
    
    </aside>
    

## Classe Carrinho

- Atributos: Nome, Valor, Descrição.
    
    <aside>
    - Aqui será armazenado os produtos que serão comprados pelo cliente
    
    </aside>
    

O projeto é baseado em três interfaces:

- **Tela 1:**
    - 01 → Login ADM
    - 02 → Login Cliente
    
    <aside>
    - A Tela 1 é onde fica o login do usuário e do ADM
    
    </aside>
    
- **Tela 2 (Login ADM):**
    - 01 → Cadastrar Cliente
    - 02 → Cadastrar ADM
    - 03 → Cadastrar Produto
    - 04 → Excluir Produto
    - 05 → Excluir Cliente
    - 06 → Listar Clientes
    - 07 → Listar Produtos
    
    <aside>
    - A Tela 2 é onde fica o menu do ADM, que é acessada, onde mostra as funções que ele pode executar como:
    
    <aside>
    - Cadastrar clientes, ADMs e os produtos, além de excluir os clientes e os produtos, e lista-los
    
    </aside>
    
    </aside>
    
- **Tela 3 (Login Cliente):**
    - 01 → Adicionar Produto
    - 02 → Excluir Produto
    - 03 → Listar Produtos
    - 04 → Ver Carrinho

<aside>
- A Tela 3 é onde fica o menu do cliente, que é acessada após o login, onde mostra as funções que ele pode executar como:

<aside>
- Adicionar um produto ao carrinho, tirar ele do carrinho, listar os produtos disponíveis e ver o carrinho

</aside>

</aside>

## Relatório

No Relatório será feito um registro de todas as compras do Cliente e mostradas em uma lista, assim como as vendas da loja que  irá mostrar o registro de todas as vendas realizadas na loja.