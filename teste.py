from supabase import create_client, Client
import random
import faker
from datetime import date, timedelta

# Credenciais do Supabase (use variáveis de ambiente para segurança)
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZm95c3p6cmNuYWR0Y3FodWluIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MjE3MDc2OSwiZXhwIjoyMDU3NzQ2NzY5fQ.6T2EtJnE6hz-n7ZJDs59bCZXoxDZ-Pjk_j-JC7DnL0o"  # Substitua com a chave da API
supabase: Client = create_client(url, key)

# Criando uma instância do gerador de dados fictícios
fake = faker.Faker()

# Função para gerar um RA fictício
def gerar_RA():
    return "RA" + str(random.randint(1000000, 9999999))

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

# Inserir dados fictícios
inserir_dados()

print("Dados populados com sucesso no Supabase!")
