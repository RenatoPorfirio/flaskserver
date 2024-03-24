import json
import requests
from api.databasecon import DBHandler

def carregar_database():
    return DBHandler('localhost', '3306', 'root', 'teardrops2021', 'projeto_pdm')    

db = carregar_database()

def parse_orcamento(orcamento):
    return {
        'unidadeOrcamentariaCodigo': orcamento[2],
        'unidadeOrcamentariaDescricao': orcamento[3],
        'funcaoESubFuncao': orcamento[4],
        'programatica': orcamento[5],
        'programaDescricao': orcamento[6],
        'acaoESubtitulo': orcamento[7],
        'esfera': orcamento[8],
        'fonteCodigo': orcamento[9],
        'fonteDescricao': orcamento[10],
        'gndCodigo': orcamento[11],
        'inicial': orcamento[12],
        'creditosAdicionaisAcrescimo': orcamento[13],
        'creditosAdicionaisDescrescimos': orcamento[14],
        'atualizada': orcamento[15],
        'contingenciado': orcamento[16],
        'movLiquidaCreditosProvisao': orcamento[17],
        'movLiquidaCreditosDestaque': orcamento[18],
        'liquida': orcamento[19],
        'empenhado': orcamento[20],
        'empenhadoPorcentagem': orcamento[21],
        'liquidado': orcamento[22],
        'liquidadoPorcentagem': orcamento[23],
        'pago': orcamento[24],
        'pagoPorcentagem': orcamento[25]
    }
        
def parse_classificacao(orcamento):
    return {
        'unidadeOrcamentariaCodigo': str(orcamento['classificacao']['unidadeOrcamentariaCodigo']),
        'unidadeOrcamentariaDescricao': str(orcamento['classificacao']['unidadeOrcamentariaDescricao']),
        'funcaoESubFuncao': str(orcamento['classificacao']['funcaoESubFuncao']),
        'programatica': str(orcamento['classificacao']['programatica']),
        'programaDescricao': str(orcamento['classificacao']['programaDescricao']),
        'acaoESubtitulo': str(orcamento['classificacao']['acaoESubtitulo']),
        'esfera': str(orcamento['classificacao']['esfera']),
        'fonteCodigo': str(orcamento['classificacao']['fonteCodigo']),
        'fonteDescricao': str(orcamento['classificacao']['fonteDescricao']),
        'gndCodigo': str(orcamento['classificacao']['gndCodigo'])
    }

def parse_dotacao(orcamento):
    return {
        'inicial': str(orcamento['dotacao']['inicial']),
        'creditosAdicionaisAcrescimo': str(orcamento['dotacao']['creditosAdicionaisAcrescimo']),
        'creditosAdicionaisDescrescimos': str(orcamento['dotacao']['creditosAdicionaisDescrescimos']),
        'atualizada': str(orcamento['dotacao']['atualizada']),
        'contingenciado': str(orcamento['dotacao']['contingenciado']),
        'movLiquidaCreditosProvisao': str(orcamento['dotacao']['movLiquidaCreditosProvisao']),
        'movLiquidaCreditosDestaque': str(orcamento['dotacao']['movLiquidaCreditosDestaque']),
        'liquida': str(orcamento['dotacao']['liquida'])
    }
    
def parse_execucao(orcamento):
    return {
        'empenhado': str(orcamento['execucao']['empenhado']),
        'empenhadoPorcentagem': str(orcamento['execucao']['empenhadoPorcentagem']),
        'liquidado': str(orcamento['execucao']['liquidado']),
        'liquidadoPorcentagem': str(orcamento['execucao']['liquidadoPorcentagem']),
        'pago': str(orcamento['execucao']['pago']),
        'pagoPorcentagem': str(orcamento['execucao']['pagoPorcentagem'])
    }

def buscar_orcamento(mes, ano, orcamentos):
    try:
        listaOrcamentos = db.select_orcamentos(int(mes), int(ano))
        dados_orcamento = {
            'mes': mes,
            'ano': ano,
        }
        if listaOrcamentos == []:
            url = f'https://k8s-prd.tjrs.jus.br/public/api/transparencia/orcamento/{ano}/{mes}'
            print('buscando orcamento de ' + mes + '/' + ano + '...')
            dados = requests.get(url, verify=False, timeout=20, headers={
                'accept': 'application/json',
                'connection': 'keep-alive',
                'Cache-Control': 'no-cache',
            })
            if dados.status_code == 200:
                orcamentos_aux = dados.json()
                db.insert_listaOrcamentos(int(mes+ano), int(mes), int(ano))
                for(orcamento) in orcamentos_aux:
                    db.insert_orcamento(int(mes+ano))
                    classificacao = parse_classificacao(orcamento)
                    dotacao = parse_dotacao(orcamento)
                    execucao = parse_execucao(orcamento)
                    
                    db.insert_classificacao(
                        classificacao['unidadeOrcamentariaCodigo'],
                        classificacao['unidadeOrcamentariaDescricao'],
                        classificacao['funcaoESubFuncao'],
                        classificacao['programatica'],
                        classificacao['programaDescricao'],
                        classificacao['acaoESubtitulo'],
                        classificacao['esfera'],
                        classificacao['fonteCodigo'],
                        classificacao['fonteDescricao'],
                        classificacao['gndCodigo']
                    )
                    db.insert_dotacao(
                        dotacao['inicial'],
                        dotacao['creditosAdicionaisAcrescimo'],
                        dotacao['creditosAdicionaisDescrescimos'],
                        dotacao['atualizada'],
                        dotacao['contingenciado'],
                        dotacao['movLiquidaCreditosProvisao'],
                        dotacao['movLiquidaCreditosDestaque'],
                        dotacao['liquida']
                    )
                    db.insert_execucao(
                        execucao['empenhado'],
                        execucao['empenhadoPorcentagem'],
                        execucao['liquidado'],
                        execucao['liquidadoPorcentagem'],
                        execucao['pago'],
                        execucao['pagoPorcentagem']
                    )
                dados_orcamento['orcamentos'] = [parse_orcamento(orcamento) for orcamento in db.select_orcamentos(int(mes), int(ano))]
                orcamentos.append(dados_orcamento)
                return False
            else:
                return True
        else:
            dados_orcamento['orcamentos'] = [parse_orcamento(orcamento) for orcamento in listaOrcamentos]
            orcamentos.append(dados_orcamento)
            return False
    except Exception as e:
        print(e)
        return True

def  comparar_orcamentos(o1, o2):
    n = len(o1)
    m = len(o2)
    if n != m:
        return False
    for i in range(n):
        for key, value in o1[i].items():
            if(o2[i][key] != value):
                return False
    return True

def buscar_intervalo_orcamentos(mesInicio, anoInicio, mesFim, anoFim):
    mi = int(mesInicio)
    ai = int(anoInicio)
    mf = int(mesFim)
    af = int(anoFim)
    
    orcamentos = []

    err_flag = False

    for ano in range(ai, af+1):
        mesi = mi if ano == ai else 1
        mesf = mf if ano == af else 12
        for mes in range(mesi, mesf+1):
            falha = buscar_orcamento(str(mes), str(ano), orcamentos)
            if falha:
                err_flag = True
                break
        if err_flag:
            break

    if err_flag:
        return (True, {'erro': 'Erro ao buscar dados! Tente novamente mais tarde.'})
    else:
        return (False, orcamentos)
