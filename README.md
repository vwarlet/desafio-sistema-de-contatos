# Desafio: Sistema de contatos 
 
O desafio abaixo pode ser realizado em qualquer linguagem e/ou ferramenta. A entrega do desafio deve ser feita via repositório público GIT. Se não for possível concluir, enviar o que foi feito. Este desafio não é eliminatório, apenas para nivelamento. Utilize os recursos que preferir. 
 
### História:
Como coordenador de desenvolvimento, eu quero armazenar os cartões que de contatos que recebo dos fornecedores, para que eu não perca os contatos e não tenha que ficar com os cartões físicos; 
 
### Conversa:
A ideia seria ter uma lista de contatos categorizada, onde fosse possível adicionar novos contatos e categorizá-los por tipo de empresa e assunto. Pode ser uma tela única, que me permite buscar um contato e incluir novos. 
 
### Confirmação:
Dado que acessei o sistema de contatos Quando eu clicar na ação Carregar Eu quero que os contatos armazenados sejam carregados em forma de lista ou grade de maneira que todos os dados do contato sejam visíveis 

Dado que estou no sistema de contratos e preenchi os filtros de busca quando eu clicar na ação Carregar eu quero ver a lista de contatos em ordem alfabética por empresa que condizem com o filtro que especifiquei 

Dado que estou na tela de contatos quando eu clicar na ação Incluir  eu quero receber uma tela para a inclusão dos dados do novo contato,  com Nome, Cargo, Empresa, Tipo de empresa, Telefone, E-mail, Assunto 

Dado que estou cadastro um novo contato e que preenchi os campos do contato quando eu clicar na ação Salvar eu quero que o contato seja salvo na lista de contatos e a lista de contatos seja atualizada 

Dado que estou cadastro um novo contato quando eu clicar na ação Cancelar  eu quero que a tela de cadastro seja fechada sem salvar os dados que preenchi 

Dado que estou com a lista de contatos carregada quando eu clicar na ação Excluir eu quero excluir um contato da lista 
 
________________________________________________________________________________________

## Implementação:
O desafio foi realizado em Python, com SQLite para armazenar os dados (arquivo contatos.db, está populado aleatoriamente como um pequeno exemplo).

Foram criados 3 arquivos: App, DataBase e GUI. O arquivo 

**DataBase** cria o banco e dados, sua conexão e persistência além dos métodos CRUD

**GUI** é a interface gráfica, criada com a biblioteca nativa Tkinter, além da janela principal para listar os contatos, atualizá-los ou deletá-los, há uma janela que é criada ao clicar para incluir um novo contato.

**App** *é o arquivo a ser executado*. Realiza as ações do desafio, relacionando as ações dos botões com os dados armazenados.
