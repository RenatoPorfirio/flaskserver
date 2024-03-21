import json
import requests
from api.databasecon import DBHandler

db = DBHandler('localhost', '3306', 'root', 'teardrops2021', 'projeto_pdm')

def carregar_orcamentos():
    with open('orcamentos.json', 'r', encoding='utf-8') as file:
        orcamentos = json.load(file)
    return orcamentos

def buscar_orcamento(mes, ano, orcamentos):
    try:
        orcamentos[ano][mes]
        return 0
    except Exception:
        orcamentos[ano] = {}
        url = f'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{ano}/{mes}'
        try:
            dados = requests.get(url, verify=False, timeout=20, headers={
                'accept': 'application/json',
                'connection': 'keep-alive',
                'Cache-Control': 'no-cache',
                #'host': 'k8s-prd.tjrs.jus.br/',
            })
            if dados.status_code == 200:
                orcamentos[ano][mes] = dados.json()
                return 0
            else:
                return 1
        except Exception as e:
            print(e)
            return 2

def buscar_intervalo_orcamentos(mesInicio, anoInicio, mesFim, anoFim):
    orcamentos = carregar_orcamentos()

    mi = int(mesInicio)
    ai = int(anoInicio)
    mf = int(mesFim)
    af = int(anoFim)
    orcamentos_periodo = {}

    err_flag = False

    for ano in range(ai, af+1):
        mesi = mi if ano == ai else 1
        mesf = mf if ano == af else 12
        orcamentos_periodo[str(ano)] = {}
        for mes in range(mesi, mesf+1):
            status = buscar_orcamento(str(mes), str(ano), orcamentos)
            if status == 0:
                orcamentos_periodo[str(ano)][str(mes)] = orcamentos[str(ano)][str(mes)]
            else:
                err_flag = True
                break
        if err_flag:
            break

    with open('orcamentos.json', 'w', encoding='utf-8') as file:
        json.dump(orcamentos, file, indent=4)

    if err_flag:
        return (True, {'erro': 'Erro ao buscar dados! Tente novamente mais tarde.'})
    else:
        return (False, orcamentos_periodo)
