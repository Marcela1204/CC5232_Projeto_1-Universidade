from supabase import create_client, Client
import random
import faker
from datetime import date, timedelta

# Credenciais do Supabase (use variáveis de ambiente para segurança)
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"
key = "SUA_CHAVE_SUPABASE"
supabase: Client = create_client(url, key)

# Criando uma instância do gerador de dados fictícios
fake = faker.Faker()

# Função para gerar um RA fictício
def gerar_RA():
    return "RA" + str(random.randint(1000000, 9999999))

# Criar tabelas no Supabase
def criar_tabelas():
    queries = [
        """
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
        );
        """
    ]
    
    for query in queries:
        try:
            supabase.rpc("execute_sql", {"sql": query}).execute()
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")

# Função para inserir dados fictícios
def inserir_dados():
    departamentos = ["Computação", "Engenharia", "Medicina", "Administração"]
    cursos = ["Ciência da Computação", "Engenharia Elétrica", "Medicina"]
    disciplinas = ["Algoritmos", "Circuitos", "Anatomia"]
    
    # Inserir departamentos
    for nome in departamentos:
        supabase.table("departamentos").insert({"nome": nome}).execute()
    
    # Inserir professores
    professores = []
    for _ in range(5):
        nome = fake.name()
        dept_id = random.randint(1, len(departamentos))
        res = supabase.table("professores").insert({"nome": nome, "departamento_id": dept_id}).execute()
        professores.append(res.data[0]["id"])
    
    # Inserir cursos
    for nome in cursos:
        dept_id = random.randint(1, len(departamentos))
        coord_id = random.choice(professores)
        supabase.table("cursos").insert({"nome": nome, "departamento_id": dept_id, "coordenador_id": coord_id}).execute()
    
    # Inserir alunos
    alunos = []
    for _ in range(10):
        nome = fake.name()
        ra = gerar_RA()
        curso_id = random.randint(1, len(cursos))
        semestre = random.randint(1, 10)
        res = supabase.table("alunos").insert({"nome": nome, "ra": ra, "curso_id": curso_id, "semestre_atual": semestre}).execute()
        alunos.append(res.data[0]["id"])
    
    # Inserir disciplinas
    for nome in disciplinas:
        curso_id = random.randint(1, len(cursos))
        codigo = f"DISC{random.randint(100, 999)}"
        supabase.table("disciplinas").insert({"nome": nome, "codigo": codigo, "curso_id": curso_id}).execute()
    
    # Inserir histórico escolar
    for aluno_id in alunos:
        for _ in range(5):
            disciplina_id = random.randint(1, len(disciplinas))
            professor_id = random.choice(professores)
            semestre = random.randint(1, 10)
            ano = random.randint(2020, 2024)
            nota = round(random.uniform(4, 10), 2)
            status = "Aprovado" if nota >= 5 else "Reprovado"
            supabase.table("historico_escolar").insert({"aluno_id": aluno_id, "disciplina_id": disciplina_id, "professor_id": professor_id, "semestre": semestre, "ano": ano, "nota": nota, "status": status}).execute()
    
    # Inserir TCCs
    for aluno_id in alunos[:5]:
        professor_id = random.choice(professores)
        titulo = fake.sentence()
        data_apresentacao = date.today() - timedelta(days=random.randint(0, 365*4))
        supabase.table("tccs").insert({"aluno_id": aluno_id, "professor_id": professor_id, "titulo": titulo, "data_apresentacao": data_apresentacao}).execute()
    
    print("Dados inseridos com sucesso!")

# Criar tabelas e inserir dados
criar_tabelas()
inserir_dados()

print("Tabelas criadas e populadas com sucesso no Supabase!")
