CREATE SCHEMA IF NOT EXISTS public;
SET search_path TO public;

-- Tabela de Alunos
create table alunos (
    id serial primary key,
    nome text,
    idade int,
    ra text unique,
    curso text,
    semestre int
);

-- Tabela de Professores
create table professores (
    id serial primary key,
    nome text,
    id_departamento text
);

-- Tabela de TCCs
create table tccs (
    id serial primary key,
    aluno_nome text,
    titulo text,
    orientador text,
    data_apresentacao date
);

-- Tabela de Histórico Escolar
create table historico_escolar (
    id serial primary key,
    ra text,
    disciplina text,
    nota float,
    ano int,
    semestre int
);

-- Tabela de Disciplinas Lecionadas por Professores
create table disciplinas_lecionadas (
    id serial primary key,
    professor_nome text,
    disciplina text,
    curso text,
    ano_inicio int,
    semestre_inicio int,
    coordenador text
);

create table departamentos (
    id serial primary key,
    chefe_departamento text,
    nome text,
    id_departamento text,
    disciplina text,
    coordenador text
);
