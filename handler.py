import json
import requests

def carregar_orcamentos():
    with open('orcamentos.json', 'r') as file:
        orcamentos = json.load(file)
    return orcamentos

def buscar_orcamento(mes, ano):
    orcamentos = carregar_orcamentos()
    try:
        orcamentos[ano][mes]
        return (200, orcamentos[ano][mes])
    except:
        orcamentos[ano] = {}
        url = 'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{}/{}'.format(ano, mes)
        try:
            dados = requests.get(url, verify=False, timeout=60)
            if dados.status_code == 200:
                orcamentos[ano][mes] = dados.json()
                with open('orcamentos.json', 'w') as file:
                    json.dump(orcamentos, file, indent=4)
                return (200, orcamentos[ano][mes])
            else:
                return (201, {})
        except Exception as e:
            print('erro: ', e)
            return (500, {})
