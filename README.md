<h1 align="center">
   <a><img src="https://github.com/Projeto-Final-Grupo-16-Magalu/Back-end/blob/4214bdb4095a4e60d6017d8cacad97620c2487fd/luizagamerreadme.gif" alt="Carrinho de compras em Python Luiza: loja de jogos eletrônicos e videogames<code>" style="max-width: 80%;"></a>
</h1>

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>

> **Esse projeto está em fase de desenvolvimento e será atualizado a cada semana. Entrega final prevista para: 12/10/2022

## :pushpin:*Título*
 <h1 align="center">Carrinho de compras em Python Luiza: loja de jogos eletrônicos e videogames</h1>


## :pushpin:*Descrição do Projeto*

Projeto em desenvolvimento para o programa de formação em tecnologia, exclusivo para mulheres, Luizacode do Luizalabs, criado pelo Magalu. 

O objetivo desse projeto é aplicar os conhecimentos adquiridos no programa, focado em Python e desenvolvimento backend, para criar um conjunto de APIs REST para um carrinho de compras de uma loja de jogos eletrônicos e videogames.

## :hammer:*funcionalidades do projeto*

Funcionalidade 1: Clientes:
   -Cadastrar/Atualizar/Remover um cliente
   -Cadastrar/Atualizar/Remover endereços para o cliente cadastrado
   -Pesquisar um cliente
   -Pesquisar os endereços de um cliente pelo seu e-mail cadastrado
   
Funcionalidade 2: Produtos:
   -Cadastrar/Atualizar/Remover um produto
   -Pesquisar um produto pelo código ou pelo nome
  
Funcionalidade 3: Carrinho de compras:
   -Aberto: O cliente pode ter apenas um carrinho de compras aberto para adicionar produtos, alterar a quantidade de itens de um produto e consultar o conteúdo do carrinho. Além disso, é possível fechar o carrinho aberto ou removê-lo.
   -Fechado: Consultar os carrinhos fechados e a quantidade deles, consultar os produtos dentro de cada carrinho fechado. 


## :computer:*Tecnologias utilizadas*

Nesse projeto foram usadas as seguintes tecnologias:

