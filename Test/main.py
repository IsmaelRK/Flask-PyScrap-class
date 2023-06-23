from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import math


def scrpreco(url, seletor):  # Recebe url com arg


    headers = {  # Define um dicionário, contendo informações HTTP, simulando um navegador

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'close'
    }

    response = requests.get(url, headers=headers)  # Faz uma solicitação (GET) para a URL (que foi recebida como arg)
    # E atribui os headers para "enganar o site", um bot se passando por um navegador comum

    soup = BeautifulSoup(response.text, 'html.parser')  # Cria um objeto a partir do conteúdo HTML da resposta
    # .text transforma o resultado da solicitação em uma string

    # 'html.parser' especifica o analizador html a ser usado, nesse caso o 'html.parser' é baseado em python, e é do
    # framework BeautifulSoup

    preco = soup.select_one(seletor).text.strip()  # Usa um seletor css para selecionar o elemento,
    #  transforma o resultado da solicitação em uma string e remove os espaços em branco (.text.strip())

    precofloat0 = ""  # Itera e cria um string "conversivel" para float

    for x in preco:
        if x == ",":
            precofloat0 += "."
        elif x.isdigit():
            precofloat0 += x

    return float(precofloat0)  # Retorna o valor precofloat convertido em float e não mais como string


url0 = 'https://www.neosolar.com.br/loja/painel-solar-fotovoltaico-155w-resun-rs6e-155p.html'
seletor0 = '#product-price-31084'

url1 = 'https://www.neosolar.com.br/loja/painel-solar-fotovoltaico-330w-osda-oda330-36-p.html'
seletor1 = '#product-price-30168'

precoscrap0 = scrpreco(url0, seletor0)  # Retorna a URL para a função e recebe o valor tratado
precoscrap1 = scrpreco(url1, seletor1)


#  Fim do scrap. Inicio do Flask:

app = Flask(__name__)  # Criar instância do Flask com o nome do módulo para "configurar" o ambiente e suas rotas

@app.route('/', methods=['GET', 'POST'])  # '/' define a rota principal do browser e methods=['GET', 'POST'] indica q a
# rota pode ser acessada por get e post

def index():  # Essa função é associada a rota raiz/principal
    if request.method == 'POST':
        num1 = int(request.form['numero1'])  # Recebe os valores do form, da input pelo name(numero1)
        num2 = int(request.form['numero2'])
        num3 = int(request.form['numero3'])
        delta = (num2 * num2) + (-4 * (num1 * num3))

        p1 = num2 * (-1)
        p2 = math.sqrt(delta)
        p3 = (2 * num1)

        x1 = (p1 + p2) / p3
        x2 = (p1 - p2) / p3


        return render_template('resultado.html', res=(precoscrap0 + precoscrap1), delta=delta, x1=x1, x2=x2)  # Retorna o parametro res para a renderização do
        # resultado.html
    return render_template('index.html')  # Retorna para renderização do index.html se o método for GET


if __name__ == '__main__':  # Verifica se esta sendo executado diretamente (e não como um módulo) e inicia o server
    app.run()


"""
opcao_selecionada = request.form.get('opcao') Se estiver vazio: None
opcao_selecionada = request.form['opcao'] Se estiver vazio: ERROR!
"""