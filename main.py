import requests
from bs4 import BeautifulSoup
from json import dumps
import lxml
from django.shortcuts import render
from json import dumps
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
  #  "Accept-Language": "en"
}
url= "https://www.viamichelin.it/web/Stazioni-di-servizio?address=70024"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
stazioni = soup.find("div", "poilist-result-count")
#print(stazioni.text)
prezzo = 10.5
j = 0
def fungasolio():
    gasolio = soup.findAll("li", "poi-item-fuel-price-1")
    prezzo_gasolio = prezzo
    jgas = j
    for i in gasolio:
        if (prezzo_gasolio > float(gasolio[jgas].find("span", "poi-item-fuel-value").text)):
            prezzo_gasolio = float(gasolio[jgas].find("span", "poi-item-fuel-value").text)
            posgasolio = jgas
        jgas = jgas + 1
    print(prezzo_gasolio)
def funsp():
    sp95 = soup.findAll("li", "poi-item-fuel-price-2")
    prezzo_sp95 = prezzo
    jsp = j
    for i in sp95:
        if (prezzo_sp95 > float(sp95[jsp].find("span", "poi-item-fuel-value").text)):
            prezzo_sp95 = float(sp95[jsp].find("span", "poi-item-fuel-value").text)
            possp95 = jsp
        jsp = jsp + 1
    print(prezzo_sp95)
def fungpl():
    gpl = soup.findAll("li", "poi-item-fuel-price-4")
    prezzo_gpl = prezzo
    jgpl = j
    for i in gpl:
        if (prezzo_gpl > float(gpl[jgpl].find("span", "poi-item-fuel-value").text)):
            prezzo_gpl = float(gpl[jgpl].find("span", "poi-item-fuel-value").text)
            posgpl = jgpl
        jgpl = jgpl + 1
    print(prezzo_gpl)
def funmet():
    metano = soup.findAll("li", "poi-item-fuel-price-8")
    prezzo_metano = prezzo
    jmet = j
    for i in metano:
        if (prezzo_metano > float(metano[jmet].find("span", "poi-item-fuel-value").text)):
            prezzo_metano = float(metano[jmet].find("span", "poi-item-fuel-value").text)
            posmetano = j
        jmet = jmet + 1

    #print(prezzo_metano)


dataDictionary = {
    'hello': 'World',
    'geeks': 'forgeeks',
    }
    # dump data
dataJSON = dumps(dataDictionary)
print(dataJSON)

#sostituire len(prezzo1) a stazioni      //print(prezzo1[0])
#print(prezzo1[0].find("span", "poi-item-fuel-value").text)
