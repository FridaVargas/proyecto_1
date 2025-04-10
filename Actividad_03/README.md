# Actividad 03: Autómatas Celulares y Dinámicas Locales

Esta actividad forma parte del curso *Proyecto I*, impartido por el **Biol. Luis Guillermo García Jácome** en la Facultad de Ciencias de la UNAM. Consiste en una colección de simulaciones desarrolladas en **NetLogo** que modelan distintos tipos de autómatas celulares y comportamientos emergentes derivados de reglas locales simples.

---

## 📋 Índice de simulaciones

1. [Autómata celular elemental](#1-autómata-celular-elemental)
2. [Falling Sand](#2-falling-sand)
3. [Juego de la Vida](#3-juego-de-la-vida)
4. [Hormiga de Langton (otro autómata)](#4-hormiga-de-langton-otro-autómata)

---

## 1. Autómata Celular Elemental

<p align="center">
  <img src="ruta/al/gif_automata_elemental.gif" width="500"/>
</p>

Este modelo genera patrones lineales basados en reglas binarias (como la Regla 30 o 110). A partir de una fila inicial, cada celda evoluciona según el estado de sus vecinas inmediatas, formando estructuras que pueden ser caóticas o repetitivas.

🔸 Puedes elegir entre condición inicial aleatoria o semilla central.  
🔸 El número entre 0 y 255 determina la regla usada.

Archivo: `AutomataElemental.nlogo`

---

## 2. Falling Sand

<p align="center">
  <img src="https://github.com/user-attachments/assets/e41147ee-5916-44f3-b65c-2e61bf16dfae" alt=" Falling Sand">
</p>

Una simulación visual de caída de partículas de arena. Los granos intentan caer verticalmente, pero si hay obstáculos, se desvían diagonalmente o lateralmente, generando una acumulación natural.

🔸 Controlas la probabilidad de aparición de arena.  
🔸 Se representa el comportamiento granular emergente.

Archivo: `falling-sand.nlogo`

---

## 3. Juego de la Vida

![Vida](https://github.com/user-attachments/assets/50697d49-dd56-4653-acfc-5b8ea62b165d)

Implementación del clásico modelo de **John Conway**. Cada celda vive, muere o revive dependiendo del número de vecinos vivos. Además, las celdas muertas cambian gradualmente de color para mostrar cuánto tiempo llevan sin actividad.

🔸 Puedes dibujar con el mouse las condiciones iniciales.  
🔸 Muestra transiciones suaves de color para el estado muerto.

Archivo: `JuegoDeLaVida.nlogo`

---

## 4. Hormiga de Langton (otro autómata)

![Hormiga](https://github.com/user-attachments/assets/aad1b79b-b156-4831-b839-cfe45fccdbda)
Modelo que simula una simple "hormiga" que sigue dos reglas:  
- Si está en un cuadrado blanco, gira a la izquierda, cambia el color a negro y avanza.  
- Si está en un cuadrado negro, gira a la derecha, cambia a blanco y avanza.

🔸 Produce patrones caóticos que terminan en caminos repetitivos (carreteras).  
🔸 Usa sólo un agente tipo `turtle`.

Archivo: `otro_automata.nlogo`

---

## 🛠 Requisitos

- NetLogo 6.0 o superior  
👉 [Descargar aquí](https://ccl.northwestern.edu/netlogo/)

---

## 👩‍💻 Autora

Frida Michelle Vargas Bautista

---

## 📄 Licencia

Este trabajo se comparte bajo una licencia  
Creative Commons Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0).
