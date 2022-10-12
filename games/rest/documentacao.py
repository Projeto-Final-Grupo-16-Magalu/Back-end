DESCRICAO_CADASTRAR_CLIENTE = """
Cadastrar um novo cliente. Para cadastrar um novo cliente:</br>
    <li>-nome: Deve ter pelo menos um nome</br>
    <li>-email: Deve informar um email válido (ao menos 3 caracteres, conter um @).</br>
    *O email do cliente deve ser único*</br>
    <li>-senha: Deve informar uma senha</br>
    <br>
    Se o cadastro for realizado com *sucesso* a API retornará sucesso (código HTTP 201)</br>
e no corpo da resposta um registro com os campos cadastrados, além de um id criado pelo sistema.</br>
Se o cadastro apresentar *erro* a API retornará uma mensagem informando o tipo de erro."""


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
Se o cadastro apresentar *erro* a API retornará uma mensagem informando o tipo de erro.</br>""" 

DESCRICAO_PESQUISAR_ENDERECO = """
Pesquisar endereços de um cliente. Para pesquisar endereço pelo email do cliente:</br>
<li>-Passar o email do cliente</br>

Se a pesquisa for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma lista de endereços do cliente.</br>
Se o cadastro apresentar *erro* a API retornará uma mensagem informando o tipo de erro.</br>"""

DESCRICAO_DELETAR_ENDERECO = """
Deletar o endereço de um cliente. Para deletar o endereço pelo email do cliente:</br>
<li>-Passar o email do cliente</br>
<li>-Passar o id do endereço que se quer deletar</br>

Se a remoçao for realizada com *sucesso* a API retornará sucesso (código HTTP 200) e </br>
e no corpo da resposta uma mensagem ("Seu endereço foi removido com sucesso!).</br>
Se o cadastro apresentar *erro* a API retornará uma mensagem informando o tipo de erro.</br>""" 