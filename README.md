# Reconocimiento de gestos de mano

> **Nota:** Por ahora está en español, pero por cuestiones de presentación será actualizado a inglés en un futuro.

## Ejecución

La idea que es que este programa no sea ejecutado como un todo, pero que mediante comandos podamos manipular los
parámetros a nuestra conveniencia.



###Sintaxis

```python main.py <function> <argument>```

###Ejemplo

El comando de ejemplo captura un conjunto de puntos tomados por la webcam y los etiqueta como `palm`. Finalmente 
los agrega al archivo `resources/data.csv`

```python main.py save_gesture palm```

## Funciones disponibles

### save_gesture < name >
Agrega un conjuto de puntos en el dataset con la etiqueta `name`.
