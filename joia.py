import random
import faker
from supabase import create_client, Client
from math import ceil

# Credenciais do Supabase
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZm95c3p6cmNuYWR0Y3FodWluIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MzExNTI1OCwiZXhwIjoyMDU4NjkxMjU4fQ.zAvSDeoZ3INAhUwSumGUCly-RTquuaYEPiPcuR4GEP4"  # api key secret


cursos = ["Ciência da Computação", "Engenharia Elétrica", "Medicina", "Administração", "Direito", "Psicologia", "Biomedicina"]
disciplinas = {
    "Ciência da Computação": ["Algoritmos", "Estruturas de Dados", "Redes de Computadores", "Banco de Dados", "Inteligência Artificial"],
    "Engenharia Elétrica": ["Circuitos Elétricos", "Sistemas Digitais", "Eletromagnetismo", "Teoria de Controle", "Máquinas Elétricas","Algoritmos"],
    "Medicina": ["Anatomia", "Fisiologia", "Bioquímica", "Farmacologia","Microbiologia","Genética"],
    "Administração": ["Gestão de Pessoas", "Marketing", "Contabilidade", "Economia", "Administração Estratégica"],
    "Direito": ["Direito Penal", "Direito Constitucional", "Direito Civil", "Direito Empresarial", "Direito Tributário"],
    "Psicologia": ["Psicologia Geral", "Psicologia do Desenvolvimento", "Psicologia Clínica", "Psicologia Organizacional", "Psicologia Educacional"],
    "Biomedicina": ["Genética", "Biotecnologia", "Microbiologia", "Imunologia", "Bioinformática"]
}
semestres = {
    "Algoritmos": 1,
    "Estruturas de Dados": 2,
    "Redes de Computadores": 5,
    "Banco de Dados": 6,
    "Inteligência Artificial": 8,
    "Circuitos Elétricos": 1,
    "Sistemas Digitais": 3,
    "Eletromagnetismo": 4,
    "Teoria de Controle": 6,
    "Máquinas Elétricas": 7,
    "Anatomia": 1,
    "Fisiologia": 2,
    "Bioquímica": 3,
    "Farmacologia": 5,
    "Microbiologia": 4,
    "Genética": 6,
    "Gestão de Pessoas": 2,
    "Marketing": 3,
    "Contabilidade": 4,
    "Economia": 5,
    "Administração Estratégica": 7,
    "Direito Penal": 1,
    "Direito Constitucional": 2,
    "Direito Civil": 3,
    "Direito Empresarial": 4,
    "Direito Tributário": 5,
    "Psicologia Geral": 1,
    "Psicologia do Desenvolvimento": 2,
    "Psicologia Clínica": 4,
    "Psicologia Organizacional": 5,
    "Psicologia Educacional": 6,
    "Biotecnologia": 3,
    "Imunologia": 5,
    "Bioinformática": 7
}

materias = []
numero_disciplinas = 0
for curso, disciplina in disciplinas.items():
    numero_disciplinas += len(disciplina)
    for materia in disciplina:
        materias.append(materia)
    #ideia sobre lista grande com todas as disciplinas, onde conforme a disciplina é adicionada para os professores ela é removida desta lista até que ela esteja vazia

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
    if num_professores > numero_disciplinas:
        print("numero de professores não pode ser maior do que os cursos disponiveis ({0})".format(numero_disciplinas))
        return
    dados = {
        "alunos": [],
        "professores": [],
        "professor_da_materia" : {},
        "tccs": [],
        "historicos_escolares": [],
        "ras" : []
    }
    usados = []
    #ras = []
    # Gerando dados de alunos
    for _ in range(num_alunos):
        nome = fake.name()
        ra = gerar_RA()
        #ras.append(ra)
        curso = random.choice(cursos)
        semestre = random.randint(1, 10)
        dados["alunos"].append({
            "nome": nome,
            "idade": random.randint(18, 30),
            "ra": ra,
            "curso": curso,
            "semestre": semestre
        })
        dados["ras"].append(ra)
        
        # Gerando TCC para cada aluno
        dados["tccs"].append(gerar_TCC(nome))

    # Gerando dados de professores
    professores = [fake.name() for _ in range(num_professores)]
    for professor in professores:
        dados["professores"].append(professor)
        #print(dados)
        ok = 0
        while ok == 0:
            #print(len(cursos))
            adicionar = random.randint(0,len(materias)-1)
            #novo = random.randint(0,len(disciplinas[cursos[adicionar]])-1)
            if len(materias) > 0:
                #dados["professor_da_materia"].append({
                #professor : materias[adicionar]
                #})
                dados["professor_da_materia"][materias[adicionar]] = professor
                #usados.append(materias[adicionar])
                materias.pop(adicionar)
                ok = 1

    #print(dados["professor_da_materia"])

    return dados

