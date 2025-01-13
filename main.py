import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    layout="wide",
)


#### Lendo banco de dados CSV
## sexto ano
df = pd.read_csv('NotasSextoAno.csv')
df['Scores 1'] = (df['Nota 1'] - df['Nota 1'].mean()) / df['Nota 1'].std()
df['Scores 2'] = (df['Nota 2'] - df['Nota 2'].mean()) / df['Nota 2'].std()
df['Scores 3'] = (df['Nota 3'] - df['Nota 3'].mean()) / df['Nota 3'].std()
df_table = df[['Nome','Scores 1', 'Scores 2', 'Scores 3']]
df['Média Anual'] = df[['Nota 1', 'Nota 2', 'Nota 3']].mean(axis=1)
## setimo ano
df1 = pd.read_csv('NotasSetimoAno.csv')
df1['Scores 1'] = (df1['Nota 1'] - df1['Nota 1'].mean()) / df1['Nota 1'].std()
df1['Scores 2'] = (df1['Nota 2'] - df1['Nota 2'].mean()) / df1['Nota 2'].std()
df1['Scores 3'] = (df1['Nota 3'] - df1['Nota 3'].mean()) / df1['Nota 3'].std()
df1_table = df1[['Nome','Scores 1', 'Scores 2', 'Scores 3']]
df1['Média Anual'] = df1[['Nota 1', 'Nota 2', 'Nota 3']].mean(axis=1)
## oitavo ano
df2 = pd.read_csv('NotasOitavoAno.csv')
df2['Scores 1'] = (df2['Nota 1'] - df2['Nota 1'].mean()) / df2['Nota 1'].std()
df2['Scores 2'] = (df2['Nota 2'] - df2['Nota 2'].mean()) / df2['Nota 2'].std()
df2['Scores 3'] = (df2['Nota 3'] - df2['Nota 3'].mean()) / df2['Nota 3'].std()
df2_table = df2[['Nome','Scores 1', 'Scores 2', 'Scores 3']]
df2['Média Anual'] = df2[['Nota 1', 'Nota 2', 'Nota 3']].mean(axis=1)
## Nono ano
df3 = pd.read_csv('NotasNonoAno.csv')
df3['Scores 1'] = (df3['Nota 1'] - df3['Nota 1'].mean()) / df3['Nota 1'].std()
df3['Scores 2'] = (df3['Nota 2'] - df3['Nota 2'].mean()) / df3['Nota 2'].std()
df3['Scores 3'] = (df3['Nota 3'] - df3['Nota 3'].mean()) / df3['Nota 3'].std()
df3_table = df3[['Nome','Scores 1', 'Scores 2', 'Scores 3']]
df3['Média Anual'] = df3[['Nota 1', 'Nota 2', 'Nota 3']].mean(axis=1)

#df = pd.DataFrame(
#    np.random.rand(30,9),
#    columns=['Nota 1','Plataforma 1', 'Nota 2', 'Plataforma 2', 'Nota 3', 'Plataforma 3', 'Recuperação 1', 'Recuperação 2', 'Recuperação 3']
#)


st.sidebar.title("Sistema de Análise de notas")

st.sidebar.header("Ano Letivo de 2024")
st.sidebar.text(" Disciplina de Matemática")
###### SEXTO ANO
if st.sidebar.button("Sexto Ano"):
    with st.expander("Notas Primeiro trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df,x = 'Nome', y=['Nota 1', 'Plataforma 1'],stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df, x='Nome', y=['Scores 1'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Segundo trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df, x='Nome', y=['Nota 2', 'Plataforma 2'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df, x='Nome', y=['Scores 2'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Terceiro trimestre", False):
        st.bar_chart(df,x='Nome', y=['Nota 1', 'Plataforma 1'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df['Nota 1'])))
    col1, col2, col3, col4 = st.columns(4, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Nota 1'].mean(), 2)))
    with col2:
        st.metric(label="Nota Paraná", value=str(round(df['Nota 1'].mean(), 2)))
    with col3:
        st.metric(label="Plataforma", value=str(round(df['Nota 1'].mean(), 2)))
    with col4:
        st.metric(label="Score 1", value=str(round(df['Scores 1'].mean(), 2)))
    st.text('')
    st.bar_chart(df, x='Nome', y=['Média Anual'], stack=False)
    st.bar_chart(df, x='Nome', y=['Plataforma 1', 'Plataforma 2', 'Plataforma 3'],
                 stack=False)

###### SEXTO ANO
if st.sidebar.button("Sétimo Ano"):
    with st.expander("Notas Primeiro trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df1,x = 'Nome', y=['Nota 1', 'Plataforma 1'],stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df1['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df1['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df1['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df1, x='Nome', y=['Scores 1'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df1_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Segundo trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df1, x='Nome', y=['Nota 2', 'Plataforma 2'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df1['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df1['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df1['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df1, x='Nome', y=['Scores 2'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df1_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Terceiro trimestre", False):
        st.bar_chart(df1,x='Nome', y=['Nota 1', 'Plataforma 1'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df1['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df1['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df1['Nota 1'])))
    col1, col2, col3, col4 = st.columns(4, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df1['Nota 1'].mean(), 2)))
    with col2:
        st.metric(label="Nota Paraná", value=str(round(df1['Nota 1'].mean(), 2)))
    with col3:
        st.metric(label="Plataforma", value=str(round(df1['Nota 1'].mean(), 2)))
    with col4:
        st.metric(label="Score 1", value=str(round(df1['Scores 1'].mean(), 2)))
    st.text('')
    st.bar_chart(df1, x='Nome', y=['Média Anual'], stack=False)
    st.bar_chart(df1, x='Nome', y=['Plataforma 1', 'Plataforma 2', 'Plataforma 3'],
                 stack=False)

