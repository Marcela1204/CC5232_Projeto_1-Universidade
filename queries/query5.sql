-- Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordena e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum"

-- O objetivo aqui é listar todos os professores que são coordenadores ou chefes de departamento
SELECT 
    COALESCE(d.coordenador, 'nenhum') AS nome_professor,
    COALESCE(CAST(p.id_departamento AS TEXT), 'nenhum') AS nome_departamento,
    COALESCE(d.curso, 'nenhum') AS curso
FROM 
    departamentos d
LEFT JOIN 
    professores p ON d.coordenador = p.nome

UNION

SELECT 
    COALESCE(d.chefe_departamento, 'nenhum') AS nome_professor,
    COALESCE(CAST(p.id_departamento AS TEXT), 'nenhum') AS nome_departamento,
    COALESCE(d.curso, 'nenhum') AS curso
FROM 
    departamentos d
LEFT JOIN 
    professores p ON d.chefe_departamento = p.nome;

