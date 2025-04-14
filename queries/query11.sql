-- Recupere os nomes dos estudantes que cursaram disciplinas do departamento de "Matemática".
SELECT DISTINCT a.nome
-- SELECT DISTINCT a.nome, dl.disciplina -> Pra saber quais disciplinas eles cursaram
FROM historico_escolar h
JOIN alunos a ON h.ra = a.ra
JOIN disciplinas_lecionadas dl ON h.disciplina = dl.disciplina
JOIN departamentos d ON dl.id_departamento = d.id_departamento
WHERE d.id_departamento = 'DMAT';
