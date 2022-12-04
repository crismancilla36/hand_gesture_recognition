# Reconocimiento de gestos de mano

> **Nota:** Por ahora está en español, pero por cuestiones de presentación será actualizado a inglés en un futuro.

## Preparación de entorno

### Requisitos

Para la ejecución de este proyecto será necesario contar con [Python3](https://www.python.org/).
Así mismo será necesario contar con un [entorno virtual](https://docs.python.org/3/library/venv.html).


> **Nota:** Por el momento, antes de crear el dataset es necesario crear la carpeta `resources`.


### Clonar el repositorio

Una vez que se ha clonado el repositorio será necesario instalar todos los paquetes que se encuentran en `requirements.txt`.

```
pip install -r requirements.txt
```

## Ejecución

La idea que es que este programa no sea ejecutado como un todo, pero que mediante comandos podamos manipular los
parámetros a nuestra conveniencia.


###Sintaxis

```
python main.py <function> <argument>
```

###Ejemplo

El comando de ejemplo captura un conjunto de puntos tomados por la webcam y los etiqueta como `palm`. Finalmente 
los agrega al archivo `resources/data.csv`

```
python main.py save_gesture palm
```

## Funciones disponibles

### save_gesture < name >
Agrega un conjuto de puntos en el dataset con la etiqueta `name`.

````commandline
python main.py save_gesture peace
````


## Implementaciones

Si usted necesita hacer uso de del modelo para otras implementaciones solo necesita editar el archivo `main.py`.
Ahí podrá llamar al iterador ``get_gesture`` el cual genera una tuplas ``(gesture_index, gesture_label)``.
