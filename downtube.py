#!/usr/bin/python
import requests as rq
#from bs4 import BeautifulSoup as bs
from time import sleep as sl
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

map4 = '//*[@id="formatSelect"]/optgroup[1]'
mp3 = '//*[@id="formatSelect"]/optgroup[4]'

url = 'https://x2download.app/pt18'
cabecalho = {
    'authority': 'x2download.app',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)',
}


data={'value':'https://youtu.be/kqvWOcPog4s'}

#sessao= rq.Session()

#pag = sessao.post(url=url, headers=cabecalho, data=data)
#print(pag.text)

nav = Chrome()

nav.get(url=url)

campo = nav.find_element(By.XPATH, '//*[@id="s_input"]')

campo.send_keys('https://youtu.be/kqvWOcPog4s')

campo.find_element(By.XPATH, '//*[@id="search-form"]/button').click()
sl(1)
campo.find_element(By.XPATH, mp3).click()
campo.find_element(By.XPATH, '//*[@id="btn-action"]').click()
sl(4)