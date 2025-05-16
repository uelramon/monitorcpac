import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# Caminho para a pasta de saída dos dados
PASTA_OUTPUT = "output"
PASTA_NUVENS = os.path.join(PASTA_OUTPUT, "nuvens")

st.set_page_config(page_title="Dashboard Instagram", layout="wide")
st.title("📊 Dashboard de Análise do Instagram")

# =========================================
# 1. ANÁLISE DAS BIOS
# =========================================
st.header("1. Análise das Bios")

# Top 10 contas mais seguidas
st.subheader("Top 10 contas mais seguidas")
top10_path = os.path.join(PASTA_OUTPUT, "top10_seguidores.csv")
top10_img = os.path.join(PASTA_OUTPUT, "top10_barplot.png")
if os.path.exists(top10_path):
    df_top10 = pd.read_csv(top10_path)
    st.dataframe(df_top10)
    if os.path.exists(top10_img):
        st.image(top10_img, caption="Top 10 contas mais seguidas")
else:
    st.warning("Arquivo top10_seguidores.csv não encontrado.")

# Distribuição por categoria
st.subheader("Distribuição por categorias")
categorias_path = os.path.join(PASTA_OUTPUT, "categorias.csv")
categorias_img = os.path.join(PASTA_OUTPUT, "categorias_barplot.png")
if os.path.exists(categorias_path):
    df_cat = pd.read_csv(categorias_path)
    st.dataframe(df_cat)
    if os.path.exists(categorias_img):
        st.image(categorias_img, caption="Distribuição por categorias")

# =========================================
# 2. ANÁLISE DE SENTIMENTOS
# =========================================
st.header("2. Análise de Sentimentos por País")
sent_path = os.path.join(PASTA_OUTPUT, "sentimentos.csv")
if os.path.exists(sent_path):
    df_sent = pd.read_csv(sent_path)
    st.dataframe(df_sent)
    st.bar_chart(df_sent.set_index("país")[["média_sentimento (1-5 estrelas)"]])
else:
    st.warning("Arquivo sentimentos.csv não encontrado.")

# =========================================
# 3. TOP POSTS E USUÁRIOS GERAL
# =========================================
st.header("3. Top Posts e Usuários - Geral")

# Top 10 posts geral
st.subheader("Top 10 posts com mais curtidas")
top_posts_path = os.path.join(PASTA_OUTPUT, "top10_posts.csv")
if os.path.exists(top_posts_path):
    st.dataframe(pd.read_csv(top_posts_path))

# Top 10 usuários geral
st.subheader("Top 10 usuários com maior soma de curtidas")
top_users_path = os.path.join(PASTA_OUTPUT, "top10_usuarios.csv")
if os.path.exists(top_users_path):
    st.dataframe(pd.read_csv(top_users_path))

# =========================================
# 4. NUVENS DE PALAVRAS POR PAÍS
# =========================================
st.header("4. Nuvens de Palavras por País")
if os.path.exists(PASTA_NUVENS):
    paises = sorted([f.replace("nuvem_", "").replace(".png", "") for f in os.listdir(PASTA_NUVENS) if f.endswith(".png")])
    pais_sel = st.selectbox("Selecione o país:", paises)
    caminho_img = os.path.join(PASTA_NUVENS, f"nuvem_{pais_sel}.png")
    if os.path.exists(caminho_img):
        st.image(caminho_img, caption=f"Nuvem de palavras - {pais_sel}")
    else:
        st.warning("Imagem da nuvem não encontrada.")
else:
    st.warning("Pasta de nuvens de palavras não encontrada.")
