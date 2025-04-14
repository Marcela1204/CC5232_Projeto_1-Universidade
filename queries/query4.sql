-- Para um determinado aluno, mostre os códigos e nomes das diciplinas já cursadas junto com os nomes dos professores que lecionaram a disciplina para o aluno; 
SELECT 
    h.disciplina AS Nome_Disciplina,
    d.id_disciplinas AS Codigo_Disciplina,
    d.nome_professor
FROM 
    historico_escolar h
JOIN 
    alunos a ON h.ra = a.ra
JOIN 
    disciplinas_lecionadas d 
    ON h.disciplina = d.disciplina
    AND h.ano = d.ano_inicio
    AND h.semestre = d.semestre_inicio
    AND a.curso = d.curso
WHERE 
    a.ra = 'RA4685719'; -- Coloquei um aluno específico, mas é possível verificar vários
