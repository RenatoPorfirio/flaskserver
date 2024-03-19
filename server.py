from flask import Flask, Response
import json
import handler

with open('orcamentos.json', 'r') as file:
    orcamentos = json.load(file)

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
    status, orcamento = handler.buscar_orcamento(mes, ano)
    if status == 200:
        return Response(json.dumps(orcamento, indent=4), status=200, mimetype='application/json')
    elif status == 201:
        return Response(erroApiJSON, status=500, mimetype='application/json')
    else:
        return Response(json.dumps(orcamento, indent=4), status=500, mimetype='application/json')
