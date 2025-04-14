-- Mostre todo o histórico escolar de um aluno que teve reprovação em uma disciplina, retornando inclusive a reprovação em um semestre e a aprovação no semestre seguinte;   
SELECT 
    h1.ra,
    h1.disciplina,
    h1.ano AS ano_reprovacao,
    h1.semestre AS semestre_reprovacao,
    h1.nota AS nota_reprovacao,
    h2.ano AS ano_aprovacao,
    h2.semestre AS semestre_aprovacao,
    h2.nota AS nota_aprovacao
FROM 
    historico_escolar h1
JOIN 
    historico_escolar h2 
    ON h1.ra = h2.ra
    AND h1.disciplina = h2.disciplina
    AND (
        (h2.ano > h1.ano)
        OR (h2.ano = h1.ano AND h2.semestre > h1.semestre)
    )
WHERE 
    h1.nota < 5 -- Reprovação
    AND h2.nota >= 5 -- Aprovação
    AND h1.ra = 'RA4685719' -- Coloquei um aluno específico, mas é possível verificar vários
ORDER BY 
    h1.ra, h1.disciplina, h1.ano, h1.semestre;

