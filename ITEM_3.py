# Lista de estudiantes con sus notas, como en el ejercicio
lista_de_estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},
    {"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]},
    {"nombre": "Valentina", "notas": [7.0, 6.8, 6.9]},
    {"nombre": "Javier", "notas": [4.0, 4.2, 4.1]},
    {"nombre": "Camila", "notas": [5.0, 5.5, 5.8]},
    {"nombre": "Martín", "notas": [3.5, 4.0, 4.2]},
    {"nombre": "Fernanda", "notas": [6.2, 6.5, 6.0]},
    {"nombre": "Tomás", "notas": [4.8, 5.0, 5.2]},
    {"nombre": "Josefa", "notas": [5.9, 6.0, 6.1]},
    {"nombre": "Matías", "notas": [3.8, 4.1, 4.0]},
    {"nombre": "Ignacio", "notas": [6.7, 6.9, 7.0]},
    {"nombre": "Daniela", "notas": [5.2, 5.4, 5.6]},
    {"nombre": "Sebastián", "notas": [4.3, 4.5, 4.7]},
    {"nombre": "Gabriela", "notas": [6.0, 6.2, 6.1]},
    {"nombre": "Felipe", "notas": [5.7, 5.8, 5.9]},
    {"nombre": "Antonia", "notas": [4.9, 5.0, 5.1]},
    {"nombre": "Vicente", "notas": [3.7, 4.0, 4.3]},
    {"nombre": "Paula", "notas": [6.3, 6.4, 6.5]}
]


def aplanar_notas(estudiantes):
    
    resultado = []
    contador_de_notas = 0  #para contar cuantas notas hay
    for estudiante in estudiantes:
        #por cada estudiante tomo sus notas
        for nota in estudiante["notas"]:
            resultado = resultado + [nota] #agrego la nota a la lista plana
            contador_de_notas += 1  #sumo uno al contador
    print("El total de notas es: ", contador_de_notas)
    print("Las notas aplanadas son: ", resultado)
    return resultado

def contar_frecuencias(datos):
    #diccionario para las frecuencias de cada nota
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1 #si esta en el diccionario sumo uno
        else:
            frecuencias[dato] = 1  #si no esta le dejo 1
    print("\nLas frecuencias de las notas son:")
    for valor, cantidad in frecuencias.items():
        print(f"  La nota {valor} aparece {cantidad} vez/veces")
    return frecuencias


def encontrar_moda(frecuencias):
    valor_que_mas_aparece = 0
    cantidad_maxima = 0
    for valor in frecuencias:
        cantidad = frecuencias[valor]
        if cantidad > cantidad_maxima:  #si esta cantidad es mayor que la maxima actualizo
            cantidad_maxima = cantidad
            valor_que_mas_aparece = valor
    print(f"\nLa moda es {valor_que_mas_aparece} porque aparece {cantidad_maxima} veces")
    return (valor_que_mas_aparece, cantidad_maxima)

#ejeccución de las funciones
notas_en_una_lista = aplanar_notas(lista_de_estudiantes)
frecuencia_de_notas = contar_frecuencias(notas_en_una_lista)
la_moda_calculada = encontrar_moda(frecuencia_de_notas)