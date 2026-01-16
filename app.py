import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚲 Dashboard: Análisis de Bicicletas (Austin)")
st.write("Este dashboard muestra los resultados procesados en la nube.")

# Creamos un selector en la barra lateral
opcion = st.sidebar.selectbox(
    '¿Qué quieres visualizar?',
    ('Resumen de Viajes', 'Comparativa Fin de Semana')
)

if opcion == 'Resumen de Viajes':
    st.subheader("Estaciones con más tráfico")
    # Datos de ejemplo basados en tu análisis anterior
    data = pd.DataFrame({
        'Estación': ['21st & Speedway', 'Riverside', 'City Hall', 'Capitol'],
        'Viajes': [1200, 950, 800, 600]
    })
    st.bar_chart(data.set_index('Estación'))

else:
    st.subheader("Análisis: ¿Ocio o Transporte?")
    st.write("Promedio de minutos por viaje:")
    # Simulación de tu resultado de Python
    col1, col2 = st.columns(2)
    col1.metric("Día Laboral", "12.5 min")
    col2.metric("Fin de Semana", "24.8 min", "12.3 min más")
    
    st.info("💡 Conclusión: Los usuarios usan las bicicletas el doble de tiempo durante el fin de semana.")
