import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# encabezado
st.header('Información de autos en venta')
# casillas de verificación
show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# histograma
if show_hist:
    st.subheader("Histograma")
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# gráfico de dispersión
if show_scatter:
    st.subheader("Gráfico de dispersión")
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")

    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
