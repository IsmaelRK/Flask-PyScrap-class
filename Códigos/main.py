from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests


def scrpreco(url, seletor):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'close'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    preco = soup.select_one(seletor).text.strip()

    precofloat0 = ""

    for x in preco:
        if x == ",":
            precofloat0 += "."
        elif x.isdigit():
            precofloat0 += x

    return float(precofloat0)


url0 = 'https://www.neosolar.com.br/loja/painel-solar-fotovoltaico-155w-resun-rs6e-155p.html'
seletor0 = '#product-price-31084'

url1 = 'https://www.neosolar.com.br/loja/painel-solar-fotovoltaico-330w-osda-oda330-36-p.html'
seletor1 = '#product-price-30168'

precoscrap0 = scrpreco(url0, seletor0)
precoscrap1 = scrpreco(url1, seletor1)
media = (precoscrap0 + precoscrap1) / 2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = int(request.form["numero1"])
        num2 = int(request.form.get("numero2"))
        num3 = int(request.form["numero3"])
        delta = (num2 * num2) + (-4 * (num1 * num3))
        return render_template('resultado.html', deltahtml=delta, mediahtml=media)
        # Lembre variável_que_irá_ser_chamada_no_html = variavel_do_python

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
