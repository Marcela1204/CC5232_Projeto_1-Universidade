-- Recupere os IDs dos estudantes que não estão matriculados em nenhum curso do departamento de "Ciência da Computação"
SELECT a.ra
FROM alunos a
WHERE a.curso NOT IN (
    SELECT d.curso
    FROM departamentos d
    WHERE d.curso = 'Ciência da Computação'
);
