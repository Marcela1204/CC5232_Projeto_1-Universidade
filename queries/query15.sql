-- Liste os nomes dos estudantes que não cursaram nenhum curso no departamento "DEEL"
SELECT DISTINCT a.nome, a.curso
FROM alunos a
WHERE a.ra NOT IN (
    SELECT h.ra
    FROM historico_escolar h
    JOIN disciplinas_lecionadas d ON h.disciplina = d.disciplina
    JOIN departamentos dept ON d.id_departamento = dept.id_departamento
    WHERE dept.curso = 'DEEL'
);
