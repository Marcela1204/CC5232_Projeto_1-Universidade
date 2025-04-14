CREATE SCHEMA IF NOT EXISTS public;
SET search_path TO public;

-- Tabela de Alunos
CREATE TABLE alunos (
    ra TEXT PRIMARY KEY,
    nome TEXT,
    idade INT,
    curso TEXT,
    semestre INT
);

-- Tabela de Professores
CREATE TABLE professores (
    id_professores SERIAL PRIMARY KEY,
    nome TEXT,
    id_departamento TEXT  -- será vinculada depois
);

-- Tabela de Disciplinas Lecionadas por Professores
CREATE TABLE disciplinas_lecionadas (
    id_disciplinas SERIAL PRIMARY KEY,
    nome_professor TEXT,
    disciplina TEXT,
    curso TEXT,
    ano_inicio INT,
    semestre_inicio INT,
    coordenador TEXT,
    id_departamento TEXT
);

-- Tabela de Departamentos (sem FK no início)
CREATE TABLE departamentos (
    id_departamento TEXT PRIMARY KEY,
    chefe_departamento TEXT,
    curso TEXT,
    coordenador TEXT
);

-- Tabela de TCCs
CREATE TABLE tccs (
    id_tccs SERIAL PRIMARY KEY,
    nome_aluno TEXT,
    titulo TEXT,
    orientador TEXT,
    data_apresentacao DATE,
    ra TEXT,
    FOREIGN KEY (ra) REFERENCES alunos(ra)
);

-- Tabela de Histórico Escolar
CREATE TABLE historico_escolar (
    id_historico SERIAL PRIMARY KEY,
    disciplina TEXT,
    nota FLOAT,
    ano INT,
    semestre INT,
    ra TEXT,
    FOREIGN KEY (ra) REFERENCES alunos(ra)
);

-- Adicionando agora as Foreign Keys que causavam problemas
ALTER TABLE professores
    ADD CONSTRAINT fk_professores_departamento
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento);

ALTER TABLE disciplinas_lecionadas
    ADD CONSTRAINT fk_disciplinas_departamento
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento);
