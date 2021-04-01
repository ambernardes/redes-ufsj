# Sobre
Trabalho Prático de Redes de Computadores: Utilização da biblioteca Sockets em Python

O trabalho consiste no estudo e implementação de um cliente e servidor utilizando a biblioteca sockets
em Python. O aluno deverá acessar o link https://realpython.com/python-sockets/ , ler e executar todo o
tutorial do site. O tutorial explica o passo a passo de como realizar a comunicação entre cliente/servidor.
O aluno deverá executar os códigos em seu computador local seguindo os passos. No final do tutorial
existe um link disponibilizando todos os códigos no GitHub.

Após realizar o tutorial, o aluno deverá implementar uma iteração simples entre um cliente e servidor. O
servidor será visto como um banco de dados contendo informações sobre pessoas e o ciente irá fazer
cadastros e consultas ao banco de dados seguindo a sintaxe de comandos:

• Cadastro: “INSERT:$NOME:$SEXO:$IDADE”
• Consulta: “SELECT*”

Os comandos são digitados no terminal como texto. Ao digitar SELECT*, todos os cadastros do banco de
dados devem aparecer no terminal do cliente. Não é necessário criar um banco de dados real no servidor.
O banco de dados pode ser uma estrutura de dados (lista ou dicionário) em memória principal. Quando o
servidor parar de executar, os dados são perdidos. Lembrando que o nosso objetivo na disciplina é tratar
a comunicação e não o armazenamento de dados. 

# Tecnologias
- Python3
- Socket

# Execução
Você precisará ter o Python3 instalado em sua máquina.
Baixe o projeto na sua máquina, navegue até a pasta raíz do projeto.

Levante o servidor, executando o comando no terminal
> python3 echo_server.py
Em um outro terminal, levante a aplicação cliente, executando o comandondo
> python3 echo_client.py

Siga as intruções exibidas no terminal cliente.