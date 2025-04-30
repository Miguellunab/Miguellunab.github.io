# Clasificador de Flores

![Screenshot del proyecto](../pixelart_miguel.png)

## Descripción

Un clasificador de especies de flores basado en visión por computadora, implementado completamente en el navegador utilizando TensorFlow.js y el modelo pre-entrenado MobileNetV2. Esta aplicación web permite a los usuarios cargar imágenes de flores y recibir predicciones sobre la especie a la que pertenecen.

## Características

- **Clasificación en tiempo real**: Sube o arrastra una imagen de una flor y recibe predicciones instantáneas.
- **Interfaz intuitiva**: Diseño moderno con soporte para arrastrar y soltar imágenes.
- **Visualización de resultados**: Muestra las 5 predicciones más probables con barras de porcentaje para una fácil interpretación.
- **Funcionamiento offline**: Una vez cargada la página, la aplicación funciona sin necesidad de conexión a internet.

## Tecnología Utilizada

- **Frontend**: HTML5, CSS3, JavaScript
- **Visión por Computadora**: TensorFlow.js, MobileNetV2
- **Interacción**: API de arrastrar y soltar de HTML5, Canvas

## Cómo Funciona

El clasificador utiliza un modelo MobileNetV2 pre-entrenado que ha sido optimizado para ejecutarse en navegadores web. Cuando el usuario carga una imagen:

1. La imagen se preprocesa y redimensiona a 224x224 píxeles
2. Se normaliza a valores entre -1 y 1
3. Se pasa al modelo para hacer la predicción
4. Los resultados se muestran ordenados por nivel de confianza

## Especies Detectables

El modelo puede identificar numerosas especies de flores, incluyendo:

- Rosas
- Girasoles
- Tulipanes
- Margaritas
- Orquídeas
- Y muchas más

## Archivos Clave

- `index.html` - Interfaz de usuario para la clasificación
- `mobilenetv2_tfjs/` - Directorio que contiene el modelo optimizado para navegador

## Lecciones Aprendidas

Este proyecto demuestra la potencia de ejecutar modelos complejos de visión por computadora directamente en el navegador del usuario, eliminando la necesidad de servidores para el procesamiento. Conceptos clave explorados:

- Optimización de modelos para entornos web
- Técnicas de preprocesamiento de imágenes
- Manejo de interfaces de usuario para aplicaciones de IA
- Visualización de datos de clasificación

---

Desarrollado por [Miguel Ángel López Jaramillo](https://github.com/Miguellunab) como parte de su portfolio de proyectos.
