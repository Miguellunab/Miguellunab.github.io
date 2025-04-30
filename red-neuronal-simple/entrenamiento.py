import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Cargamos los datos de entrenamiento y prueba
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# 1 sola capa con 1 neurona
# capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo = tf.keras.Sequential([capa])

# 3 capas con 4, 4 y 1 neuronas respectivamente
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=4, input_shape=[1]),
    tf.keras.layers.Dense(units=4),
    tf.keras.layers.Dense(units=1)
])

# Compilamos el modelo
modelo.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Entrenamos el modelo
print("Entrenando el modelo...")
historial = modelo.fit(celsius, fahrenheit, epochs=100, verbose=False)
print("Modelo entrenado.")

# Guardar el modelo en formato Keras (.h5)
modelo.save("modelo.h5")
print("Modelo guardado en modelo.h5")

# Graficamos la pérdida del modelo
# plt.xlabel("# Epoca")
# plt.ylabel("Magnitud de pérdida")
# plt.plot(historial.history["loss"])
# plt.show()

# Hacemos una predicción
resultado = modelo.predict([100.0])
print(f"El resultado es {resultado} fahrenheit.")