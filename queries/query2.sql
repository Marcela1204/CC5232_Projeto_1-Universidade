-- Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto; 
SELECT 
    orientador AS Professor_do_Projeto,
    nome_aluno AS Nome_do_Aluno,
    titulo AS Titulo_do_Projeto
FROM tccs
WHERE orientador = 'Lisa Mayer' -- Coloquei um professor específico, mas é possível verificar vários
