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
	unidadeOrcamentariaCodigo VARCHAR(5),
    unidadeOrcamentariaDescricao VARCHAR(100),
	funcaoESubFuncao VARCHAR(6),
	programatica VARCHAR(11),
	programaDescricao VARCHAR(500),
	acaoESubtitulo VARCHAR(1000),
	esfera CHAR,
	fonteCodigo VARCHAR(3),
	fonteDescricao VARCHAR(500),
    gndCodigo CHAR,
    PRIMARY KEY (id_orcamento)
);

CREATE TABLE dotacao(
	id_orcamento INT AUTO_INCREMENT,
    inicial NUMERIC(12, 2),
	creditosAdicionaisAcrescimo NUMERIC(12, 2),
	creditosAdicionaisDescrescimos NUMERIC(12, 2),
	atualizada NUMERIC(12, 2),
	contingenciado NUMERIC(12, 2),
	movLiquidaCreditosProvisao NUMERIC(12, 2),
	movLiquidaCreditosDestaque NUMERIC(12, 2),
	liquida NUMERIC(12, 2),
    PRIMARY KEY (id_orcamento)
);

CREATE TABLE execucao(
	id_orcamento INT AUTO_INCREMENT,
    empenhado NUMERIC(12, 2),
	empenhadoPorcentagem FLOAT,
	liquidado NUMERIC(12, 2),
	liquidadoPorcentagem FLOAT,
	pago NUMERIC(12, 2),
	pagoPorcentagem FLOAT,
    PRIMARY KEY (id_orcamento)
);