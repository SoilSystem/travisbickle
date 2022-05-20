import requests
from bs4 import BeautifulSoup
import lxml
from flask import Flask, render_template, request, send_file, redirect, session, g
from json import dumps


prezzo = 10.5
lista = None
soup = None
posizione = None
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def stazioni(cap1,tipoCarb1):
    global posizione
    global soup
    global lista
    url = "https://www.viamichelin.it/web/Stazioni-di-servizio?address=" + str(cap1)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    stazioni = soup.find("div", "poilist-result-count")
    NrStazioni = stazioni
    lista = "".join(map(str, soup.findAll("ul", "poilist clearfx")))
    if (tipoCarb1 == "b7"):
        posizione = fungasolio()
    elif (tipoCarb1 == "e5"):
        posizione = funsp()
    elif (tipoCarb1 == "lpg"):
        posizione = fungpl()
    elif (tipoCarb1 == "cng"):
        posizione = funmet()


def fungasolio():
    gasolio = soup.findAll("li", "poi-item-fuel-price-1")
    prezzo_gasolio = prezzo
    jgas = 0
    for i in gasolio:
        if prezzo_gasolio > float(gasolio[jgas].find("span", "poi-item-fuel-value").text):
            prezzo_gasolio = float(
                gasolio[jgas].find("span", "poi-item-fuel-value").text
            )
            posgasolio = jgas
        jgas = jgas + 1
    return prezzo_gasolio


def funsp():
    sp95 = soup.findAll("li", "poi-item-fuel-price-2")
    prezzo_sp95 = prezzo
    jsp = 0
    for i in sp95:
        if prezzo_sp95 > float(sp95[jsp].find("span", "poi-item-fuel-value").text):
            prezzo_sp95 = float(sp95[jsp].find("span", "poi-item-fuel-value").text)
            possp95 = jsp
        jsp = jsp + 1
    return prezzo_sp95


def fungpl():
    gpl = soup.findAll("li", "poi-item-fuel-price-4")
    prezzo_gpl = prezzo
    jgpl = 0
    for i in gpl:
        if prezzo_gpl > float(gpl[jgpl].find("span", "poi-item-fuel-value").text):

            prezzo_gpl = float(gpl[jgpl].find("span", "poi-item-fuel-value").text)

            posgpl = jgpl
        jgpl = jgpl + 1
    return prezzo_gpl


def funmet():
    metano = soup.findAll("li", "poi-item-fuel-price-8")
    prezzo_metano = prezzo
    jmet = 0
    for i in metano:
        if prezzo_metano > float(metano[jmet].find("span", "poi-item-fuel-value").text):
            prezzo_metano = float(metano[jmet].find("span", "poi-item-fuel-value").text)
            posmetano = 0
        jmet = jmet + 1
    return prezzo_metano


app = Flask(__name__)
app.secret_key = "key"


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/index", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")


@app.route("/tool2", methods=["POST", "GET"])
def tool2():
    global lista
    return render_template("tool2.html")


@app.route("/tool3", methods=["POST", "GET"])
def tool3():
    global lista
    cap = request.form["cap"]
    tipoCarb = request.form["carburante"]
    stazioni(cap, tipoCarb)
    return render_template("tool3.html", stazioni=str(lista),
                           cap=cap,
                           tipocarb = tipoCarb,
                           posizione = posizione
                           )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
