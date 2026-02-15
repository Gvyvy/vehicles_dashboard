import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.title("Dashboard de Vehículos")

# Leer dataset
df = pd.read_csv('vehicles_us.csv')

st.write("Explora el dataset de anuncios de vehículos en EE.UU.")

# 🔹 Crear columnas para los botones
col1, col2 = st.columns(2)

# 🔘 Botón para construir histograma
with col1:
    hist_button = st.button("Mostrar histograma de precios")

# 🔘 Botón para construir gráfico de dispersión
with col2:
    scatter_button = st.button("Mostrar gráfico de dispersión")


#hist_button = st.button("Construir histograma de precios")

if hist_button:
    st.write("Distribución de precios de los vehículos")

    fig = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Distribución de Precios"
    )

    st.plotly_chart(fig, width="stretch")


#scatter_button = st.button("Construir gráfico Precio vs Año")

if scatter_button:
    st.write("Relación entre el año del modelo y el precio")

    fig_scatter = px.scatter(
        df,
        x="model_year",
        y="price",
        opacity=0.6,
        title="Precio vs Año del Vehículo"
    )

    st.plotly_chart(fig_scatter, width="stretch")