import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Obter o diretório do arquivo atual e configurar o caminho
caminho = Path(__file__).resolve().parent / "data" / "ibov.csv"

# Título e cabeçalho do app
st.title("Meu primeiro dashboard")
st.header("Esse é um header")

# Exemplo de Markdown
st.markdown(
    '''
    # 1
    ## 2
    ### 3
    '''
)

# Criação de abas
abas = st.tabs(["Botão", "Radio", "DataFrame", "Gráfico"])

# Aba do botão
with abas[0]:
    if st.button("Clique aqui"):
        st.text("Você apertou o botão")

# Aba do radio (com a escolha do time)
with abas[1]:
    opcao = st.radio("Escolha seu time:", ["flamengo", "corinthians", "palmeiras"])
    
    if opcao == "flamengo":
        st.info("Você é um urubu")
    elif opcao == "corinthians":
        st.error("Você é campeão")
    else:
        st.warning("Você é um perdedor")

# Aba do DataFrame
with abas[2]:
    st.subheader("Exibição do DataFrame")
    
    # Verificar se o arquivo existe e, em caso afirmativo, exibir o DataFrame
    if caminho.exists():
        df = pd.read_csv(caminho)
        st.dataframe(df)
    else:
        st.error("Arquivo não encontrado: " + str(caminho))

# Aba do gráfico
with abas[3]:
    # Gráfico com dados do DataFrame
    if 'df' in locals():  # Verifica se o DataFrame foi carregado
        fig, ax = plt.subplots()
        
        # Gráfico de barras com dados do DataFrame
        ax.bar(df["data"], df["abertura"], color='tab:red')

        # Nome do eixo Y
        ax.set_ylabel('Valores de Abertura')

        # Nome do eixo X
        ax.set_xlabel("Datas - de 2000-01-03 a 2024-04-01")

        # Nome do gráfico
        ax.set_title('Variações no Ibovespa')

        # Exibir o gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.error("Não foi possível criar o gráfico, pois o DataFrame não está disponível.")