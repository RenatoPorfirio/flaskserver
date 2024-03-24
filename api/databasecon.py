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
        self.orcamento_insertQuery = """
        INSERT INTO orcamento (
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
            '{unidadeOrcamentariaCodigo:s}',
            '{unidadeOrcamentariaDescricao:s}',
            '{funcaoESubFuncao:s}',
            '{programatica:s}',
            '{programaDescricao:s}',
            '{acaoESubtitulo:s}',
            '{esfera:s}',
            '{fonteCodigo:s}',
            '{fonteDescricao:s}',
            '{gndCodigo:s}'
        );"""
        self.dotacao_insertQuery = """
        INSERT INTO dotacao (
            inicial,
            creditosAdicionaisAcrescimo,
            creditosAdicionaisDescrescimos,
            atualizada,
            contingenciado,
            movLiquidaCreditosProvisao,
            movLiquidaCreditosDestaque,
            liquida
        ) VALUES (
            '{inicial:s}',
            '{creditosAdicionaisAcrescimo:s}',
            '{creditosAdicionaisDescrescimos:s}',
            '{atualizada:s}',
            '{contingenciado:s}',
            '{movLiquidaCreditosProvisao:s}',
            '{movLiquidaCreditosDestaque:s}',
            '{liquida:s}'
        );"""
        self.execucao_insertQuery = """
        INSERT INTO execucao (
            empenhado,
            empenhadoPorcentagem,
            liquidado,
            liquidadoPorcentagem,
            pago,
            pagoPorcentagem
        ) VALUES (
            '{empenhado:s}',
            '{empenhadoPorcentagem:s}',
            '{liquidado:s}',
            '{liquidadoPorcentagem:s}',
            '{pago:s}',
            '{pagoPorcentagem:s}'
        );"""
        self.intervalo_selectQuery = """
        SELECT mes,ano,unidadeOrcamentariaCodigo,unidadeOrcamentariaDescricao,funcaoESubFuncao,programatica,programaDescricao,acaoESubtitulo,esfera,fonteCodigo,fonteDescricao,gndCodigo,inicial,creditosAdicionaisAcrescimo,creditosAdicionaisDescrescimos,atualizada,contingenciado,movLiquidaCreditosProvisao,movLiquidaCreditosDestaque,liquida,empenhado,empenhadoPorcentagem,liquidado,liquidadoPorcentagem,pago,pagoPorcentagem
        FROM lista_orcamentos
        CROSS JOIN orcamento
        USING (id_lista)
        CROSS JOIN classificacao
        USING (id_orcamento)
        CROSS JOIN dotacao
        USING (id_orcamento)
        CROSS JOIN execucao
        USING (id_orcamento)
        WHERE (mes = {mes:d} AND ano = {ano:d});
        """
        self.all_selectQuery = """
        SELECT mes,ano,unidadeOrcamentariaCodigo,unidadeOrcamentariaDescricao,funcaoESubFuncao,programatica,programaDescricao,acaoESubtitulo,esfera,fonteCodigo,fonteDescricao,gndCodigo,inicial,creditosAdicionaisAcrescimo,creditosAdicionaisDescrescimos,atualizada,contingenciado,movLiquidaCreditosProvisao,movLiquidaCreditosDestaque,liquida,empenhado,empenhadoPorcentagem,liquidado,liquidadoPorcentagem,pago,pagoPorcentagem
        FROM lista_orcamentos
        CROSS JOIN orcamento
        USING (id_lista)
        CROSS JOIN classificacao
        USING (id_orcamento)
        CROSS JOIN dotacao
        USING (id_orcamento)
        CROSS JOIN execucao
        USING (id_orcamento)
        ORDER BY ano,mes ASC;
        """
        
    def insert_listaOrcamentos(
        self,
        id_lista,
        mes,
        ano
    ):
        self.cursor.execute(self.listaOrcamentos_insertQuery.format(
            id_lista=id_lista,
            mes=mes,
            ano=ano
        ))
        self.db.commit()
    
    def insert_orcamento(
        self,
        arg_idLista
    ):
        self.cursor.execute(self.orcamento_insertQuery.format(
            id_lista=arg_idLista
        ))
        self.db.commit()
        
    def insert_classificacao(
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
        self.cursor.execute(self.classificacao_insertQuery.format(
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
    
    def insert_dotacao(
        self,
        inicial,
        creditosAdicionaisAcrescimo,
        creditosAdicionaisDescrescimos,
        atualizada,
        contingenciado,
        movLiquidaCreditosProvisao,
        movLiquidaCreditosDestaque,
        liquida
    ):
        self.cursor.execute(self.dotacao_insertQuery.format(
            inicial=inicial,
            creditosAdicionaisAcrescimo=creditosAdicionaisAcrescimo,
            creditosAdicionaisDescrescimos=creditosAdicionaisDescrescimos,
            atualizada=atualizada,
            contingenciado=contingenciado,
            movLiquidaCreditosProvisao=movLiquidaCreditosProvisao,
            movLiquidaCreditosDestaque=movLiquidaCreditosDestaque,
            liquida=liquida
        ))
        self.db.commit()
        
    def insert_execucao(
        self,
        empenhado,
        empenhadoPorcentagem,
        liquidado,
        liquidadoPorcentagem,
        pago,
        pagoPorcentagem
    ):
        self.cursor.execute(self.execucao_insertQuery.format(
            empenhado=empenhado,
            empenhadoPorcentagem=empenhadoPorcentagem,
            liquidado=liquidado,
            liquidadoPorcentagem=liquidadoPorcentagem,
            pago=pago,
            pagoPorcentagem=pagoPorcentagem
        ))
        self.db.commit()

    def select_orcamentos(self, mes, ano):
        self.cursor.execute(self.intervalo_selectQuery.format(mes=mes, ano=ano))
        return self.cursor.fetchall()

    def select_all(self):
        self.cursor.execute(self.all_selectQuery)
        return self.cursor.fetchall()
