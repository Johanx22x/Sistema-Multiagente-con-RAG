# Informe Técnico - Sistema Multiagente con RAG

**Curso:** Inteligencia Artificial  
**Profesor:** Kenneth Obando Rodríguez  
**Fecha de entrega:** 23 de junio de 2025  
**Estudiante(s):** 
- Johan Efrén Rodríguez Salas - 2022141892
- Carlos Eduardo Leiva Medaglia - 2021032973


**Caso de uso elegido:** Tutor Académico Personalizado

## Nombre del sistema

**TutorIA** - Sistema Multiagente para el Apoyo Académico Personalizado en Álgebra Lineal

## Descripción general

TutorIA es un sistema multiagente que guía al usuario en el estudio de conceptos específicos de álgebra lineal. Integra técnicas de inteligencia artificial generativa y recuperación aumentada (RAG) para ofrecer explicaciones detalladas, ejemplos prácticos y ejercicios guiados. Su arquitectura modular y colaborativa permite la interacción entre agentes especializados para asistir al usuario de forma personalizada y efectiva.

## Agentes involucrados

El sistema cuenta con tres agentes principales:

### 1. **Agente Lector**
- **Rol:** Extraer contenido relevante del material PDF (apuntes, libros).
- **Prompt:** “Lee el siguiente documento y selecciona fragmentos relacionados con el concepto: {concepto}.”
- **Interacción:** Envía los fragmentos al Agente Tutor.

### 2. **Agente Tutor**
- **Rol:** Explica el concepto utilizando los fragmentos proporcionados por el Lector.
- **Prompt:** “Usando este texto: {fragmento}, explica de forma clara y sencilla el concepto: {concepto}.”
- **Interacción:** Envía explicación al Agente Ejercitador.

### 3. **Agente Ejercitador**
- **Rol:** Genera un ejercicio práctico con solución paso a paso.
- **Prompt:** “Crea un ejercicio relacionado al concepto: {concepto} y explícalo paso a paso.”
- **Interacción:** Entrega el resultado final al usuario.

## Uso del RAG

El **Agente Lector** utiliza recuperación semántica para buscar y extraer información relevante desde una base vectorial previamente generada a partir de documentos en PDF. Se emplea FAISS para la indexación y búsqueda semántica con embeddings generados por LangChain.

## Tecnologías utilizadas

- **Lenguaje:** Python
- **Frameworks:** LangChain, LangGraph
- **Modelo base:** Mistral (ejecutado localmente con Ollama)
- **Base vectorial:** FAISS
- **Otros:** PyPDF, chromadb, etc.

## Diagrama de arquitectura

@startuml
actor Usuario

Usuario --> "Agente Lector" : Ingresa concepto

"Agente Lector" --> "Base Vectorial (FAISS)" : Realiza búsqueda semántica
"Base Vectorial (FAISS)" --> "Agente Lector" : Devuelve fragmentos relevantes

"Agente Lector" --> "Agente Tutor" : Envía fragmentos
"Agente Tutor" --> "Agente Ejercitador" : Envía explicación
"Agente Ejercitador" --> Usuario : Entrega ejercicio resuelto

note right of "Agente Lector"
Utiliza RAG y embeddings
generados por LangChain
end note

note bottom of "Base Vectorial (FAISS)"
Creados desde PDFs en carpeta `/data`
con `ingest_data.py`
end note
@enduml

## Implementación funcional

- Código escrito en Python, con estructura modular y clara.
- El archivo principal es `main.py`, el cual orquesta la interacción entre agentes.
- La base vectorial se genera mediante `ingest_data.py`.
- El archivo `README.md` contiene todas las instrucciones necesarias para ejecutar el sistema desde cero.
- El sistema fue probado con conceptos como “matriz inversa” y generó resultados exitosos en cada etapa.

## Video de presentación

Se realizó un video de demostración que incluye:
- Explicación del caso de uso.
- Diagrama y flujo del sistema.
- Ejecución real donde se consulta un concepto y el sistema responde con:
  - Fragmento del PDF.
  - Explicación del tutor.
  - Ejercicio con solución.

[Enlace al video]()

## Organización del código y documentación

- Repositorio: [https://github.com/Johanx22x/Sistema-Multiagente-con-RAG](https://github.com/Johanx22x/Sistema-Multiagente-con-RAG)
- Instrucciones completas incluidas en `README.md`.
- Código modular dividido por agentes.

## Conclusión

TutorIA demuestra una integración efectiva de múltiples agentes utilizando RAG y otras tecnologías de IA. El sistema refleja los conceptos aprendidos en clase, es funcional, modular y está preparado para ser extendido a otras áreas de conocimiento.