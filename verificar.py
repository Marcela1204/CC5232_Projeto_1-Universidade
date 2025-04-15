from supabase import create_client, Client

# Credenciais do Supabase
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZm95c3p6cmNuYWR0Y3FodWluIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MzExNTI1OCwiZXhwIjoyMDU4NjkxMjU4fQ.zAvSDeoZ3INAhUwSumGUCly-RTquuaYEPiPcuR4GEP4"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)


readAlunos = supabase.table("alunos").select("*").execute()
readDepartamentos = supabase.table("departamentos").select("*").execute()
readDisciplinas = supabase.table("disciplinas_lecionadas").select("*").execute()
readHistorico = supabase.table("historico_escolar").select("*").execute()
readProfessores = supabase.table("professores").select("*").execute()
readTccs = supabase.table("tccs").select("*").execute()
for i in readAlunos.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela alunos".format(j))
            break
print("Alunos ok!")
        #print(i[j])
for i in readDepartamentos.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela departamentos".format(j))
            break
print("Departamentos ok!")
for i in readDisciplinas.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela disciplinas_lecionadas".format(j))
            break
print("Disciplinas ok!")
for i in readHistorico.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela historico_escolar".format(j))
            break
print("Historico ok!")
for i in readProfessores.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela professores".format(j))
            break
print("Professores ok!")
for i in readTccs.data:
    for j in i:
        if i[j] == "":
            print("Campo vazio {} na tabela tccs".format(j))
            break
print("Tccs ok!")