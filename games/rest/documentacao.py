##############################################################
#CLIENTES
##############################################################
DESCRICAO_CADASTRAR_CLIENTE = """
Cadastrar um novo cliente. Para cadastrar um novo cliente:</br>
    <li>-nome: Deve ter pelo menos um nome</br>
    <li>-email: Deve informar um email válido (ao menos 3 caracteres, conter um @).</br>
    *O email do cliente deve ser único*</br>
    <li>-senha: Deve informar uma senha</br>
    <br>
    Se o cadastro for realizado com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos cadastrados, além de um id criado pelo sistema.</br>
Se o cadastro não for efetivado um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_PESQUISAR_CLIENTES = """
Pesquisar todos os clientes.

Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma lista de clientes.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_PESQUISAR_CLIENTE_POR_EMAIL = """
Pesquisar cliente por email. Para pesquisar cliente por email:</br>
<li>-Passar o email do cliente</br>

Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta o cadastro requerido.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""


##############################################################
#ENDEREÇOS
##############################################################

DESCRICAO_CADASTRAR_ENDERECO = """
Cadastrar endereços para um cliente. Para cadastrar um novo endereço:</br>
<li>-logradouro: Deve ter pelo menos um nome.</br>
<li>-CEP: Deve ter pelo menos um CEP válido.</br>
<li>-bairro: Deve ter pelo menos um nome.</br>
<li>-cidade: Deve ter pelo menos um nome.</br>
<li>-estado: Deve ter pelo menos um nome.</br>
<li>-numero: Deve ter pelo menos um número válido ou sem numero.</br>
Um mesmo endereço pode ser cadastrado para mais de um cliente e um cliente pode ter vários endereços.</br>
Se o cadastro for realizado com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos cadastrados, além de um id para aquele endereço criado pelo sistema.</br>
Se o cadastro não for efetivado um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>""" 

DESCRICAO_PESQUISAR_ENDERECO = """
Pesquisar endereços de um cliente. Para pesquisar endereço pelo email do cliente:</br>
<li>-Passar o email do cliente</br>

Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma lista de endereços do cliente.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_DELETAR_ENDERECO = """
Deletar o endereço de um cliente. Para deletar o endereço pelo email do cliente:</br>
<li>-Passar o email do cliente</br>
<li>-Passar o id do endereço que se quer deletar</br>

Se a remoçao for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma mensagem ("Seu endereço foi removido com sucesso!).</br>
Se a remoçao não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>""" 

##############################################################
#CARRINHO
##############################################################

DESCRICAO_CRIAR_CARRINHO_ABERTO = """
Criar um carrinho aberto. Para criar um carrinho aberto:</br>
    <li>-nome: Deve ter um cliente</br>
    <li>-produto: Inicia com a lista de produtos vazia</br>
    *Cada cliente só pode ter um carrinho*</br>
Se o carrinho for criado com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos do carrinho, além de um id criado pelo sistema.</br>
Se a criação do carrinho não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

ADICIONAR_ITEM_CARRINHO_ABERTO = """
Adicionar um item a um carrinho aberto. Para adicionar um item a um carrinho aberto:</br>
    <li>-produto: Informa o produto que será adicionado</br>
    <li>-quantidade: Informa a quantidade desse produto que será comprada</br>
    <li>-valor: Atualiza o valor do produto em relação à quantidade</br>
Se o item for adicionado com *sucesso* a API retornará sucesso (código HTTP 200)</br>
Se o item não conseguir ser adicionado no carrinho um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_FECHAR_CARRINHO_ABERTO = """
Fechar um carrinho aberto para um cliente. Para fechar um carrinho aberto:</br>
    <li>-Passar o email do cliente</br>
   
Se o carrinho for fechado com *sucesso* a API retornará sucesso (código HTTP 200)</br>
e no corpo da resposta um registro com os campos do carrinho, além de um id criado pelo sistema.</br>
Se o carrinho não conseguir ser fechado um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_REMOVER_CARRINHO_ABERTO = """
Remover um carrinho aberto para um cliente. Para remover um carrinho aberto:</br>
    <li>-Passar o email do cliente</br>
   
Se o carrinho for removido com *sucesso* a API retornará sucesso (código HTTP 200)</br>
Se o carrinho não conseguir ser removido um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_PESQUISAR_CARRINHO_ABERTO ="""
Pesquisar um carrinho aberto para um cliente. Para pesquisar um carrinho aberto:</br>
    <li>-Passar o email do cliente</br>
   
Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta o carrinho aberto do cliente.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_PESQUISAR_CARRINHOS_FECHADOS = """
Pesquisar os carrinhos fechados de um cliente. Para pesquisar os carrinhos fechados:</br>
    <li>-Passar o email do cliente</br>
   
Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta o carrinho aberto do cliente.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

##############################################################
#PRODUTOS
##############################################################

DESCRICAO_CADASTRAR_PRODUTO = """
Cadastrar um novo produto. Para cadastrar um novo produto:</br>
    <li>-nome: Deve ter pelo menos um nome</br>
    *O nome do produto deve ser único*</br>
    <li>-descrição: Descrição sobre o produto.</br>
    <li>-tipo: Descrição sobre o tipo do produto.</br>
    <li>-plataforma: Tipo de plataforma do produto</br>
    <li>-preço: Preço do produto > R$0,01</br>
    <li>-quantidade em estoque: Quantidade de produtos em estoque</br>
    <li>-código: Codigo único para o produto</br>
    <li>-imagem: Opcional</br>
    <br>
    
Se o cadastro for realizado com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos cadastrados, além de um id criado pelo sistema.</br>
Se o cadastro não for efetivado um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_ATUALIZAR_DADOS_PRODUTO = """
Atualizar dados de um produto. Para atualizar dados de um produto, passar os dados que serão atualizados:</br>
    <li>-nome: Deve ter pelo menos um nome</br>
    *O nome do produto deve ser único*</br>
    <li>-descrição: Descrição sobre o produto.</br>
    <li>-plataforma: Tipo de plataforma do produto</br>
    <li>-preço: Preço do produto > R$0,01</br>
    <li>-quantidade em estoque: Quantidade de produtos em estoque</br>
    <li>-imagem: Opcional</br>
    <br>
    
Se a atualização for realizada com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos cadastrados, além de um id criado pelo sistema.</br>
Se a atualização não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro."""

DESCRICAO_PESQUISAR_PRODUTO_ID = """
Pesquisar produtos pelo Id. Para pesquisar produto pelo id do produto 
<li>-Passar o id do produto</br>
   
Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta o produto.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_PESQUISAR_PRODUTO_NOME = """
Pesquisar produtos pelo nome do produto. Para pesquisar produto pelo nome do produto 
<li>-Passar o nome do produto</br>
   
Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta o produto.</br>
Se a pesquisa não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_REMOVER_PRODUTO = """
Deletar um produto. Para deletar um produto pelo id do produto:</br>
<li>-Passar o id do produto que se quer deletar</br>

Se a remoçao for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma mensagem ("Produto removido com sucesso!).</br>
Se a remoçao não for efetivada um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.</br>"""

##############################################################
#PRINCIPAL
##############################################################

DESCRICAO_PRINCIPAL = """
Rota de verificação da aplicação web.
Se a API estiver funcionando com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta uma mensagem de *Oi*.</br>
Se a API não estiver funcionando um *erro* será apresentado e a API retornará uma mensagem informando o tipo de erro.""" 