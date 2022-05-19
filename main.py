import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, render_template, request, send_file, redirect, session, g
from json import dumps

'''
@app.route('/tool2', methods=['post', 'get'])
def cap():
    cap = request.form.get('cap')
    return render_template('tool2.html', cap=cap)
    '''
prezzo = 10.5
j = 0
lista = None
soup = None
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
  #  "Accept-Language": "en"
}

def stazioni(cap1):
    global soup
    global lista
    url = "https://www.viamichelin.it/web/Stazioni-di-servizio?address=" + str(cap1)
    print(url)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    stazioni = soup.find("div", "poilist-result-count")
    NrStazioni= stazioni
    lista ="".join(map(str,soup.findAll("ul", "poilist clearfx")))




def fungasolio():
    gasolio = soup.findAll("li", "poi-item-fuel-price-1")
    prezzo_gasolio = prezzo
    jgas = j
    for i in gasolio:
        if (prezzo_gasolio > float(gasolio[jgas].find("span", "poi-item-fuel-value").text)):
            prezzo_gasolio = float(gasolio[jgas].find("span", "poi-item-fuel-value").text)
            posgasolio = jgas
        jgas = jgas + 1
    return prezzo_gasolio


def funsp():
    sp95 = soup.findAll("li", "poi-item-fuel-price-2")
    prezzo_sp95 = prezzo
    jsp = j
    for i in sp95:
        if (prezzo_sp95 > float(sp95[jsp].find("span", "poi-item-fuel-value").text)):
            prezzo_sp95 = float(sp95[jsp].find("span", "poi-item-fuel-value").text)
            possp95 = jsp
        jsp = jsp + 1
    return prezzo_sp95


def fungpl():
    gpl = soup.findAll("li", "poi-item-fuel-price-4")
    prezzo_gpl = prezzo
    jgpl = j
    for i in gpl:
        if (prezzo_gpl > float(gpl[jgpl].find("span", "poi-item-fuel-value").text)):
            prezzo_gpl = float(gpl[jgpl].find("span", "poi-item-fuel-value").text)
            posgpl = jgpl
        jgpl = jgpl + 1
    return prezzo_gpl


def funmet():
    metano = soup.findAll("li", "poi-item-fuel-price-8")
    prezzo_metano = prezzo
    jmet = j
    for i in metano:
        if (prezzo_metano > float(metano[jmet].find("span", "poi-item-fuel-value").text)):
            prezzo_metano = float(metano[jmet].find("span", "poi-item-fuel-value").text)
            posmetano = j
        jmet = jmet + 1
    return prezzo_metano



app = Flask(__name__)
app.secret_key = "key"

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/about', methods=["POST", "GET"])
def about():
    return render_template("about.html")

@app.route('/tool2', methods=["POST", "GET"])
def tool2():
    global lista
    cap = '70024'
    stazioni(cap)
    print(lista)
    return render_template("tool2.html",
                           stazioni=str(lista),
                           cap = cap)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#sostituire len(prezzo1) a stazioni      //print(prezzo1[0])
#print(prezzo1[0].find("span", "poi-item-fuel-value").text)