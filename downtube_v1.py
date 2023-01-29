from selenium import webdriver as wg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep as sl
from bs4 import BeautifulSoup as bs

mp4_xpath = '//*[@id="formatSelect"]/optgroup[1]'
mp3_xpath = '//*[@id="formatSelect"]/optgroup[4]'
path_input = '//*[@id="s_input"]'
botao = '//*[@id="search-form"]/button'
botao2 = '//*[@id="btn-action"]'
url = 'https://x2download.app/pt18'

opi = wg.ChromeOptions()
opi.add_argument('--headless')

def download(url_yt, ext, delay=1):
	nav = wg.Chrome(options=opi)
	nav.get(url)
	sl(3)
	campo = nav.find_element(By.XPATH, path_input)

	campo.send_keys(url_yt)

	campo.find_element(By.XPATH, botao).click()

	sl(delay)
	selecionado = campo.find_element(By.XPATH, '//*[@id="formatSelect"]')
	selecionado = Select(selecionado)
	if ext =='mp3':
		selecionado.select_by_value('128')
	else:
		selecionado.select_by_value('720p')
	sl(3)
	
	text = campo.find_element()

	return text


def extrai(texto):
	texto = bs(texto, 'html.parser')
	link = texto.find_all('href')
	print(link)

if __name__=='__main__':
	url_yt = 'https://youtu.be/vvFkZ2vlyxU'
	print(download(url_yt, ext='mp3'))