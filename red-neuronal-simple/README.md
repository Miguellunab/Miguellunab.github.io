# Red Neuronal Simple

![Screenshot del Proyecto](../pixelart_miguel.png)

## Descripción

Una implementación interactiva de una red neuronal básica que convierte temperaturas de grados Celsius a Fahrenheit utilizando TensorFlow.js. Este proyecto está diseñado como una introducción práctica a los conceptos fundamentales del machine learning.

## Características

- **Conversión en tiempo real**: Selecciona una temperatura en Celsius mediante un deslizador y observa la predicción en Fahrenheit.
- **Interfaz intuitiva**: Diseño limpio y minimalista para facilitar la comprensión del proceso.
- **Modelo pre-entrenado**: El modelo ha sido entrenado previamente utilizando TensorFlow en Python y exportado para su uso en el navegador.

## Tecnología Utilizada

- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: TensorFlow.js
- **Entrenamiento**: Python con TensorFlow/Keras

## Cómo Funciona

En lugar de programar manualmente la conversión usando la fórmula `F = C × 1.8 + 32`, el modelo aprende la relación entre Celsius y Fahrenheit a partir de datos de ejemplo. El modelo neuronal consta de:

- Una capa de entrada (1 neurona)
- Una capa oculta densa (4 neuronas con activación ReLU)
- Una capa de salida (1 neurona)

## Archivos Clave

- `index.html` - Interfaz de usuario para la conversión
- `model.json` - El modelo exportado de TensorFlow
- `entrenamiento.py` - Script Python utilizado para entrenar y exportar el modelo

## Lecciones Aprendidas

Este proyecto demuestra cómo una red neuronal puede "aprender" incluso relaciones matemáticas simples a partir de datos, sin necesidad de programar explícitamente la fórmula. Es un excelente punto de partida para comprender conceptos básicos como:

- Arquitectura de red neuronal simple
- Conversión de modelos para uso en navegador
- Inferencia en tiempo real con JavaScript

---

Desarrollado por [Miguel Ángel López Jaramillo](https://github.com/Miguellunab) como parte de su portfolio de proyectos.
