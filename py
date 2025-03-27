import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados (use os seus dados reais ou um arquivo .csv)
# df = pd.read_csv('seu_arquivo.csv')

# Exemplo simples
eNPS = 84  # Exemplo de eNPS calculado
total_respostas = 32
promotores = 27
neutros = 5
detratores = 0

# Gráficos
def grafico_pizza():
    labels = ['Promotores', 'Neutros', 'Detratores']
    sizes = [promotores, neutros, detratores]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#14532d", "#4d7c0f", "#a3e635"])
    plt.axis('equal')
    st.pyplot()

def grafico_histograma():
    # Dados fictícios de idade para o histograma
    idades = [25, 34, 45, 29, 54, 60, 32, 43, 51, 40]
    plt.hist(idades, bins=10, color="#14532d", edgecolor="black")
    plt.title('Distribuição de Idade')
    st.pyplot()

# Dashboard Layout
st.title("Dashboard de Satisfação - UPAC")
st.write(f"**eNPS**: {eNPS}")
st.write(f"**Total de Respostas**: {total_respostas}")
st.write(f"**Promotores**: {promotores}, **Neutros**: {neutros}, **Detratores**: {detratores}")

# Adicionar gráficos
st.subheader("Distribuição de Satisfação (eNPS)")
grafico_pizza()

st.subheader("Distribuição de Idade dos Pacientes")
grafico_histograma()