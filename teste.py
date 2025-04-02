from supabase import create_client

# URL e chave do Supabase
url = "https://nlfoyszzrcnadtcqhuin.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZm95c3p6cmNuYWR0Y3FodWluIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MzExNTI1OCwiZXhwIjoyMDU4NjkxMjU4fQ.zAvSDeoZ3INAhUwSumGUCly-RTquuaYEPiPcuR4GEP4"  # api key secret

# Criação do cliente Supabase
supabase = create_client(url, key)

# Consulta para obter os dados
response = supabase.table("alunos").select("*").execute()  # Substitua 'sua_tabela' pelo nome da tabela

# Verifica se a consulta foi bem-sucedida
#if response.error is None:
dados = response.data
    # Inicializa listas para armazenar os valores
lista_coluna1 = [item['nome'] for item in dados]  # Substitua 'coluna1' pelas colunas reais
lista_coluna2 = [item['curso'] for item in dados]  # Substitua 'coluna2' pelas colunas reais

print(lista_coluna1)
print(lista_coluna2)
#else:
#print("Erro ao buscar dados:", response.status_code, response.json())