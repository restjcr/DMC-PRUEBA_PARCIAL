import streamlit as st
import pandas as pd

st.title("1. Flujo de caja con listas")

# Lista Vacía
if "registros" not in st.session_state:
    st.session_state.registros = []

# Concepto
concepto = st.text_input("Ingresa el concepto")

# Tipo de Operación
tipo_operacion = st.radio(
    "Tipo de Operación",
    ["Ingreso 💰", "Gasto 💸"],
    horizontal=True
)

# Monto
monto = st.number_input("Monto", min_value=0.0)

# 👉 feedback
if st.button("Agregar"):
    if not concepto:
        st.error("El concepto es obligatorio ❌")
    elif monto <= 0:
        st.error("El monto debe ser mayor a 0 ❌")
    else:
        st.session_state.registros.append({
            "concepto": concepto,
            "tipo_operacion": tipo_operacion,
            "monto": monto
        })
        st.success("Registro agregado correctamente ✅")

# Asegurar columnas siempre
df = pd.DataFrame(
    st.session_state.registros,
    columns=["concepto", "tipo_operacion", "monto"]
)

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no hay registros")

# KPIs (sin error si está vacío)
ingresos = df.loc[df["tipo_operacion"] == "Ingreso 💰", "monto"].sum()
gastos = df.loc[df["tipo_operacion"] == "Gasto 💸", "monto"].sum()

if ingresos > gastos:
    saldo = "A favor 📈"
elif ingresos == gastos:
    saldo = "Neutro"
else:
    saldo = "En contra 📉"

col1, col2, col3 = st.columns(3)

col1.metric("Ingresos", f"S/. {ingresos}")
col2.metric("Gastos", f"S/. {gastos}")
col3.metric("Saldo", saldo)