# Trabajo Practico 1 - Data Science

Hola, este es nuestro trabajo practico numero 1 de data science, que hicimos en grupo. La tarea era hacer varias funciones para calcular estadisticas basicas con listas de datos numericos, y despues trabajar con datos de estudiantes y sus notas.

## ITEM_1.py
En este archivo hicimos las funciones basicas que se piden en el ejercicio 1A, como calcular la suma de una lista, el largo (cantidad de elementos), el promedio, el minimo y el maximo. Todo sin usar funciones built-in de python, solo con loops.

Despues en 1B implementamos el bubble sort para ordenar la lista, tanto ascendente como descendente. La funcion hace copias de la lista para no modificar la original.

En 1C agregamos la mediana, que ordena la lista y toma el valor del medio (o promedio de dos si es par), y la desviacion estandar, que calcula la varianza y despues la raiz cuadrada con aproximacion numerica.

## ITEM_2.py
Aqui tenemos una lista de estudiantes con sus nombres y notas (3 notas cada uno). En 2A calculamos el promedio de cada estudiante y los clasificamos en categorias como "Destacado", "Aprobado", "Suficiente" o "Reprobado" segun el promedio.

Tambien hicimos una funcion para generar un reporte completo con promedio, estado, nota max, min y rango.

En 2B contamos cuantos estudiantes hay en cada categoria de rendimiento.

## ITEM_3.py
En este ultimo archivo, tomamos la lista de estudiantes y aplanamos todas las notas en una sola lista grande. Despues contamos las frecuencias de cada nota (cuantas veces aparece cada una), y encontramos la moda (la nota que mas se repite).

Tambien hicimos un histograma horizontal con barras de X para visualizar las frecuencias, y una funcion para clasificar las notas en tramos como "1.0-3.9", "4.0-5.9", etc.

Eso es todo lo que pide la tarea. Esperamos que este bien hecho, aunque algunos calculos podrian optimizarse pero lo hicimos como se pidio sin usar librerias externas.