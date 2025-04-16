-- Liste os cursos que foram ministrados pelos professores '10' e '11'
SELECT DISTINCT p.id_professores, d.curso
FROM disciplinas_lecionadas d
JOIN professores p ON d.nome_professor = p.nome
WHERE p.id_professores IN ('10', '11');
