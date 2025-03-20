import random
import faker
from supabase import create_client, Client

# Credenciais do Supabase
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZm95c3p6cmNuYWR0Y3FodWluIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MjE3MDc2OSwiZXhwIjoyMDU3NzQ2NzY5fQ.6T2EtJnE6hz-n7ZJDs59bCZXoxDZ-Pjk_j-JC7DnL0o"  # Substitua com a chave da API


cursos = ["Ciência da Computação", "Engenharia Elétrica", "Medicina", "Administração", "Direito", "Psicologia", "Biomedicina"]
disciplinas = {
    "Ciência da Computação": ["Algoritmos", "Estruturas de Dados", "Redes de Computadores", "Banco de Dados", "Inteligência Artificial"],
    "Engenharia Elétrica": ["Circuitos Elétricos", "Sistemas Digitais", "Eletromagnetismo", "Teoria de Controle", "Máquinas Elétricas"],
    "Medicina": ["Anatomia", "Fisiologia", "Bioquímica", "Microbiologia", "Farmacologia"],
    "Administração": ["Gestão de Pessoas", "Marketing", "Contabilidade", "Economia", "Administração Estratégica"],
    "Direito": ["Direito Penal", "Direito Constitucional", "Direito Civil", "Direito Empresarial", "Direito Tributário"],
    "Psicologia": ["Psicologia Geral", "Psicologia do Desenvolvimento", "Psicologia Clínica", "Psicologia Organizacional", "Psicologia Educacional"],
    "Biomedicina": ["Genética", "Biotecnologia", "Microbiologia", "Imunologia", "Bioinformática"]
}

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

# Criando uma instância do gerador de dados fictícios
fake = faker.Faker()

# Função para gerar um RA fictício (número aleatório com o padrão de RA)
def gerar_RA():
    return "RA" + str(random.randint(1000000, 9999999))

# Função para gerar dados de TCCs com a data formatada corretamente
def gerar_TCC(aluno_nome):
    titulos = ["Análise de Algoritmos", "Estudo sobre Redes Neurais", "Impacto Ambiental de Máquinas Elétricas", "Efeitos Psicológicos na Educação", "Análise de Casos Jurídicos no Brasil"]
    tcc_data = fake.date_this_decade()  # Gera uma data
    return {
        "aluno_nome": aluno_nome,
        "titulo": random.choice(titulos),
        "orientador": fake.name(),
        "data_apresentacao": tcc_data.isoformat()  # Converte para o formato YYYY-MM-DD
    }

# Função para gerar dados fictícios de alunos, professores, TCCs e históricos
def gerar_dados_ficticios(num_alunos, num_professores):
    dados = {
        "alunos": [],
        "professores": [],
        "tccs": [],
        "historicos_escolares": [],
    }

    # Gerando dados de alunos
    for _ in range(num_alunos):
        nome = fake.name()
        ra = gerar_RA()
        curso = random.choice(cursos)
        semestre = random.randint(1, 10)
        dados["alunos"].append({
            "nome": nome,
            "idade": random.randint(18, 30),
            "ra": ra,
            "curso": curso,
            "semestre": semestre
        })
        
        # Gerando TCC para cada aluno
        dados["tccs"].append(gerar_TCC(nome))

    # Gerando dados de professores
    professores = [fake.name() for _ in range(num_professores)]
    for professor in professores:
        dados["professores"].append(professor)
        #print(dados)

    return dados

# Inserir os dados no Supabase
def inserir_no_supabase(dados):
    # Inserir alunos
    for aluno in dados["alunos"]:
        supabase.table('teste_codigo.alunos').insert(aluno).execute()

    # Inserir TCCs
    for tcc in dados["tccs"]:
        supabase.table('teste_codigo.tccs').insert(tcc).execute()

    # Inserir históricos escolares
    for historico in dados["historicos_escolares"]:
        for disciplina in historico:
            supabase.table('teste_codigo.historico_escolar').insert(disciplina).execute()

    # Inserir professores
    for professor in dados["professores"]:
        supabase.table('teste_codigo.professores').insert({"nome": professor}).execute()

# Gerando dados fictícios de 5 alunos e 3 professores
dados_ficticios = gerar_dados_ficticios(15, 5)

# Inserir no Supabase
inserir_no_supabase(dados_ficticios)

print("Dados inseridos com sucesso no Supabase!")
