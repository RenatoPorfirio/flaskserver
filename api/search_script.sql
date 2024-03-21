SELECT * FROM lista_orcamentos;
SELECT * FROM orcamento;
SELECT * FROM classificacao;
SELECT * FROM dotacao;
SELECT * FROM execucao;

SELECT *
FROM lista_orcamentos
CROSS JOIN orcamento
USING (id_lista)
CROSS JOIN classificacao
USING (id_orcamento)
CROSS JOIN dotacao
USING (id_orcamento)
CROSS JOIN execucao
USING (id_orcamento)
WHERE (2022 <= ano AND ano <= 2023);