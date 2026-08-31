import streamlit as st
import pandas as pd
import database as db

st.set_page_config(
    page_title="Locadora de Veículos",
    page_icon="image.png",
    layout="centered"
)

# Criar tabela
db.criar_tabela()

# MENU
# =========================
menu = st.sidebar.radio(
    "Menu",
    ["Cadastrar veículo", "Consultar veículos"]
)


# =========================
# CADASTRAR VEÍCULO
# =========================
if menu == "Cadastrar veículo":

    st.image("image.png")
    st.header("Cadastrar veículo")

    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    ano = st.number_input(
        label="Ano",
        min_value=1950,
        max_value=2026
    )
    placa = st.text_input("Placa")
    diaria = st.number_input("Valor diária")
    disponibilidade = st.selectbox("disponibilidade"
                                  ["top", "center", "bottom"], index=2)
    
   

    if st.button("Enviar dados"):

        if marca and modelo and placa:

            db.cadastrar_veiculo(
                marca,
                modelo,
                int(ano),
                placa,
                diaria,
                disponibilidade 
            )

            st.success("Veículo cadastrado com sucesso!")

        else:
            st.warning("Preencha todos os campos!")


# =========================
# CONSULTAR VEÍCULOS
# =========================
elif menu == "Consultar veículos":

    st.header("Veículos cadastrados")

    veiculos = db.consultar_veiculos()

    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        filtro_placa = st.text_input("Filtrar por placa")

    with col2:
        filtro_modelo = st.text_input("Filtrar por modelo")

    with col3:
        filtro_marca = st.text_input("Filtrar por marca")
    with col4:
          filtro_diaria= st.text_input("Filtrar por valor")
    with col5:
          filtro_disponibilidade = st.text_input("Filtrar por disponibilidade")


    if veiculos:

        # Aqui criamos a variável
        veiculos_filtrados = []

        # Aqui fazemos os filtros
        for veiculo in veiculos:

            placa = str(veiculo[4])
            modelo = str(veiculo[2])
            marca = str(veiculo[1])
            diaria = str(veiculo[5])
            disponibilidade = str(veiculo[6])

            if (
                filtro_placa.lower() in placa.lower()
                and filtro_modelo.lower() in modelo.lower()
                and filtro_marca.lower() in marca.lower()
                and filtro_diaria.lower() in diaria.lower()
                and filtro_disponibilidade.lower() in disponibilidade.lower()
            ):
                veiculos_filtrados.append(veiculo)

        # Criar tabela
        tabela = []

        for veiculo in veiculos_filtrados:
            tabela.append({
                "ID": veiculo[0],
                "Marca": veiculo[1],
                "Modelo": veiculo[2],
                "Ano": veiculo[3],
                "placa": veiculo[4],
                "diaria": f"{veiculo[5]:.2f}",
                "disponibilidade": veiculo[6]
            })

        st.table(tabela)

        st.write(
            f"{len(veiculos_filtrados)} veículo(s) encontrado(s)."
        )

    else:
        st.info("Nenhum veículo cadastrado.")


    



 

  




