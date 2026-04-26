import streamlit as st
import pandas as pd
import libreria_funciones_proyecto1 as superfunc


st.title("3. Uso de funciones desde una librería externa")

st.markdown("Ingresa los valores para calcular el retorno sobre la inversión.")

# Histórico
if "historial" not in st.session_state:
    st.session_state.historial = []

ganancia = st.number_input("Ganancia neta", min_value=0.0)
inversion = st.number_input("Inversión", min_value=0.0)

# Botón
if st.button("Calcular ROI"):
    try:
        resultado = superfunc.calcular_roi(ganancia, inversion)

        st.success(f"ROI: {resultado['roi_pct']}% 📈")

        # Guardar histórico
        st.session_state.historial.append({
            "ganancia_neta": ganancia,
            "inversion": inversion,
            "roi_pct": resultado["roi_pct"]
        })

    except ValueError as e:
        st.error(str(e))


# DataFrame histórico
df = pd.DataFrame(st.session_state.historial)

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no hay cálculos realizados")