### OITAVO ANO

if st.sidebar.button("Oitavo Ano"):
    with st.expander("Notas Primeiro trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df2,x = 'Nome', y=['Nota 1', 'Plataforma 1'],stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df2['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df2['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df2['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df2, x='Nome', y=['Scores 1'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df2_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Segundo trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df2, x='Nome', y=['Nota 2', 'Plataforma 2'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df2['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df2['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df2['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df2, x='Nome', y=['Scores 2'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df2_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Terceiro trimestre", False):
        st.bar_chart(df2,x='Nome', y=['Nota 1', 'Plataforma 1'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df2['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df2['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df2['Nota 1'])))
    col1, col2, col3, col4 = st.columns(4, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df2['Nota 1'].mean(), 2)))
    with col2:
        st.metric(label="Nota Paraná", value=str(round(df2['Nota 1'].mean(), 2)))
    with col3:
        st.metric(label="Plataforma", value=str(round(df2['Nota 1'].mean(), 2)))
    with col4:
        st.metric(label="Score 1", value=str(round(df2['Scores 1'].mean(), 2)))
    st.text('')
    st.bar_chart(df2, x='Nome', y=['Média Anual'], stack=False)
    st.bar_chart(df2, x='Nome', y=['Plataforma 1', 'Plataforma 2', 'Plataforma 3'],
                 stack=False)
### Nono Ano

if st.sidebar.button("Nono Ano"):
    with st.expander("Notas Primeiro trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df3,x = 'Nome', y=['Nota 1', 'Plataforma 1'],stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df3['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df3['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df3['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df3, x='Nome', y=['Scores 1'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df3_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Segundo trimestre", False):
        st.text('Comparativo de notas e plataformas')
        st.bar_chart(df3, x='Nome', y=['Nota 2', 'Plataforma 2'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df3['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df3['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df3['Nome'])))
        st.markdown("Gráfico de Scores por aluno")
        st.bar_chart(df3, x='Nome', y=['Scores 2'])
        st.text('Tabela dos 3 maiores Scores Z do Sexto Ano')
        st.table(df3_table.nlargest(3, 'Scores 1').round(2))
    with st.expander("Notas Terceiro trimestre", False):
        st.bar_chart(df3,x='Nome', y=['Nota 1', 'Plataforma 1'], stack=False)
        col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
        with col1:
            st.metric(label="Média turma", value=str(round(df3['Nota 1'].mean(), 3)))
        with col2:
            st.metric(label="Média Plataformas", value=str(round(df3['Plataforma 1'].mean(), 3)))
        with col3:
            st.metric(label="Numero de alunos ativos", value=str(len(df3['Nota 1'])))
    col1, col2, col3, col4 = st.columns(4, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df3['Nota 1'].mean(), 2)))
    with col2:
        st.metric(label="Nota Paraná", value=str(round(df3['Nota 1'].mean(), 2)))
    with col3:
        st.metric(label="Índice Plataforma", value=str(round(df3['Nota 1'].mean(), 2)))
    with col4:
        st.metric(label="Score", value=str(round(df3['Scores 1'].mean(), 2)))
    st.text('')
    st.bar_chart(df3, x='Nome', y=['Média Anual'], stack=False)
    st.bar_chart(df3, x='Nome', y=['Plataforma 1', 'Plataforma 2', 'Plataforma 3'],
                 stack=False)


if st.sidebar.button("Análise Estatistica por Série"):
    st.markdown("Análise Estatistica por Série")
    with st.expander("Estatistica Sexto Ano", expanded=False):
       st.table(df.describe().apply(lambda x: round(x,1)))

    with st.expander("Estatistica Setimo Ano", expanded=False):
       st.table(df1.describe().apply(lambda x: round(x,1)))

    with st.expander("Estatistica Oitavo Ano", expanded=False):
       st.table(df2.describe().apply(lambda x: round(x,1)))

    with st.expander("Estatistica Nono Ano", expanded=False):
       st.table(df2.describe().apply(lambda x: round(x,1)))

if st.sidebar.button("Estatística do Acerta Brasil"):
    st.markdown("## Acerta Brasil")