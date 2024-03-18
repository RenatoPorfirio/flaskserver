from flask import Flask, Response
import requests
import json

erroApiJSON = json.dumps({
    "erroApi": "Erro ao buscar dados! Existe um possivel problema com a API do TJRS. Tente novamente mais tarde.",
}, indent=4)

erroConexaoJSON = json.dumps({
    "erroCon": "Erro ao buscar dados! Verifique sua conexão e tente novamente.",
}, indent=4)

app = Flask(__name__)

@app.route('/')
def index():
    return 'API para buscar dados de orçamento do TJRS. Acesse /ano/mes para buscar os dados.'

@app.route('/<ano>/<mes>')
def buscarOrcamento(ano, mes):
    try:
        url = 'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{}/{}'.format(ano, mes)
        dados = requests.get(url, verify=False, timeout=25)
        if dados.status_code == 200:
            return Response(status=200, response=dados.text, mimetype='application/json')
        else:
            return Response(status=dados.status_code, response=erroApiJSON, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(status=500, response=erroConexaoJSON, mimetype='application/json')