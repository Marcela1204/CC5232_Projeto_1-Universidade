-- Encontre os nomes de todos os estudantes que cursaram "Banco de Dados" (course_id = 'CS-101').
SELECT DISTINCT a.nome, a.ra
FROM historico_escolar h
JOIN alunos a ON h.ra = a.ra
JOIN disciplinas_lecionadas d ON h.disciplina = d.disciplina
WHERE d.disciplina = 'Banco de Dados';
