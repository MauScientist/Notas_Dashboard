import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    layout="wide",
)


#### Lendo banco de dados CSV
## sexto ano


def DataFrame_notas(df):
    df['Media Plataforma'] = df[['Plataforma 1','Plataforma 2', 'Plataforma 3']].mean(axis=1)
    df['NotaERec1'] = df[['Nota 1','Recuperação 1']].max(axis=1)
    df['NotaERec2'] = df[['Nota 2','Recuperação 2']].max(axis=1)
    df['NotaERec3'] = df[['Nota 3','Recuperação 3']].max(axis=1)
    df['Nota Final'] = round(df[['NotaERec1','NotaERec2', 'NotaERec3']].mean(axis=1),2)
    df['Scores'] = (df['Nota Final'] - 6.0) / df['Nota Final'].std()
    df['Score Medio'] = df['Scores'].mean()
    df['Situação'] = df['Nota Final'] >= 6.0
    df['Situação'] = df['Situação'].map({True: 'Aprovado', False: 'Reprovado'})
    df_scores = df[['Nome','Scores']]
    return df, df_scores


#df = pd.DataFrame(
#    np.random.rand(30,9),
#    columns=['Nota 1','Plataforma 1', 'Nota 2', 'Plataforma 2', 'Nota 3', 'Plataforma 3', 'Recuperação 1', 'Recuperação 2', 'Recuperação 3']
#)


st.sidebar.title("Sistema de Análise de notas")
st.sidebar.header("Ano Letivo de 2024")
st.sidebar.text(" Disciplina de Matemática")
###### SEXTO ANO
def Analise_alunos(TURMA_LETIVA, PLATAFORMA,df,df_scores):
    if st.sidebar.button(TURMA_LETIVA):
        st.header("Parâmetros do "+TURMA_LETIVA)
        with st.expander("Notas Primeiro trimestre", False):
            st.markdown('### Notas e suas recuperações')
            st.bar_chart(df,x = 'Nome', y=['Nota 1','Recuperação 1', 'Nota 2', 'Recuperação 2', 'Nota 3', 'Recuperação 3'],stack=False)
            st.markdown('## Nota Final ')
            st.bar_chart(df,x = 'Nome', y=['Nota Final'],stack=False)
            col1, col2, col3 = st.columns(3, vertical_alignment="bottom", border=True)
            with col1:
                st.metric(label="Média turma", value=str(round(df['Nota Final'].mean(), 3)))
            with col2:
                st.metric(label="Média Plataformas", value=str(round(df['Media Plataforma'].mean(), 3)))
            with col3:
                st.metric(label="Numero de alunos ativos", value=str(len(df['Nome'])))
            st.markdown("### Gráfico de Scores por aluno")
            st.bar_chart(df, x='Nome', y=['Scores'], stack = False)
            st.text('**Notas 1 = 3.0, Nota 2 = 2.0 e Nota 3 = 5.0 (Provão)')
            st.markdown('## Tabela dos 3 maiores Scores Z do Sexto Ano')
            st.table(df_scores.nlargest(3, 'Scores').round(2))
        with st.expander("Situação do aluno", False):
            st.markdown("## Situação do Aluno")
            st.table(df[['Nome','Nota 1','Recuperação 1','Nota 2','Recuperação 2','Nota 3','Recuperação 3', 'Nota Final', 'Situação']])
        with st.expander("Métricas Importantes", False):
            st.markdown("## Métricas Importantes")
            col1, col2, col3  = st.columns(3, vertical_alignment="bottom", border=True)
            with col1:
                st.metric(label="Média turma", value=str(round(df['Nota Final'].mean(),2)))
            with col2:
                st.metric(label="Porcentagem Nota Paraná", value=str(round(df['Nota 1'].mean(), 2)))
            with col3:
                st.metric(label="Índice Médio "+PLATAFORMA, value=str(round(df['Media Plataforma'], 2)))
        with st.expander("Análise Estatistica por Série"):
             st.markdown("## Análise Estatistica por Série")
             st.table(df.describe().apply(lambda x: round(x,1)))
        with st.expander("Acerta Brasil"):
            st.markdown("Em breve Notas do Acerta Brasil")

df6 = pd.read_csv('NotasSextoAno_2T.csv', sep=",")
df6A,df6AScores = DataFrame_notas(df6)
Analise_alunos("6A","Matific",df6A,df6AScores)

df7 = pd.read_csv('NotasSetimoAno_2T.csv', sep=",")
df7A,df7AScores = DataFrame_notas(df7)
Analise_alunos("7A","Matific",df7A,df7AScores)

df8 = pd.read_csv('NotasOitavoAno_2T.csv', sep=",")
df8A,df7AScores = DataFrame_notas(df8)
Analise_alunos("8A","Khan Academy", df8A,df7AScores)

df9 = pd.read_csv('NotasOitavoAno_2T.csv', sep=",")
df9A,df9AScores = DataFrame_notas(df9)
Analise_alunos("9A","Khan Academy",df9A,df9AScores)

st.sidebar.info(': mau.ap.ribeiro@gmail.com', icon=":material/mail:")