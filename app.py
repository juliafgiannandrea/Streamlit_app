#Usando o Streamlit:

import streamlit as st 
import pandas as pd



st.title("Meu primeiro dashboard")
st.header("Esse é um header")

#Criando abas: 
abas = st.tabs(["Botão", "Radio", "Dataframe", "Gráfico"])

with abas[0]: 
    if st.button("Clique aqui"):
        st.text("Você apertou o botão")

with abas[1]: 
    opcao = st.radio(
        "Escolha a opção:",
        ("flamengo", "corinthians", "palmeiras")
        )

if opcao == "flamengo":
    st.info("Você é um urubu")
elif opcao == "corinthians":
    st.error("Você é campeão")
else:
   st.warning("Você é um perdedor") 

#wanrning e info muda a cor da resposta ao clicar no botão (info é azul e warning é vermelho)


#Pegando um dataframe: 
df = pd.read_csv("C:\\Users\\Dell\\Documents\\Ciência de Dados IBMEC\\Projeto em Ciência de Dados I\\exercicios_aula\\frontend\\data\\ibov.csv")
df = pd.DataFrame(df)   

#com o data frame fornecido: criar uma tabela no site usando o streamlit 
with abas[2]:
    st.dataframe(df)


#fazer gráfico do dataframe com os dados do dataframe: 
import matplotlib.pyplot as plt
import numpy as np 

with abas[3]: 
    fig, ax = plt.subplots()
    ax.bar(df["data"], df["abertura"], color='tab:red')

# Nome do eixo Y
    ax.set_ylabel('Valores de abertura')

#Nome do eixo X:
    ax.set_xlabel("Datas - de 2000-01-03 a 2024-04-01")

# Nome do gráfico
    ax.set_title('Variações no Ibovespa')

# Jogando o gráfico no Streamlit
    st.pyplot(fig)



