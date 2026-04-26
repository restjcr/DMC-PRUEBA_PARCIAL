import streamlit as st
import pandas as pd
import libreria_clases_proyecto1 as superclass

st.title("4. Gestión de Empleados (CRUD)")

st.markdown("Operaciones de Insercion, actualizacion, lectura y eliminación de empleados de una empresa ficticia.")

# --- Estado ---
if "empleados" not in st.session_state:
    st.session_state.empleados = []

tab1, tab2, tab3 = st.tabs(["Crear", "Actualizar", "Eliminar"])

# =========================
# 🟢 CREAR
# =========================
with tab1:
    st.subheader("Nuevo empleado")

    nombre = st.text_input("Nombre")
    salario_base = st.number_input("Salario base", min_value=0.0)
    bono = st.number_input("% Bono", min_value=0.0)
    descuento = st.number_input("% Descuento", min_value=0.0)

    if st.button("Agregar empleado"):
        try:
            emp = superclass.Empleado(nombre, salario_base, bono, descuento)
            st.session_state.empleados.append(emp.resumen())
            st.success("Empleado agregado ✅")
        except Exception as e:
            st.error(str(e))

# =========================
# 🔵 VISUALIZAR
# =========================
st.subheader("Listado de empleados")

df = pd.DataFrame(st.session_state.empleados)

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No hay empleados registrados")

# =========================
# 🟡 ACTUALIZAR
# =========================
with tab2:
    st.subheader("Actualizar empleado")

    if st.session_state.empleados:
        nombres = [e["nombre"] for e in st.session_state.empleados]
        seleccionado = st.selectbox("Selecciona empleado", nombres)

        idx = nombres.index(seleccionado)
        emp_actual = st.session_state.empleados[idx]

        nuevo_salario = st.number_input("Nuevo salario base", value=emp_actual["salario_base"])
        nuevo_bono = st.number_input("% Bono", value=0.0)
        nuevo_desc = st.number_input("% Descuento", value=0.0)

        if st.button("Actualizar"):
            try:
                emp = superclass.Empleado(seleccionado, nuevo_salario, nuevo_bono, nuevo_desc)
                st.session_state.empleados[idx] = emp.resumen()
                st.success("Empleado actualizado ✅")
            except Exception as e:
                st.error(str(e))
    else:
        st.info("No hay empleados para actualizar")

# =========================
# 🔴 ELIMINAR
# =========================
with tab3:
    st.subheader("Eliminar empleado")

    if st.session_state.empleados:
        nombres = [e["nombre"] for e in st.session_state.empleados]
        seleccionado = st.selectbox("Selecciona empleado a eliminar", nombres)

        if st.button("Eliminar"):
            idx = nombres.index(seleccionado)
            st.session_state.empleados.pop(idx)
            st.success("Empleado eliminado 🗑️")
    else:
        st.info("No hay empleados para eliminar")