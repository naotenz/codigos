# Algoritmo de Suma Lineal

Este documento muestra el funcionamiento de un **algoritmo lineal simple** para calcular la suma de los elementos de un conjunto.

---

## 🔹 Descripción
El algoritmo recorre todos los elementos de un conjunto **una sola vez**, acumulando sus valores en una variable `suma`.

- Complejidad temporal: **O(n)**
- Complejidad espacial: **O(1)**

---

## 🔹 Pseudocódigo
Algoritmo SumaElementos
Entrada: Conjunto A de n elementos
suma ← 0
Para i ← 1 hasta n hacer
suma ← suma + A[i]
Fin Para
Salida: suma
Fin Algoritmo

---

## 🔹 Representación conceptual (diagrama)

```text
 ┌────────────────────┐
 │   Conjunto A =     │
 │   [3, 5, 7, 2]     │
 └─────────┬──────────┘
           │ (recorrer cada elemento)
           ▼
 ┌────────────────────┐
 │   Inicializar suma │
 │   suma = 0         │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │  Tomar elemento 3  │
 │  suma = 0 + 3 = 3  │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │  Tomar elemento 5  │
 │  suma = 3 + 5 = 8  │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │  Tomar elemento 7  │
 │  suma = 8 + 7 = 15 │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │  Tomar elemento 2  │
 │  suma = 15 + 2 =17 │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │  Resultado final:  │
 │       17           │
 └────────────────────┘

---

### 🔹 Resultado
Con eso se verá **alineado y limpio**, porque el bloque `text` usa **fuente monoespaciada** (cada caracter ocupa el mismo ancho).  

---

👉 Pregunta: ¿quieres que te prepare un `README.md` con el diagrama ya arreglado y listo para copiar/pegar, o prefieres que te muestre cómo hacerlo con **dibujos gráficos (SVG/mermaid)** para que se vea todavía más bonito en GitHub?
