-- Liste os cursos que são ministrados pelo professor '10', juntamente com os títulos dos cursos
SELECT p.id_professores, d.curso, d.disciplina AS Titulo
FROM disciplinas_lecionadas d
JOIN professores p ON d.nome_professor = p.nome
WHERE p.id_professores = '10';
