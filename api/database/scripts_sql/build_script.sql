USE projeto_pdm;
DROP TABLE IF EXISTS lista_orcamentos;
DROP TABLE IF EXISTS orcamento;
DROP TABLE IF EXISTS classificacao;
DROP TABLE IF EXISTS dotacao;
DROP TABLE IF EXISTS execucao;

CREATE TABLE lista_orcamentos(
	id_lista INT,
	mes INT,
	ano INT,
	PRIMARY KEY (id_lista)
);

CREATE TABLE orcamento(
	id_orcamento INT AUTO_INCREMENT,
	id_lista INT,
	PRIMARY KEY (id_orcamento)
);

CREATE TABLE classificacao(
	id_orcamento INT AUTO_INCREMENT,
	unidadeOrcamentariaCodigo VARCHAR(100),
    unidadeOrcamentariaDescricao VARCHAR(100),
	funcaoESubFuncao VARCHAR(100),
	programatica VARCHAR(100),
	programaDescricao VARCHAR(500),
	acaoESubtitulo VARCHAR(1000),
	esfera VARCHAR(100),
	fonteCodigo VARCHAR(100),
	fonteDescricao VARCHAR(500),
    gndCodigo VARCHAR(100),
    PRIMARY KEY (id_orcamento)
);

CREATE TABLE dotacao(
	id_orcamento INT AUTO_INCREMENT,
    inicial VARCHAR(100),
	creditosAdicionaisAcrescimo VARCHAR(100),
	creditosAdicionaisDescrescimos VARCHAR(100),
	atualizada VARCHAR(100),
	contingenciado VARCHAR(100),
	movLiquidaCreditosProvisao VARCHAR(100),
	movLiquidaCreditosDestaque VARCHAR(100),
	liquida VARCHAR(100),
    PRIMARY KEY (id_orcamento)
);

CREATE TABLE execucao(
	id_orcamento INT AUTO_INCREMENT,
    empenhado VARCHAR(100),
	empenhadoPorcentagem VARCHAR(100),
	liquidado VARCHAR(100),
	liquidadoPorcentagem VARCHAR(100),
	pago VARCHAR(100),
	pagoPorcentagem VARCHAR(100),
    PRIMARY KEY (id_orcamento)
);