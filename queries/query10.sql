-- Encontre os estudantes que cursaram "Sistemas de Banco de Dados" mas não "Inteligência Artificial".
-- INSERIR ESSAS DISCIPLINAS
SELECT DISTINCT a.nome
FROM historico_escolar h
JOIN alunos a ON h.ra = a.ra
WHERE h.disciplina = 'Sistemas de Banco de Dados'
AND a.ra NOT IN (
    SELECT ra
    FROM historico_escolar
    WHERE disciplina = 'Inteligência Artificial'
);
