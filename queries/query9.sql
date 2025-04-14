-- Encontre os estudantes que cursaram "Ciência da Computação" ou "Engenharia Elétrica".
SELECT DISTINCT a.nome, a.curso
FROM historico_escolar h
JOIN alunos a ON h.ra = a.ra
WHERE a.curso IN ('Ciência da Computação', 'Engenharia Elétrica');
