#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:18:07 2020

@author: Alex Alves
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def Tratar_conteduo(conteudo):
    lista =""
    for i in conteudo:
       # lista.append((i.text).strip())
        lista = i.text.strip()
    return lista

def Tratar_tag_li(conteudo):
    lista =""
    for i in conteudo:
        lista = (i.text).strip()[0]
    return lista
    
colunas = ["URL","Titulo","Endereço","Condomínio","Área","Quartos","Suítes","Banheiros","Vagas","Preço"]
df  = pd.DataFrame(columns=colunas)    
  
    
#https://www.vivareal.com.br/venda/rio-grande-do-norte/natal/apartamento_residencial/#onde=BR-Rio_Grande_do_Norte-NULL-Natal&tipos=apartamento_residencial
url = "https://www.vivareal.com.br/venda/rio-grande-do-norte/natal/?pagina=1#onde=BR-Rio_Grande_do_Norte-NULL-Natal&tipos=apartamento_residencial"
html = requests.get('https://www.vivareal.com.br/venda/rio-grande-do-norte/natal/?pagina=1#onde=BR-Rio_Grande_do_Norte-NULL-Natal&tipos=apartamento_residencial')
if html.status_code == 200:
   objeto_bs4 = bs(html.text, "html.parser")
   lista = objeto_bs4.find_all('article',class_="property-card__container")
   for conteudo_lista in lista:
       conteudo_titulos = conteudo_lista.find_all('a',class_='property-card__title')
       titulo = Tratar_conteduo(conteudo_titulos)
       conteudo_enderecos = conteudo_lista.find_all('span',class_='property-card__address')
       endereco = Tratar_conteduo(conteudo_enderecos)
       conteudo_areas = conteudo_lista.find_all('span',class_='property-card__detail-area')
       area = Tratar_conteduo(conteudo_areas)
       conteudo_condominio = conteudo_lista.find_all('strong',class_='js-condo-price')
       condominio = Tratar_conteduo(conteudo_condominio)
       conteudo_quarto = conteudo_lista.find_all('li',class_='property-card__detail-room')
       quartos = Tratar_tag_li(conteudo_quarto)
       conteudo_suites = conteudo_lista.find_all('li',class_='property-card__detail-item-extra')
       if len(conteudo_suites)==0:
           suites = "0"
       else:    
           suites = Tratar_tag_li(conteudo_suites)
       conteudo_banheiro = conteudo_lista.find_all('li',class_='property-card__detail-bathroom')
       banheiros = Tratar_tag_li(conteudo_banheiro)
       conteudo_vagas = conteudo_lista.find_all('li',class_='property-card__detail-garage')
       vagas = Tratar_tag_li(conteudo_vagas)
       conteudo_preco = conteudo_lista.find_all('div',class_='property-card__price')
       preco = Tratar_conteduo(conteudo_preco)
       
       dados = [url,titulo,endereco,condominio,area,quartos,suites,banheiros,vagas,preco]
       df.loc[len(df)] = dados
       
df.to_csv("teste.csv")