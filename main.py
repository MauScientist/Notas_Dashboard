import streamlit as st
import pandas as pd
import numpy as np

#### Lendo banco de dados CSV

#df = pd.read_csv('citations.csv')
df = pd.DataFrame(
    np.random.rand(30,9),
    columns=['Nota 1','Plataforma 1', 'Nota 2', 'Plataforma 2', 'Nota 3', 'Plataforma 3', 'Recuperação 1', 'Recuperação 2', 'Recuperação 3']
)

st.sidebar.image('teste.png')
st.markdown("# Aplicativo de visualização de Notas")
st.markdown("-Aplicativo baseado em steamlit para analise rápida das notas de alunos")
st.sidebar.header('Avaliações')
if st.sidebar.button("Nota 1"):
    st.header("Nota 1")
    st.bar_chart(df,y = ['Nota 1','Plataforma 1'])
    col1,col2,col3 = st.columns(3, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Nota 1'].mean(), 3)))
    with col2:
        st.metric(label="Média Plataformas", value=str(round(df['Plataforma 1'].mean(), 3)))
    with col3:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 1'].mean(), 3)))
if st.sidebar.button("Nota 2"):
    st.header("Nota 2")
    st.bar_chart(df,y = ['Nota 2','Plataforma 2'])
    col1,col2,col3 = st.columns(3, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Nota 2'].mean(), 2)))
    with col2:
        st.metric(label="Média Plataformas", value=str(round(df['Plataforma 2'].mean(), 2)))
    with col3:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 2'].mean(), 2)))
if st.sidebar.button('Nota 3'):
    st.header("Nota 3")
    st.bar_chart(df,y = ['Nota 3','Plataforma 3'])
    col1,col2,col3 = st.columns(3, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Nota 3'].mean(), 2)))
    with col2:
        st.metric(label="Média Plataformas", value=str(round(df['Plataforma 3'].mean(), 2)))
    with col3:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 3'].mean(), 2)))
st.sidebar.subheader('Recuperações')
if st.sidebar.button('Recuperação 1'):
    st.header("Recuperação 1")
    st.bar_chart(df,y = ['Recuperação 1'])
    col1,col2 = st.columns(2, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Recuperação 1'].mean(), 2)))
    with col2:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 3'].mean(), 2)))
if st.sidebar.button('Recuperação 2'):
    st.header("Recuperação 2")
    st.bar_chart(df,y = ['Recuperação 2'])
    col1,col2 = st.columns(2, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Recuperação 2'].mean(), 2)))
    with col2:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 3'].mean(), 2)))
if st.sidebar.button('Recuperação 3'):
    st.header("Recuperação 3")
    st.bar_chart(df,y = ['Recuperação 3'])
    col1,col2 = st.columns(2, vertical_alignment="bottom", border=True)
    with col1:
        st.metric(label="Média turma", value=str(round(df['Recuperação 3'].mean(), 2)))
    with col2:
        st.metric(label="Numero de alunos ativos", value=str(round(df['Nota 3'].mean(), 2)))
st.sidebar.subheader('Média Final')
if st.sidebar.button('Médias Finais'):
    st.header('Média Final')
    #st.line_chart(df['Recuperação 3'])
st.sidebar.text("Desenvolvido por: Mauricio A. Ribeiro e Rafaela Martins")



