-- Encontre os nomes de todos os estudantes que cursaram "Banco de Dados" (course_id = 'CS-101').
SELECT a.nome
FROM historico_escolar h
JOIN alunos a ON h.RA = a.RA
WHERE h.disciplina = 'Banco de Dados';
