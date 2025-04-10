# Actividad 04: Reflexión y Práctica sobre Modelos Basados en Agentes

Esta actividad forma parte del curso *Proyecto 1*, impartido por el **Biol. Luis Guillermo García Jácome**. 

---

La práctica consistió en explorar y modificar un modelo basado en reglas de dominancia cíclica (tipo piedra-papel-tijera), con distintos grados de complejidad y tipos de interacción.

### 🌐 Enlace a la práctica:
https://curso-modelos-basados-en-agentes.github.io/curso_MBA/practica_04/

###  Modelos desarrollados:

<p align="center">
  <img src="https://github.com/user-attachments/assets/f69f74b0-f391-453f-8731-3df5c1abb2e7" />
</p>

- **`automata_RSP.nlogo`**: Versión base del modelo para referencia, con reglas de dominancia entre colores pero sin dinámica estocástica de eventos.
  
<p align="left">
  <img src="https://github.com/user-attachments/assets/48946014-d515-4769-b9d7-320852857e4d" />
</p>

- **`modelo_RSP_01.nlogo`**: Simulación basada en una dinámica de interacción tipo piedra-papel-tijera entre parches de tres colores (rojo, azul, amarillo). Los agentes compiten entre sí local o globalmente, según la configuración, e invaden al otro si “le ganan”.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c863a4ae-0e34-40e2-9be7-4b98c942c8a1" />
</p>

- **`modelo_RSP_02.nlogo`**: Variante avanzada que introduce tres tipos de eventos: selección (competencia entre agentes), reproducción (ocupación de espacios vacíos) e intercambio (cambio de lugar entre agentes). Cada evento tiene una tasa controlable por el usuario. Además, los agentes eliminados se vuelven inactivos (celdas negras).




## 📚 Créditos

**Curso:** Modelos Basados en Agentes  
**Profesor:** Biol. Luis Guillermo García Jácome  
**Institución:** Facultad de Ciencias, UNAM  
**Año:** 2025
