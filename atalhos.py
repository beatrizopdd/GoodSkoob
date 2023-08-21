from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException

import time

#o skoob muitas vezes não reconhece o nome quando tem um ex.: Harry Potter (Volume #2)
def formatar_nome(nome):

	novo_nome = nome.split(' (')
	return novo_nome[0]



#o goodreads entrega a data no formato YYYY/MM/DD
def formatar_data(d_lido, d_adicionado):

	ano_mes_dia = d_lido.split('/')
	if (ano_mes_dia == ['']):
		ano_mes_dia = d_adicionado.split('/')
		
	dia_mes_ano = [int(ano_mes_dia[2]), int(ano_mes_dia[1]), int(ano_mes_dia[0])]
	return dia_mes_ano



#por algum motivo eu não consigo colocar a data pela janelinha que aparece quando clica no +
#pra abrir em uma outra aba tem que entrar em um link com base nos números que aparecem no final do link do livro
#pra isso serve essa função
def abrir_aba_datar(browser):

	url = browser.current_url
	
	tempA = url.split("ed")
	tempB = tempA[1].split(".")
	cod_livro = tempB[0]
	
	novo_url = "https://www.skoob.com.br/estante/s_editar/" + cod_livro
	browser.get(novo_url)



def logar(username, password, browser):

	browser.find_element("xpath", "/html/body/div/div[1]/div/div[2]/div/a").click()

	campo_email = browser.find_element("id", "UsuarioEmail")
	campo_senha = browser.find_element("id", "UsuarioSenha")
	enviar = browser.find_element("xpath", "/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div/input")
	
	campo_email.click()
	campo_email.send_keys(username)
	campo_senha.click()
	campo_senha.send_keys(password)

	enviar.click()

		

def guardar(nome, status, browser):

	browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[5]/button-shelf/div/button").click()
	time.sleep(2)
	
	if (status == "to-read"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[5]/button-shelf/div/ul/li[3]/a").click()

		
	elif (status == "currently-reading"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[5]/button-shelf/div/ul/li[2]/a").click()

		
	elif (status == "read"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[5]/button-shelf/div/ul/li[1]/a").click()
	
		

def buscar(nome, status, browser):

	barra_pesquisa = browser.find_element("id", "search")
	barra_pesquisa.click()
	barra_pesquisa.send_keys(nome)
	browser.find_element("xpath", "/html/body/div/div[1]/div/div[1]/form/div[2]/span/button").click()
	
	try:	
		capa_livro = browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[2]/div[2]/div[1]")
		capa_livro.click()
		guardar(nome, status, browser)
		
		return True

	except NoSuchElementException:
		print("ERRO AO BUSCAR: ", nome)
		
		return False



def avaliar(estrelas, browser):

	if (estrelas == "1"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[4]/star-rating/ul/li[1]").click()
		
	elif (estrelas == "2"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[4]/star-rating/ul/li[2]").click()
		
	elif (estrelas == "3"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[4]/star-rating/ul/li[3]").click()
		
	elif (estrelas == "4"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[4]/star-rating/ul/li[4]").click()
		
	elif (estrelas == "5"):
		browser.find_element("xpath", "/html/body/div/div[2]/div[3]/div/div/div[1]/div/div[4]/star-rating/ul/li[5]").click()
	

def datar(data, nome, browser):
	
	abrir_aba_datar(browser)
	time.sleep(3)
	
	try:
		select_dia = browser.find_element("name", "data[MeusLivro][dia_leitura]")
		select_mes = browser.find_element("name", "data[MeusLivro][mes_leitura]")
		select_ano = browser.find_element("name", "data[MeusLivro][ano_leitura]")
	
		dia = Select(select_dia)
		mes = Select(select_mes)
		ano = Select(select_ano)
		
		dia.select_by_value(str(data[0]))
		mes.select_by_value(str(data[1]))
		ano.select_by_value(str(data[2]))
		
		browser.find_element("xpath", "/html/body/div/div[2]/form/input").click()
		browser.get("https://www.skoob.com.br/")
	
	except NoSuchElementException:
		browser.get("https://www.skoob.com.br/")
		
		print("ERRO AO DATAR: ", nome)
		
	
	
