import streamlit as st
import numpy as np
import pandas as pd

st.title("2. Registro de ventas con NumPy")

st.markdown("Formulario para registrar productos, ventas o registros similares.")

# Inicializar arrays en session_state
if "data" not in st.session_state:
    st.session_state.data = {
        "producto": np.array([], dtype=str),
        "categoria": np.array([], dtype=str),
        "precio": np.array([], dtype=float),
        "cantidad": np.array([], dtype=int),
        "total": np.array([], dtype=float),
    }

# Formulario
producto = st.text_input("Nombre del producto")

categoria = st.selectbox(
    "Categoría",
    ["Alimentos", "Limpieza", "Ferretería", "Otros"]
)

precio = st.number_input("Precio", min_value=0.0)
cantidad = st.number_input("Cantidad", min_value=0, step=1)

# Botón
if st.button("Agregar"):
    if not producto:
        st.error("El producto es obligatorio ❌")
    elif precio <= 0 or cantidad <= 0:
        st.error("Precio y cantidad deben ser mayores a 0 ❌")
    else:
        total = precio * cantidad

        # Append a arrays (NumPy)
        st.session_state.data["producto"] = np.append(st.session_state.data["producto"], producto)
        st.session_state.data["categoria"] = np.append(st.session_state.data["categoria"], categoria)
        st.session_state.data["precio"] = np.append(st.session_state.data["precio"], precio)
        st.session_state.data["cantidad"] = np.append(st.session_state.data["cantidad"], cantidad)
        st.session_state.data["total"] = np.append(st.session_state.data["total"], total)

        st.success("Registro agregado correctamente ✅")

# Convertir a DataFrame
df = pd.DataFrame(st.session_state.data)

# Mostrar tabla
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no hay registros")

# KPI opcional
if not df.empty:
    st.metric("Total ventas", f"S/ {df['total'].sum():,.2f}")