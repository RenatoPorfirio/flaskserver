import mysql.connector

class DBHandler:
    def __init__(self, _host, _port, _user, _password, _database):
        self.db = mysql.connector.connect(
            host=_host,
            port=_port,
            user=_user,
            password=_password,
            database=_database
        )
        self.cursor = self.db.cursor()
        self.listaOrcamentos_insertQuery = """
        INSERT INTO lista_orcamentos (
            id_lista,
            mes,
            ano
        ) VALUES (
            {id_lista:d},
            {mes:d},
            {ano:d}
        );"""
        self.orcamento_insertQuery = """INSERT INTO orcamento (
            id_lista
        ) VALUES (
            {id_lista:d}
        );"""
        self.classificacao_insertQuery = """
        INSERT INTO classificacao (
            unidadeOrcamentariaCodigo,
            unidadeOrcamentariaDescricao,
            funcaoESubFuncao,
            programatica,
            programaDescricao,
            acaoESubtitulo,
            esfera,
            fonteCodigo,
            fonteDescricao,
            gndCodigo
        ) VALUES (
            {unidadeOrcamentariaCodigo:s},
            {unidadeOrcamentariaDescricao:s},
            {funcaoESubFuncao:s},
            {programatica:s},
            {programaDescricao:s},
            {acaoESubtitulo:s},
            {esfera:s},
            {fonteCodigo:s},
            {fonteDescricao:s},
            {gndCodigo:s}
        );"""
        self.dotacao_insertQuery = "INSERT INTO dotacao (id_lista, mes, ano) VALUES ({id_lista:d},{mes:d},{ano:d});"
        self.execucao_insertQuery = "INSERT INTO execucao (id_lista, mes, ano) VALUES ({id_lista:d},{mes:d},{ano:d});"
        
    def insert_listaOrcamentos(
        self,
        unidadeOrcamentariaCodigo,
        unidadeOrcamentariaDescricao,
        funcaoESubFuncao,
        programatica,
        programaDescricao,
        acaoESubtitulo,
        esfera,
        fonteCodigo,
        fonteDescricao,
        gndCodigo
    ):
        self.cursor.execute(self.listaOrcamentos_insertQuery.format(
            unidadeOrcamentariaCodigo=unidadeOrcamentariaCodigo,
            unidadeOrcamentariaDescricao=unidadeOrcamentariaDescricao,
            funcaoESubFuncao=funcaoESubFuncao,
            programatica=programatica,
            programaDescricao=programaDescricao,
            acaoESubtitulo=acaoESubtitulo,
            esfera=esfera,
            fonteCodigo=fonteCodigo,
            fonteDescricao=fonteDescricao,
            gndCodigo=gndCodigo
        ))
        self.db.commit()
    
    def insert_orcamento(self, arg_idLista):
        self.cursor.execute(self.orcamento_insertQuery.format(id_lista=arg_idLista))
        self.db.commit()
        
    def insert_classificacao(self, arg_idLista):
        self.cursor.execute(self.orcamento_insertQuery.format(id_lista=arg_idLista))
        self.db.commit()
            
db = DBHandler('localhost', '3306', 'root', 'teardrops2021', 'projeto_pdm')