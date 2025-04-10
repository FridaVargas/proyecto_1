# Actividad 02: Sincronización de luciérnagas

Esta actividad forma parte del curso *Proyecto 1*, impartido por el **Biol. Luis Guillermo García Jácome**, y tiene como objetivo modelar la sincronización colectiva en poblaciones de luciérnagas mediante reglas simples de interacción local. El modelo fue implementado en el entorno de simulación **NetLogo**.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/41c28afb-7397-46b6-8ece-dd81cecc09ce" alt="Luciérnagas" width="500"/>
</p>

## Descripción del modelo

Cada luciérnaga es representada como un agente con un reloj interno que avanza en cada tic del sistema. Cuando el reloj alcanza un umbral, la luciérnaga emite un destello (se vuelve amarilla) y reinicia su reloj. Las luciérnagas cercanas a un destello pueden ajustar su fase para acercarse a la sincronía.

Además, el modelo selecciona **una luciérnaga al azar** (`luciernaga_muestra`) para poder darle seguimiento individual si se desea graficar o destacar su comportamiento.

---


## Variables clave

- `reloj`: ciclo interno de cada luciérnaga.
- `umbral`: valor que determina cuándo una luciérnaga destella.
- `radio_vision`: distancia en la que una luciérnaga detecta el destello de otras.
- `min_luces_resetear`: número mínimo de destellos vecinos necesarios para que una luciérnaga reinicie su reloj.
- `luciernaga_muestra`: agente seleccionado al azar como muestra de referencia.

---

## Cómo ejecutar el modelo

1. Abrir NetLogo (versión 6.0 o superior).
2. Cargar el archivo `sincronizacion_luciernagas.nlogo`.
3. Presionar `setup` para inicializar.
4. Presionar `go` para iniciar la simulación.

---


## Requisitos

- NetLogo 6.0 o superior  
  👉 https://ccl.northwestern.edu/netlogo/

---

## Autora

Frida Michelle Vargas Bautista

---

## Licencia

Este trabajo se comparte bajo una licencia  
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
