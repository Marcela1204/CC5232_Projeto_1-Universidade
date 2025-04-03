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
<br>

## Execução do Projeto
<br>

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

