import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df = load_data()

# Encabezado
st.title("Análisis de Anuncios de Coches en EE.UU.")
st.markdown("Explora los datos mediante gráficos interactivos y controles.")

# Casilla de verificación
if st.checkbox("Mostrar datos crudos"):
    st.write(df.head())

# Histograma del odómetro
st.subheader("Distribución del Kilometraje (odómetro)")
fig_hist = px.histogram(df, x="odometer", nbins=30, title="Histograma del Odómetro")
st.plotly_chart(fig_hist)

# Gráfico de dispersión: Precio vs Odómetro
st.subheader("Precio vs Kilometraje")
fig_scatter = px.scatter(df, x="odometer", y="price", color="type", title="Gráfico de Dispersión Precio vs Odómetro")
st.plotly_chart(fig_scatter)

# Botón de recarga
if st.button("Recargar datos"):
    df = load_data()
    st.success("Datos recargados exitosamente.")

    import streamlit as st



if __name__ == "__main__":
    st.set_page_config(page_title="Anuncios de Coches", layout="wide")