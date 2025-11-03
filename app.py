import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Top Filmes IMDb",
    page_icon="🎬",
    layout="wide"
)

# Carregar dados dos filmes


# Sidebar apenas com filtro de gênero
# coloque a logo e a selectbox


# Aplicar filtro


# Título da página

# Mostrar quantidade de filmes


# Mostrar filmes em grid (3 colunas)
colunas = st.columns(3)

for index, filme in filmes_filtrados.iterrows():
    # Calcular em qual coluna colocar (0, 1 ou 2)
    coluna_index = index % 3
    
    with colunas[coluna_index]:
        # Container de cada filme com altura fixa
        with st.container():
            # Imagem com altura fixa
            st.image(filme['Image URL'], use_container_width=True)
            
            # Informações do filme

            
            # Botão para ver no IMDb
            if st.button(f"Ver no IMDb", key=f"btn_{filme['Rank']}"):
                st.markdown(f"[🔗 Abrir página do IMDb]({filme['IMDb URL']})")
            
       