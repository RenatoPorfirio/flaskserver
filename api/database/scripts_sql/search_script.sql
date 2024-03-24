SELECT * FROM lista_orcamentos;
SELECT * FROM orcamento;
SELECT * FROM classificacao;
SELECT * FROM dotacao;
SELECT * FROM execucao;

SELECT *
FROM lista_orcamentos
CROSS JOIN orcamento
USING (id_lista)
LEFT JOIN classificacao
USING (id_orcamento)
LEFT JOIN dotacao
USING (id_orcamento)
LEFT JOIN execucao
USING (id_orcamento)
ORDER BY ano,mes ASC;
