from selenium import webdriver
from atalhos import*
import csv

#CONTROLE DO NAVEGADOR
navegador = webdriver.Firefox()
navegador.get("https://www.skoob.com.br/")


#ARQUIVO COM OS LIVROS
estante = open('goodreads_library_export.csv', encoding='utf-8')
prateleira = csv.reader(estante, delimiter=',')


#LOGIN
username = ""
password = ""
logar(username, password, navegador)


encontrado = True


for livro in prateleira:
  
	#INFO BÁSICA DO LIVRO
	title = formatar_nome(livro[1])
	status = livro[18]

	#BUSCANDO e GUARDANDO
	encontrado = buscar(title, status, navegador)
	
	#AVALIANDO se for o caso
	if (encontrado == True and status == "read"):
		rating = livro[7]
		date_read = formatar_data(livro[14], livro[15])
		
		avaliar(rating, navegador)
		datar(date_read, title, navegador)

