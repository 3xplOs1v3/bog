#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:29:21 2023

@author: sk
"""
import requests
from bs4 import BeautifulSoup

#url = 'https://www.coingecko.com/es'

def pagina(url):
    
    res = []
    a = requests.get(url) 
    aa = BeautifulSoup(a.text,'html.parser').find_all('tr')
    
    for i in range(1,len(aa)):
        
        name = aa[i].find('span',{'class':'lg:tw-flex font-bold tw-items-center tw-justify-between'}).text
        
        # precio, vol24h, cap, noseke
        k1 = aa[i].find_all('span',{'data-target':'price.price'})
        
        # cosas verdes v1h, v24h, v7d
        k2 = aa[i].find_all('span',{'data-up-class':'text-green'})
        
        print("NAME: ", name, [ki.text for ki in k1+k2],"\n")
        
        res.append([name, k1+k2])
        
    return res

    


for pag in range(1,113):
    print("PAGINA: ", pag)
    url = 'https://www.coingecko.com/es?page='+str(pag)
    pagina(url)
    

