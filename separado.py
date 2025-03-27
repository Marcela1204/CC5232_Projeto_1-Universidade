import random
import faker
from supabase import create_client, Client

# Credenciais do Supabase
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "your-api-key"  # Substitua com sua chave de API

cursos = ["Ciência da Computação", "Engenharia Elétrica", "Medicina", "Administração", "Direito", "Psicologia", "Biomedicina"]
disciplinas = {
    "Ciência da Computação": ["Algoritmos", "Estruturas de Dados", "Redes de Computadores", "Banco de Dados", "Inteligência Artificial"],
    "Engenharia Elétrica": ["Circuitos Elétricos", "Sistemas Digitais", "Eletromagnetismo", "Teoria de Controle", "Máquinas Elétricas","Algoritmos"],
    "Medicina": ["Anatomia", "Fisiologia", "Bioquímica", "Microbiologia", "Farmacologia","Genética"],
    "Administração": ["Gestão de Pessoas", "Marketing", "Contabilidade", "Economia", "Administração Estratégica"],
    "Direito": ["Direito Penal", "Direito Constitucional", "Direito Civil", "Direito Empresarial", "Direito Tributário"],
    "Psicologia": ["Psicologia Geral", "Psicologia do Desenvolvimento", "Psicologia Clínica", "Psicologia Organizacional", "Psicologia Educacional"],
    "Biomedicina": ["Genética", "Biotecnologia", "Microbiologia", "Imunologia", "Bioinformática"]
}

departamentos = {
    "Ciência da Computação": "DCOMP",
    "Engenharia Elétrica": "DEEL",
    "Medicina": "DMED",
    "Administração": "DADM",
    "Direito": "DDIR",
    "Psicologia": "DPSI",
    "Biomedicina": "DBIO"
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

    alunos_existentes = set()
    professores_existentes = set()

    # Gerando dados de alunos
    for _ in range(num_alunos):
        nome = fake.name()
        ra = gerar_RA()
        while ra in alunos_existentes:  # Garantir que o RA seja único
            ra = gerar_RA()
        alunos_existentes.add(ra)

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
    for _ in range(num_professores):
        nome = fake.name()
        if nome not in professores_existentes:  # Garantir que o nome do professor seja único
            professores_existentes.add(nome)
            dados["professores"].append(nome)

    return dados

# Inserir os dados no Supabase com validações
def inserir_no_supabase(dados):
    try:
        # Verificando dados antes de inserir

        # Inserir alunos
        for aluno in dados["alunos"]:
            # Verificar se o aluno já existe no banco (verificação do RA)
            existing_aluno = supabase.table('alunos').select('ra').eq('ra', aluno['ra']).execute()
            if existing_aluno.data:
                print(f"Aluno com RA {aluno['ra']} já existe!")
            else:
                response = supabase.table('alunos').insert(aluno).execute()
                print(f"Aluno {aluno['nome']} inserido com sucesso.")

        # Inserir TCCs
        for tcc in dados["tccs"]:
            response = supabase.table('tccs').insert(tcc).execute()
            print(f"TCC de {tcc['aluno_nome']} inserido com sucesso.")

        # Inserir professores
        for professor in dados["professores"]:
            # Verificar se o professor já existe
            existing_professor = supabase.table('professores').select('nome').eq('nome', professor).execute()
            if existing_professor.data:
                print(f"Professor {professor} já existe!")
            else:
                response = supabase.table('professores').insert({"nome": professor}).execute()
                print(f"Professor {professor} inserido com sucesso.")

        # Inserir disciplinas lecionadas, garantindo que não haja duplicidade
        for curso in cursos:
            for disciplina in disciplinas[curso]:
                # Verificar se a disciplina já foi inserida para esse curso
                existing_disciplina = supabase.table('disciplinas_lecionadas').select('disciplina', 'curso').eq('disciplina', disciplina).eq('curso', curso).execute()
                if existing_disciplina.data:
                    print(f"Disciplina {disciplina} já foi inserida para o curso {curso}.")
                else:
                    response = supabase.table('disciplinas_lecionadas').insert({"disciplina": disciplina, "curso": curso}).execute()
                    print(f"Disciplina {disciplina} inserida para o curso {curso}.")

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

# Gerando dados fictícios de 15 alunos e 5 professores
dados_ficticios = gerar_dados_ficticios(15, 5)

# Inserir no Supabase com validação
inserir_no_supabase(dados_ficticios)

print("Dados inseridos com sucesso no Supabase!")
