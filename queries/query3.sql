-- Mostre a matriz curricular de pelo menos 2 cursos diferentes que possuem disciplinas em comum (e.g., Ciência da Computação e Ciência de Dados). Este exercício deve ser dividido em 2 queries sendo uma para cada curso;   
SELECT id_departamento, disciplina, curso
FROM disciplinas_lecionadas
WHERE curso = 'Ciência da Computação'


SELECT id_departamento, disciplina, curso
FROM disciplinas_lecionadas
WHERE curso = 'Engenharia Elétrica'

-- A DISCIPLINA EM COMUM É ALGORITMOS