# Inserir os dados no Supabase
def inserir_no_supabase(dados):
    try:
        # Inserir alunos
        for aluno in dados["alunos"]:
            response = supabase.table('alunos').insert(aluno).execute()
            #print("Aluno inserido com sucesso:", response)

        # Inserir TCCs
        for tcc in dados["tccs"]:
            response = supabase.table('tccs').insert(tcc).execute()
            #print("TCC inserido com sucesso:", response)

        # Inserir históricos escolares
        for historico in dados["historicos_escolares"]:
            for disciplina in historico:
                response = supabase.table('historico_escolar').insert(disciplina).execute()
                #print("Histórico inserido com sucesso:", response)

        # Inserir professores
        for professor in dados["professores"]:
            response = supabase.table('professores').insert({"nome": professor}).execute()
            #print("Professor inserido com sucesso:", response)

        profs = {}
        jafoi = []
        for curso in cursos:
            for disciplina in disciplinas[curso]:
                if curso not in jafoi:
                    profs[curso] = dados["professor_da_materia"][disciplina]
                    jafoi.append(curso)
                response = supabase.table('disciplinas_lecionadas').insert({"disciplina": disciplina, "curso": curso, "professor_nome": dados["professor_da_materia"][disciplina], "coordenador" : profs[curso], "semestre_inicio" : semestres[disciplina], "ano_inicio" : ceil(semestres[disciplina]/2)}).execute()
                #print("curso inserido com sucesso:", response)
        
        for ras in dados["ras"]:
            read = supabase.table("alunos").select("*").eq("ra", ras).execute()
            disciplinas_semestre = [disciplina for disciplina, semestre in semestres.items() if semestre <= read.data[0]["semestre"] and disciplina in disciplinas[read.data[0]["curso"]]]
            #semestre = random.randint(1,10)
            passou = []
            for mat in disciplinas_semestre:
                response = supabase.table('historico_escolar').insert({"ra": ras, "disciplina" : mat, "nota" : random.randrange(4,10), "ano" : ceil(semestres[mat]/2), "semestre" : semestres[mat] }).execute()
                read2 = supabase.table("historico_escolar").select("*").eq("ra", ras).execute()
                for i in read2.data:
                    if i["nota"] < 5 and i["disciplina"] not in passou:
                        passou.append(i["disciplina"])
                        response = supabase.table('historico_escolar').insert({"ra": ras, "disciplina" : mat, "nota" : random.randrange(5,10), "ano" : ceil((i["semestre"]+1)/2), "semestre" : i["semestre"]+1}).execute()
        
        for curso in cursos:
            leitura = supabase.table("disciplinas_lecionadas").select("*").eq("curso",curso).execute()
            response = supabase.table('departamentos').insert({"nome" : curso,"curso" : curso, "id_departamento" : departamentos[curso], "coordenador" : leitura.data[0]["coordenador"], "chefe_departamento" :leitura.data[1]["professor_nome"]}).execute()


            

    except Exception as e:
        print(e)

# Gerando dados fictícios de 15 alunos e 37 professores
#for i in range(0,36):
dados_ficticios = gerar_dados_ficticios(15, 37) #nao colocar valor menor q 37, preguiça de arrumar
    #print("Gerando dados fictícios para {0} professores".format(i))

# Inserir no Supabase
inserir_no_supabase(dados_ficticios)
#print(dados_ficticios)
print("OK!")