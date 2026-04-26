import streamlit as st

st.set_page_config(page_title="DMC", layout="wide")

# Definir páginas
home        =   st.Page("pages/0_home.py", title="Home", icon="🏠")
ejercicio1  =   st.Page("pages/1_ejercicio1.py", title="Ejercicio 1", icon="📊")
ejercicio2  =   st.Page("pages/2_ejercicio2.py", title="Ejercicio 2", icon="📊")
ejercicio3  =   st.Page("pages/3_ejercicio3.py", title="Ejercicio 3", icon="📊")
ejercicio4  =   st.Page("pages/4_ejercicio4.py", title="Ejercicio 4", icon="📊")

# Crear navegación
pg = st.navigation([home, ejercicio1, ejercicio2, ejercicio3, ejercicio4])

# Ejecutar página seleccionada
pg.run()