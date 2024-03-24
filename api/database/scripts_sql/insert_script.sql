USE projeto_pdm;

INSERT INTO lista_orcamentos
VALUE(
	92023,
    9,
    2023
);

INSERT INTO orcamento(id_lista)
VALUE(
	92023
);

INSERT INTO classificacao(
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
)
VALUES (
	'03.01',
	'Tribunal de Justiça',
	'02-061',
	'01-726-2031',
	'Gestão, Manutenção e Serviços ao Estado',
	'Gestão, Manutenção e Serviços ao Estado - TJ / REMUNERAÇÃO DE PESSOAL DO TRIBUNAL DE JUSTICA',
	'1',
	'500',
	'Recursos não vinculados de Impostos',
	'1'
);

INSERT INTO dotacao(
	inicial,
	creditosAdicionaisAcrescimo,
	creditosAdicionaisDescrescimos,
	atualizada,
	contingenciado,
	movLiquidaCreditosProvisao,
	movLiquidaCreditosDestaque,
	liquida
)
VALUES (
	'1770204012.00',
	'0.00',
	'375855000.00',
	'1394349012.00',
	'0.00',
	'0.00',
	'0.00',
	'1394349012.00'
);

INSERT INTO execucao(
	empenhado,
	empenhadoPorcentagem,
	liquidado,
	liquidadoPorcentagem,
	pago,
	pagoPorcentagem
)
VALUES (
	'809438150.90',
	'0.5805',
	'779438150.90',
	'0.559',
	'719438150.90',
	'0.516'
);

UPDATE classificacao
SET unidadeOrcamentariaDescricao = "a"
WHERE ()