import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮")

st.title("🧮 Generador de Ecuaciones de Primer Grado")

# Función para generar ecuaciones tipo ax + b = c
def generar_ecuacion():
    a = random.randint(1, 10)
    x = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x

# Inicializar estado
if "ecuacion" not in st.session_state:
    st.session_state.ecuacion = generar_ecuacion()

a, b, c, solucion = st.session_state.ecuacion

# Mostrar ecuación
st.subheader(f"Ecuación:")
st.latex(f"{a}x + ({b}) = {c}")

# Entrada del usuario
respuesta = st.number_input("¿Cuál es el valor de x?", step=1)

# Botón verificar
if st.button("Verificar respuesta"):
    if respuesta == solucion:
        st.success("✅ ¡Correcto!")
        st.balloons()  # Animación de éxito
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era {solucion}")

# Botón nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.ecuacion = generar_ecuacion()
    st.rerun()
