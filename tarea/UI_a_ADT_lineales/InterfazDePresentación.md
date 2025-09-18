import streamlit as st

st.title("Algoritmos Lineales y Estructuras Matemáticas")

# Suma de lista
entrada = st.text_input("Ingresa una lista de números separados por coma:")
if entrada:
    suma, pasos = procesar_suma_lista(entrada)
    st.write("Paso a paso:")
    for i, numero, total in pasos:
        st.write(f"Iteración {i}: sumar {numero} → suma = {total}")
    st.success(f"Suma final: {suma}")

# Conjuntos
c1 = st.text_input("Ingresa elementos del Conjunto 1 separados por coma:")
c2 = st.text_input("Ingresa elementos del Conjunto 2 separados por coma:")
if c1 and c2:
    union = procesar_union_conjuntos([int(x) for x in c1.split(",")], [int(x) for x in c2.split(",")])
    st.success(f"Unión de conjuntos: {union}")
