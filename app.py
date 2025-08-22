# importar las librerías necesarias
import pandas as pd
import plotly_express as px
import streamlit as st

# cargar el dataset
car_data = pd.read_csv('vehicles_us.csv')

# contenido de la aplicación Streamlit
st.header('Análisis Exploratorio de vehículos')  # agregar encabezado
hist_button = st.button('Construir Histograma') # botón para construir el histograma
scatter_checkbox = st.checkbox('Construir Gráfico de Dispersión') # checkbox para construir el gráfico de dispersión

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Construyendo un histograma de los odómetros de los vehículos...')
    
    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:  # al marcar la casilla
    # escribir un mensaje
    st.write('Construyendo un gráfico de dispersión de los odómetros de los vehículos...')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x='odometer')
    
    # mostrar gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)