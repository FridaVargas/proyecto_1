# Actividad 01: Modelos de Segregación en NetLogo

Esta actividad forma parte del curso *Proyecto 1*, impartido por el **Biol. Luis Guillermo García Jácome**, y tiene como objetivo explorar distintos modelos de segregación inspirados en el modelo de Schelling, utilizando el entorno de simulación NetLogo.

Se presentan tres variantes del modelo básico, enfocadas en diferentes mecanismos de preferencia y agrupamiento entre agentes.

---

## Modelos incluidos

### 1. `Modelo_Segregacion.nlogo`
Modelo básico de segregación de Schelling. Los agentes se mueven si no están satisfechos con la proporción de vecinos similares.

### 2. `segregacion_diferentes_preferencias.nlogo`
![SchellingPreferencias](https://github.com/user-attachments/assets/6c81dd42-feea-4fba-9f38-11b09100a971)
Extensión del modelo anterior donde los agentes pertenecen a distintos grupos y cada grupo tiene un nivel distinto de tolerancia (preferencia mínima).

### 3. `segregacion_multiples_grupos.nlogo`
![SchellingGrupos](https://github.com/user-attachments/assets/b7519857-ec65-41ed-b014-1f0a2cf6cde7)
Versión con múltiples grupos (hasta 9), cada uno con su propio color. Se exploran patrones de segregación más complejos.

---

## Variables clave

- `densidad`: Porcentaje de celdas ocupadas por agentes.

- `preferencia`: Proporción de vecinos similares requerida para que un agente esté satisfecho.
- `grupos`: Número de grupos distintos en el modelo.

---

## Cómo ejecutar el modelo

1. Abrir NetLogo.
2. Cargar cualquiera de los archivos `.nlogo` incluidos en esta carpeta.
3. Presionar el botón `setup` para inicializar el mundo.
4. Presionar `go` para iniciar la simulación.

---

## Observaciones

- Se pueden observar patrones de segregación emergente incluso cuando los agentes tienen preferencias moderadas.
- A mayor número de grupos, la segregación tiende a ser más dispersa y compleja.

---

## Requisitos

- NetLogo 6.0 o superior: https://ccl.northwestern.edu/netlogo/

---

## Autora

Frida Michelle Vargas Bautista

---

## Licencia

Este trabajo se comparte bajo una licencia Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