### Linguagem de programação: Python 3.10 
### Bibliotecas: 
- 
- [fastapi](https://fastapi.tiangolo.com/),
- [uvicorn](https://www.uvicorn.org/),
- [motor](https://motor.readthedocs.io/en/stable/).
- [pymongo](https://pypi.org/project/pymongo/)
- [pydantic](https://pypi.org/project/pydantic/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) 
- [PyJWT](https://pypi.org/project/PyJWT/)
- [typing](https://pypi.org/project/typing/)   
- [decimal](https://github.com/python/cpython/blob/3.10/Lib/decimal.py)
- [datetime](https://pypi.org/project/DateTime/)
- [bson](https://github.com/py-bson/bson)
- [logging](https://pypi.org/project/logging/)

### Protocolos HTTP
### Aplicações usadas:
- Visual Studio Code
- Testes: REST Client for Visual Studio Code
### Materiais
- [pip](https://pip.pypa.io/en/stable/getting-started/).
- [venv](https://docs.python.org/pt-br/3/library/venv.html).
- API REST, documento da :
  - [Red Hat](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api).
  - [AWS](https://aws.amazon.com/pt/what-is/restful-api/).
- [FastAPI](https://fastapi.tiangolo.com/).

## :file_folder:*Acesso ao projeto*

Você pode [acessar o código fonte do projeto]([https://github.com/dsamandarc/projetocarrinho](https://github.com/dsamandarc/carrinhogrupo18)) ou [baixá-lo](https://github.com/dsamandarc/carrinhogrupo18/archive/refs/heads/main.zip).

## :electric_plug:*Para começar:*

- É necessário ter instalado o Python 3.10 e Visual Studio Code 

- Baixar os arquivos do projeto com:
```
git clone https://github.com/Projeto-Final-Grupo-16-Magalu/Back-end.git
```
- Entrar na pasta do projeto:
```
cd Back-end
```
## :clipboard:*Etapas para *
Temos uma estrutura separada para cada requisito funcional da aplicação: -Clientes, Endereços, Produtos e Carrinho
### [Etapa A]: Criação do ambiente virtual Python e carregar pacotes que serão usados:
   
Para começar a rodar a aplicação,criamos um ambiente virtual do Python ([venv](https://docs.python.org/pt-br/3/library/venv.html)).
Para isso é preciso:
#### Entrar na pasta da aplicação e criar o ambiente:
Entrar na pasta ´Back-end´:

```
cd Back-end
```

Criando o ambiente virtual no Linux, usando o Python 3.9:

```
python3.9 -m venv venv
```

Criando o ambiente virtual no Windows, usando o Python 3.9, no Prompt de Comando:

```
python -m venv venv
```
#### Ativar o ambiente virtual venv:
Para _ativar_ o ambiente virtual no Linux:

```
source venv/bin/activate
```

E no Windows:

```
venv\Scripts\activate
```
#### Istalar os pacotes no ambiente virtual:
Criamos o arquivo requerimentos.txt, que contém todos os pacotes do Pyhton necessários para a aplicação, nas versões usadas para desenvolvê-la.
Instalando os pacotes necessários para projeto:

```
pip install -r requerimentos.txt
```

### [Etapa B]: Testando a API
### Executando o servidor no ambiente virtual

Para executar o servidor FastAPI:

```sh
uvicorn  games.aplicacao:app --reload
```

### Acessando a aplicação

Teste a aplicação ao acessar: 

> http://localhost:8000

Ela irá lhe dizer um "`Oi`".
### [Etapa C]: Organizando a aplicação.

Organizamos nossa aplicação por estruturá-la em vários módulos e pacotes do Python.
Para fins didáticos, iremos ter as seguintes pastas:

- [games]: Pasta principal da aplicação. 
  - [persistencia]: Módulo para persistência (repositório) com o banco de dados.
  - [regras]: Módulos para as regras (casos de uso) da aplicação.
  - [rest]: Módulos para de _controle_ e/ou _comunicação_ com o FastAPI.

Dentro desses diretórios iremos ter estes arquivos:
- [modelos]: Modelos para as classes
- [aplicacao.py]: Arquivo principal do projeto. Vamos dizer que a aplicação FastAPI _inicia_ aqui. Configurações com o FastAPI.
- [configuracoes.py]: Configurações gerais da aplicação.
- [rest]: Rotas para cada caminho de URL "`/`".
- [regras](./musicas/regras/musicas_regras.py): Regras para o funcionamento da API
- [persistencia]: Responsável pela persistência da API

Logo, navegue pelos arquivos e acesse as funcionalidades.

## :woman:*Desenvolvedoras*

[<img src="https://media-exp1.licdn.com/dms/image/C4D03AQFBFaZ09QRqeA/profile-displayphoto-shrink_200_200/0/1659111454432?e=1670457600&v=beta&t=cS-vd8IRIBh8QKns3tklDG9TJlY0msAqCTkp1R4l-A4" width=115 > <br> <sub> Amanda (Jones) Oliveira </sub>](https://www.linkedin.com/in/amanda-oliveira-jones/) 
<br>
[![Gmail](https://img.shields.io/badge/Email-amandaoliveirajones@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:amandaoliveirajones@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-amandaoliveirajones-informational?style=flat-square&logo=linkedin&logoColor=white)](linkedin.com/in/amanda-oliveira-jones/)
<br>
<br>
[<img src="https://media-exp1.licdn.com/dms/image/D4D35AQGFY_w5bsKJdQ/profile-framedphoto-shrink_200_200/0/1654617757807?e=1666717200&v=beta&t=SPwtveHKqUZjrx8MUqQMrcAek3uUNuYEzIsC3hgGtxI" width=115 > <br> <sub> Amanda Rodrigues Cruz </sub>](https://www.linkedin.com/in/amandarodriguescruz/)
<br>
[![Gmail](https://img.shields.io/badge/Email-amandinharodriguescruz@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:amandinharodriguescruz@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-amandarodriguescruz-informational?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amandarodriguescruz/)
<br>
<br>
[<img src="https://avatars.githubusercontent.com/u/4570617?v=4" width=115 > <br> <sub> Camila Katheryne </sub>](https://github.com/camilakatheryne) 
<br>
[![Gmail](https://img.shields.io/badge/Email-camila.katheryne@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:camila.katheryne@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-camilacangussu-informational?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/camila-cangussu-188b54160/)
<br>
<br>
[<img src="https://media-exp1.licdn.com/dms/image/C4D03AQEc-_WYQG_UgQ/profile-displayphoto-shrink_200_200/0/1659385910410?e=1670457600&v=beta&t=wF5TTSpdqKqon4l3i1r0p64eDJibqzM0s8yHZfOXKYo" width=115 > <br> <sub> Caroline Melo </sub>](https://www.linkedin.com/in/carolinemelo-dev/) 
<br>
[![Gmail](https://img.shields.io/badge/Email-stefani.uffs@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:stefani.uffs@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-carolinemelo-informational?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carolinemelo-dev/)
<br>
<br>
[<img src="https://media-exp1.licdn.com/dms/image/C4D03AQEPMCS_0rk06Q/profile-displayphoto-shrink_200_200/0/1641747392936?e=1670457600&v=beta&t=Q-Y8LCPRJoNsApZ8EF5iD9m8Mws31LMMwUrcfXmMszA" width=115 > <br> <sub> Jaqueline Rocha </sub>](https://www.linkedin.com/in/jaquelinerochao/) 
<br>
[![Gmail](https://img.shields.io/badge/Email-jaquerotero@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:jaquerotero@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jaquelinerochao-informational?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaquelinerochao/)
<br>
<br>
[<img src="https://avatars.githubusercontent.com/u/104438961?v=4" width=115 > <br> <sub> Nayara Lelis </sub>](https://www.linkedin.com/in/nayaralelis/) 
<br>
[![Gmail](https://img.shields.io/badge/Email-contato.naayalelis@gmail.com-informational?style=flat-square&color=8B89CC&logo=protonmail&logoColor=white)](malito:contato.naayalelis@gmail.com)
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-nayaralelis-informational?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nayaralelis/)
## :memo:*Licença*

Carrinho de compras em Python Luizacode é [MIT licensed](./LICENSE).

A documentação do Carrinho de compras em Python Luizacode é [Creative Commons licensed](./LICENSE-docs)

## :blue_heart:*Agradecimentos especiais*

<img src="https://github.com/Projeto-Final-Grupo-16-Magalu/Back-end/blob/0950afd9c72dc3f630416043c46c850928e6b7a2/extras/luizalabs%20logo.png" width=115 > <br> 
[[LuizaLabs]](https://medium.com/luizalabs) que ofereceu por meio do Luiza code (programa de formação em tecnologia) - 5ª edição todo conhecimento necessário para a construção desse carrinho. À todos os nossos professores, mentores, madrinhas e a Taci nosso muito obrigada! 
