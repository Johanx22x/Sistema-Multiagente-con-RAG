# 🧠 Pasos completos para correr el sistema multiagente con Ollama

## ✅ 1. Instalar Ollama

1. Ir a 👉 [https://ollama.com](https://ollama.com) y descargar el instalador para tu sistema operativo.
2. Instalarlo y luego en una terminal correr:

```bash
ollama run mistral
```

> Esto descarga y mantiene corriendo el modelo `mistral`. ¡Dejá esta terminal abierta todo el tiempo!

---

## ✅ 2. Instalar dependencias del proyecto

En una **nueva terminal**, dentro de la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

## ✅ 3. Crear la base vectorial (una sola vez)

Esto lee los PDFs y crea el índice que el sistema usa para responder.

```bash
python ingest_data.py
```

> Deberías ver algo como:

```
✅ ¡Base vectorial creada correctamente!
```

---

## ✅ 4. Ejecutar el sistema

Con Ollama aún corriendo en otra terminal, ejecutá:

```bash
python main.py
```

El sistema te va a preguntar:

```
¿Qué concepto deseas estudiar? >
```

Podés escribir algo como:

```
matriz inversa
```

Y vas a ver:
- 📚 Fragmento del PDF
- 🧠 Explicación del tutor
- ✏️ Ejercicio con solución paso a paso

---
