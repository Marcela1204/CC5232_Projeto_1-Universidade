CREATE TABLE IF NOT EXISTS alunos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            ra VARCHAR(20) UNIQUE NOT NULL,
            curso_id INT REFERENCES cursos(id),
            semestre_atual INT CHECK (semestre_atual BETWEEN 1 AND 10)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS professores (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            departamento_id INT REFERENCES departamentos(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS departamentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) UNIQUE NOT NULL,
            chefe_id INT REFERENCES professores(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS cursos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) UNIQUE NOT NULL,
            departamento_id INT REFERENCES departamentos(id),
            coordenador_id INT REFERENCES professores(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS disciplinas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) UNIQUE NOT NULL,
            codigo VARCHAR(20) UNIQUE NOT NULL,
            curso_id INT REFERENCES cursos(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS historico_escolar (
            id SERIAL PRIMARY KEY,
            aluno_id INT REFERENCES alunos(id),
            disciplina_id INT REFERENCES disciplinas(id),
            professor_id INT REFERENCES professores(id),
            semestre INT,
            ano INT,
            nota NUMERIC(4,2),
            status VARCHAR(10) CHECK (status IN ('Aprovado', 'Reprovado'))
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS historico_lecionadas (
            id SERIAL PRIMARY KEY,
            professor_id INT REFERENCES professores(id),
            disciplina_id INT REFERENCES disciplinas(id),
            semestre INT,
            ano INT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS tccs (
            id SERIAL PRIMARY KEY,
            aluno_id INT REFERENCES alunos(id),
            professor_id INT REFERENCES professores(id),
            titulo VARCHAR(255) NOT NULL,
            data_apresentacao DATE NOT NULL


---------------------------------------------------------------------

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    departamento_id INT REFERENCES departamentos(id)
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL,
    departamento_id INT REFERENCES departamentos(id),
    coordenador_id INT REFERENCES professores(id)
);

CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    ra VARCHAR(50) UNIQUE NOT NULL,
    curso_id INT REFERENCES cursos(id),
    semestre_atual INT NOT NULL
);

CREATE TABLE disciplinas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    curso_id INT REFERENCES cursos(id)
);

CREATE TABLE historico_escolar (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(id),
    disciplina_id INT REFERENCES disciplinas(id),
    professor_id INT REFERENCES professores(id),
    semestre INT NOT NULL,
    ano INT NOT NULL,
    nota NUMERIC(4,2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE tccs (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(id),
    professor_id INT REFERENCES professores(id),
    titulo TEXT NOT NULL,
    data_apresentacao DATE NOT NULL
);
