from api.server import iniciar_api
from api.handler import db, parse_orcamento, parse_classificacao, parse_dotacao, parse_execucao, comparar_orcamentos
from multiprocessing import Process
import requests

comandosAtualizar = ['atualizar', 'a']
comandosEncerrar = ['encerrar', 'e']

def rotina_atualizacao():
    def checar(mes, ano, orcamentos):
        print(f'Verificando dados de {mes}/{ano}...')
        try:
            url = f'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{ano}/{mes}'
            orcamentos_mes = requests.get(url, verify=False, timeout=20, headers={
                'accept': 'application/json',
                'connection': 'keep-alive',
                'Cache-Control': 'no-cache',
            })
            if orcamentos_mes.status_code == 200:
                novos_orcamentos = []
                for orcamento in orcamentos_mes.json():
                    aux = {}
                    aux.update(parse_classificacao(orcamento))
                    aux.update(parse_dotacao(orcamento))
                    aux.update(parse_execucao(orcamento))
                    novos_orcamentos.append(aux)
                n = len(orcamentos)
                m = len(novos_orcamentos)
                print(novos_orcamentos[0])
                print(orcamentos[0])
                if n != m or not comparar_orcamentos(orcamentos, novos_orcamentos):
                    print(f'Divergência! Atualizando dados de {mes}/{ano}...')

        except Exception as e:
            print(e)
        
    mes = ano = 0
    orcamentos = []
    for orcamento in db.select_all():
        if orcamento[0] == mes and orcamento[1] == ano:
            orcamentos.append(parse_orcamento(orcamento))
        else:
            checar(mes, ano, orcamentos)
            mes = orcamento[0]
            ano = orcamento[1]
            orcamentos = []
    checar(mes, ano, orcamentos)
    
if __name__ == '__main__':
    try:
        str = ''
        while all([str != comando for comando in comandosEncerrar]):
            str = ''
            serverProcess = Process(target=iniciar_api)
            serverProcess.start()
            while all([str != comando for comando in comandosAtualizar]) and all([str != comando for comando in comandosEncerrar]):
                str = input()
            if any([str == comando for comando in comandosAtualizar]):
                print('Atualizando dados...')
                rotina_atualizacao()
            serverProcess.kill()
    except Exception as e:
        print('erro:', e, '\nServiço encerrado!')