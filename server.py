from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homePage():
    if request.method == 'POST':
        ano = request.form['ano']
        mes = request.form['mes']
    else:
        ano = request.args.get('ano')
        mes = request.args.get('mes')
    url = 'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{}/{}'.format(ano, mes)
    dados = requests.get(url, verify=False)
    return Response(status=dados.status_code, response=dados.text.encode(), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)