import streamlit as st
import time

st.title("Algoritmo Lineal: Suma de Lista con Seguimiento")

# Entrada de datos
entrada = st.text_input("Ingresa los números separados por coma:", "1,2,3,4,5")
if entrada:
    numeros = [int(x) for x in entrada.split(",")]

    # Inicialización
    suma = 0
    paso = st.empty()
    paso.write(f"Inicializando suma = {suma}")

    # Proceso iterativo con seguimiento
    for i, numero in enumerate(numeros):
        suma += numero
        paso.write(f"Iteración {i+1}: sumar {numero} → suma = {suma}")
        time.sleep(0.5)  # Espera 0.5 segundos para ver cada paso

    # Resultado final
    st.success(f"La suma final de la lista es: {suma}")
