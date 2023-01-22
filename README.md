<h1 align="center"> :book: GoodSkoob :book: </h1>

Criei esse programa para exportar 301 livros do do Goodreads para o Skoobs. O objetivo é avaliar, colocar na prateleira correta e informar a data de leitura.

## MANUAL DE USO

- Baixar o arquivo csv das leituras do goodreads. Para evitar dor de cabeça deixa o nome do jeito que ele veio ao mundo: "goodreads_library_export.csv";

- Copiar o arquivo pra pasta do projeto;

- Abrir o arquivo csv e apagar a primeira linha de cabeçalho, salva e fecha;

- Abrir o arquivo "goodskoob.py" e, nas linhas 16 e 17, digitar seu usuário e senha dentro das aspas, salva e fecha;

username = "email@fulano.com"

password = "uva321pera"

### OBSERVAÇÕES

PS_0: Isso aqui é pensado em quem já tem conhecimento prévio em python e programação.

PS_1: Eu uso o Firefox como navegador, então tendo o ps anterior em mente muda o webdriver no arquivo "goodskoob.py" e coloca o certo na pasta (apaga o geckodriver).

PS_2: Em alguns momentos ele pode falhar mas eu coloquei uns prints no console pra você ter controle de quais já foram. Caso queira parar e continuar outro dia é só apagar os livros já logados.

PS_3: 99% de chance do livro entrar com o título em inglês mas as vezes, por uma intervenção divina, o Skoob entende e coloca em portugues. 

## PASSO-A-PASSO DO PROGRAMA

- abre o navegador
	- entra no site do skoob

- abre o arquivo comos livros do goodreads

- entra na area de login
	- endereça todos os campos e botão
	- preenche os campos
	- envia dados

- digita na barra de pesquisa
	- clica na lupa

- se for encontrado
	- seleciona o primeiro livro
	- clica no botão adicionar
	- adiciona na prateleira certa

- se não for encontrado
	- imprime `ERRO AO BUSCAR nome-do-livro`

- se já for um livro lido
	- avalia com as estrelas
	- abre a aba para editar as informações de leitura
		- adiciona a data de leitura ou, caso ela esteja vazia, a data que foi adicionado a estante
		- clica no botão salvar alterações
		
	- se ocorreu um erro na formatação do link
		- imprime `ERRO AO DATAR nome-do-livro`
- volta para a página inicial

