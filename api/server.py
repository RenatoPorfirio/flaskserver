import json
from flask import Flask, Response, request
from gevent.pywsgi import WSGIServer
from api.handler import buscar_intervalo_orcamentos

erroApiJSON = json.dumps({
    "erroApi": "Erro ao buscar dados! Existe um possivel problema com a API do TJRS. Tente novamente mais tarde.",
}, indent=4)

erroConexaoJSON = json.dumps({
    "erroCon": "Erro ao buscar dados! Verifique sua conexão e tente novamente.",
}, indent=4)

app = Flask(__name__)

@app.route('/')
def index():
    return 'API para buscar dados de orçamento do TJRS. Acesse /mesIncio/anoInicio/mesFim/anoFim para buscar os dados.'

@app.route('/<mesInicio>/<anoInicio>/<mesFim>/<anoFim>')
def buscarOrcamento(mesInicio, anoInicio, mesFim, anoFim):
    if not mesInicio.isnumeric() or not anoInicio.isnumeric() or not mesFim.isnumeric() or not anoFim.isnumeric():
        return Response(json.dumps({"erro": "Os parâmetros devem ser numéricos."}, indent=4), status=400, mimetype='application/json')

    falha, lista_orcamento = buscar_intervalo_orcamentos(mesInicio, anoInicio, mesFim, anoFim)
    if falha:
        return Response(json.dumps(lista_orcamento, indent=4), status=500, mimetype='application/json')
    else:
        return Response(json.dumps(lista_orcamento, indent=4), status=200, mimetype='application/json')

def iniciar_api():
    try:
        print('Iniciando serviço na porta 8000...')
        WSGIServer(('0.0.0.0', 8000), app).serve_forever()
    except:
        pass
