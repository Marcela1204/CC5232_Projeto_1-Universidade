<div align="center">
  
# UNIVERSIDADE
## PROJETO 1: BANCO DE DADOS

</div>
<br>

## Introdução
Projeto criado por:
* [Lucas Kerr](https://github.com/Adelgrin) | RA: 221230329
* [Marcela Nalesso](https://github.com/Marcela1204) | RA: 222220113

* Link do git hub: https://github.com/Marcela1204/CC5232_Projeto_1-Universidade/tree/main
* Link do git hub2: https://github.com/Marcela1204/CC5232_Projeto_1-Universidade.git
<br>

## Descrição do Projeto
- **Objetivo**   
> O objetivo deste projeto é desenvolver e implementar um sistema de banco de dados para uma universidade. O sistema deve ser capaz de armazenar e gerenciar informações essenciais relacionadas a alunos, professores, departamentos, cursos e disciplinas. Além disso, deve contemplar o registro de históricos escolares de alunos, histórico de disciplinas lecionadas por professores e registros de Trabalhos de Conclusão de Curso (TCCs), considerando tanto os grupos de alunos envolvidos quanto os professores orientadores.
<br>

- **Tabelas** (Mudar a descrição das tabelas)   
> O banco de dados deverá conter as seguintes informações:   
1. Alunos: RA, Nome, Idade, Curso, Semestre.   
2. Professores: ID_Professores, Nome, ID_Departamento.   
3. Departamentos: ID_Departamento, Nome, Curso, Coordenador, Chefe de Departamento.     
4. Disciplinas Lecionadas: ID_Disciplinas, Nome do Professor, Disciplina, Curso, Ano de Início, Semestre de Início, Coordenador.   
5. Histórico Escolar: ID_Histórico, RA, Disciplina, Nota, Ano, Semestre.   
6. TCCs Apresentados: ID_TCCs, Nome do Aluno, Título, Orientador, Data de Apresentação.

- **Queries** (Colocar as outras queries)
> Para demonstrar o funcionamento do banco, foram usadas as seguintes queries:   
1. Mostre todo o histórico escolar de um aluno que teve reprovação em uma disciplina, retornando inclusive a reprovação em um semestre e a aprovação no semestre seguinte;   
2. Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto;    
3. Mostre a matriz curicular de pelo menos 2 cursos diferentes que possuem disciplinas em comum (e.g., Ciência da Computação e Ciência de Dados). Este exercício deve ser dividido em 2 queries sendo uma para cada curso;    
4. Para um determinado aluno, mostre os códigos e nomes das diciplinas já cursadas junto com os nomes dos professores que lecionaram a disciplina para o aluno;    
5. Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordena e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum"
6. (Tem outras 10 queries pra colocar)

## Execução do Projeto
Passo a passo para exceutar o projeto: 

### Primeiro passo: Criação do banco de dados
- Através do arquivo 'tabela.sql', abra um novo snippet, cole o código e execute. Você verá o banco criado quando ir a aba table editor e selecionar o schema 'public'

### Segundo passo: Executar código para criação dos dados
- Abra o Codespace do github, instale as bibliotecas (terminal) 'faker' e 'supabase' e execute o código em python
  OBS: Verifique a URL e API Keys do seu banco e substitua no código nas variáveis 'url' e 'key', respectivamente, antes de executar o código.

### Terceiro passo: 
- Com as informações prontas, execute as queries determinadas pelo projeto na aba SQL editor.

COLOCAR IMAGENS/VÍDEO PRA MOSTRAR COMO FUNCIONA

## Diagramas

### MER
![image](https://github.com/user-attachments/assets/6c515ff0-5609-4ef7-869b-50e25009f397)

### MR
(Colocar os dados e observações)
#### Tabela Alunos
<table border="1">
  <tr>
    <th style="text-align: right;">RA</th>
    <th style="text-align: right;">Nome</th>
    <th style="text-align: right;">Idade</th>
    <th style="text-align: right;">Curso</th>
    <th style="text-align: right;">Semestre</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">3</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
    <td style="text-align: right;">Ciência da Computação</td>
    <td style="text-align: right;">4</td>
  </tr>
</table>

#### Tabela Departamentos
<table border="1">
  <tr>
    <th style="text-align: right;">ID_Departamento</th>
    <th style="text-align: right;">Nome</th>
    <th style="text-align: right;">Curso</th>
    <th style="text-align: right;">Chefe_Departamento</th>
    <th style="text-align: right;">Coordenador</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">3</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
    <td style="text-align: right;">Ciência da Computação</td>
    <td style="text-align: right;">4</td>
  </tr>
</table>

#### Tabela Disciplinas
<table border="1">
  <tr>
    <th style="text-align: right;">ID_Disciplinas</th>
    <th style="text-align: right;">Nome_Disciplina</th>
    <th style="text-align: right;">Curso</th>
    <th style="text-align: right;">Semestre_Inicio</th>
    <th style="text-align: right;">Coordenador</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">3</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
    <td style="text-align: right;">Ciência da Computação</td>
    <td style="text-align: right;">4</td>
  </tr>
</table>

#### Tabela Disciplinas Lecionadas
<table border="1">
  <tr>
    <th style="text-align: right;">ID_Disciplinas</th>
    <th style="text-align: right;">ID_professores</th>
    <th style="text-align: right;">Ano_Inicio</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
  </tr>
</table>

#### Tabela Historico Escolar
<table border="1">
  <tr>
    <th style="text-align: right;">ID_Historico</th>
    <th style="text-align: right;">RA</th>
    <th style="text-align: right;">Disciplina</th>
    <th style="text-align: right;">Semestre</th>
    <th style="text-align: right;">Nota</th>
    <th style="text-align: right;">Ano</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">2</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">3</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
    <td style="text-align: right;">Ciência da Computação</td>
    <td style="text-align: right;">4</td>
    <td style="text-align: right;">2</td>
  </tr>
</table>

#### Tabela Professores
<table border="1">
  <tr>
    <th style="text-align: right;">ID_Professores</th>
    <th style="text-align: right;">Nome</th>
    <th style="text-align: right;">ID_Departamento</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
  </tr>
</table>

#### Tabela TCCs
<table border="1">
  <tr>
    <th style="text-align: right;">ID_TCCs</th>
    <th style="text-align: right;">RA</th>
    <th style="text-align: right;">Nome_Aluno</th>
    <th style="text-align: right;">Orientador</th>
    <th style="text-align: right;">Titulo</th>
    <th style="text-align: right;">Data_Apresentacao</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
    <td style="text-align: right;">25</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">2</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
    <td style="text-align: right;">18</td>
    <td style="text-align: right;">Medicina</td>
    <td style="text-align: right;">3</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
    <td style="text-align: right;">23</td>
    <td style="text-align: right;">Ciência da Computação</td>
    <td style="text-align: right;">4</td>
  </tr>
</table>

#### Tabela TCC Orientador
<table border="1">
  <tr>
    <th style="text-align: right;">ID_TCCs</th>
    <th style="text-align: right;">ID_Professores</th>
  </tr>
  <tr>
    <td style="text-align: right;">RA6568465</td>
    <td style="text-align: right;">Hannah Hill</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA2151041</td>
    <td style="text-align: right;">Sarah Wilcox</td>
  </tr>
  <tr>
    <td style="text-align: right;">RA7412121</td>
    <td style="text-align: right;">Christina Garcia</td>
  </tr>
</table>

***

