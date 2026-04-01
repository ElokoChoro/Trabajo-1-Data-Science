#3a) 
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

#3B
def generar_histograma(frecuencias, ancho_max=25):
    """Imprime histograma horizontal con barras de X."""
    if not frecuencias:
        print("No hay datos para graficar.")
        return
        
    max_frecuencia = max(frecuencias.values())
    
    print("\n  HISTOGRAMA DE NOTAS ")
    
    # Ordenamos un poco las notas para que el gráfico se vea de menor a mayor
    for categoria, cantidad in sorted(frecuencias.items()):
        if max_frecuencia > 0:
            largo_barra = int((cantidad / max_frecuencia) * ancho_max)
        else:
            largo_barra = 0
            
        barra = "X" * largo_barra
        #.ljust es un justificador hacia la izquierda
        print(f"Nota {str(categoria).ljust(5)} | {barra} ({cantidad})")

#3C
def clasificar_en_tramos(datos, tramos):
    """
    tramos = {"1.0-3.9": (1.0, 3.9), "4.0-5.9": (4.0, 5.9), ...}
    Retorna dict con cantidad por tramo.
    """
    
    # 1. Preparamos nuestro diccionario de resultados
    # Lo inicializamos con los nombres de los tramos y cantidad 0
    resultados = {}
    for nombre_tramo in tramos:
        resultados[nombre_tramo] = 0
        
    # 2. Tomamos cada número de nuestra lista de datos
    for numero in datos:
        
        # 3. Por cada número, revisamos todos los tramos disponibles
        # .items() nos da el nombre ("1.0-3.9") y los límites (1.0, 3.9)
        for nombre_tramo, limites in tramos.items():
            
            minimo = limites[0] # El primer valor de la tupla, ej: 1.0
            maximo = limites[1] # El segundo valor de la tupla, ej: 3.9
            
            # 4. Preguntamos: ¿El número está dentro de este tramo?
            if minimo <= numero <= maximo:
                resultados[nombre_tramo] += 1
                
                # Si ya encontramos su tramo, dejamos de buscar en los demás
                # y pasamos al siguiente número gracias a "break"
                break 
                
    return resultados
#───────────────────────────────────────────────────────
#3d)

texto = """
La ciencia de datos es un campo interdisciplinario que utiliza
métodos científicos y algoritmos para extraer conocimiento de
los datos. La estadística y la programación son herramientas
fundamentales para un científico de datos. Los datos pueden
ser estructurados o no estructurados. El análisis de datos
permite tomar decisiones basadas en evidencia.
"""


def limpiar_texto(texto):
    #funcion basica de python transforma mayusculas a minusculas
    texto = texto.lower()
    
    #funcion que reemplaza los saltos de linea por espacios
    texto = texto.replace("\n", " ")
    
    #caracteres qye sacaremos del texto
    puntuacion = ".,;:!?()[]{}\"'¿¡-_"
    texto_limpio = ""
    
    #recorre cada carácter del texto
    for caracter in texto:
        #si el carácter NO está en la puntuación, lo agregamos
        if caracter not in puntuacion:
            texto_limpio = texto_limpio + caracter
    
    print("Texto limpio:", texto_limpio)
    return texto_limpio

def frecuencia_palabras(texto_limpio):
    palabras = []
    palabra_actual = ""
    
    for caracter in texto_limpio:
        if caracter == " ": #si hay espacio termina la palabra
            if palabra_actual != "": #distinto de vacio, agregar palabra a la lista
                palabras = palabras + [palabra_actual]
                palabra_actual = ""
        else:
            #else, agregamos el caracter a la palabra actual
            palabra_actual = palabra_actual + caracter
    
    #oara el loop, evita agregar cadena vacia
    if palabra_actual != "":
        palabras = palabras + [palabra_actual]

    #diccionario de frecuencia
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1 #si la palabra ya existe en el diccionario suma 1
        else:
            frecuencias[palabra] = 1 #primera vez inicializa en 1
    
    print("\nFrecuencia de palabras:", frecuencias)
    return frecuencias


def top_n_palabras(frecuencias, n=10):
    #convertir el diccionario a una lista de tuplas ej:(palabra, cantidad)(hola, 1)
    pares = []
    for palabra, cantidad in frecuencias.items():
        pares = pares + [(palabra, cantidad)]

    #bubble sort para ordenar por frecuencia (de mayor a menor)
    largo = 0
    for _ in pares:
        largo += 1

    #compara elementos y intercambiar si es necesario
    for i in range(largo - 1):
        for j in range(largo - 1 - i):
            #si el elemento actual es menor que el siguiente, intercambia los elementos
            if pares[j][1] < pares[j + 1][1]:
                temp = pares[j]
                pares[j] = pares[j + 1]
                pares[j + 1] = temp

    #toma solo los primeros n elementos
    top = []
    contador = 0
    for par in pares:
        if contador < n:
            top = top + [par]
            contador += 1

    print(f"\nTop {n} palabras más frecuentes:")
    for palabra, cantidad in top:
        print(f"  '{palabra}': {cantidad}")
    return top


def diversidad_lexica(texto_limpio):
    #Igual que en frecuencia_palabras, separamos el texto en una lista de 
    #palabras recorriendo caracter por caracter esto nos da "todas" 
    #las palabras incluyendo repetidas, por ejemplo:
    #["la", "ciencia", "de", "datos", "la", "de", "datos", "datos"]
    palabras = []
    palabra_actual = ""
    for caracter in texto_limpio:
        if caracter == " ":
            if palabra_actual != "":
                palabras = palabras + [palabra_actual]
                palabra_actual = ""
        else:
            palabra_actual = palabra_actual + caracter
    if palabra_actual != "":
        palabras = palabras + [palabra_actual]

    #crea una lista de palabras únicas (sin repetidas)
    unicas = []
    for palabra in palabras:
        encontrada = False
        #revisa si la palabra ya está en la lista de únicas
        for u in unicas:
            if u == palabra:
                encontrada = True
        # Si no se encuentra, la agregamos a la lista unica
        if not encontrada:
            unicas = unicas + [palabra]

    # Contar el total de palabras (incluyendo repetidas)
    total = 0
    for _ in palabras:
        total += 1

    # Contar el total de palabras únicas
    total_unicas = 0
    for _ in unicas:
        total_unicas += 1

    #calculo del ratio para medir la diversidad léxica
    #entre más alto el ratio, más diversa es la selección de palabras
    ratio = total_unicas / total
    print(f"\nDiversidad léxica: {total_unicas} únicas / {total} total = {ratio:.2f}")
    return ratio

#3E)

def calcular_bigramas(texto_limpio):
    palabras = []
    palabra_actual = ""
    for caracter in texto_limpio:
        if caracter == " ":
            if palabra_actual != "":
                palabras = palabras + [palabra_actual]
                palabra_actual = ""
        else:
            palabra_actual = palabra_actual + caracter
    if palabra_actual != "":
        palabras = palabras + [palabra_actual]

    #diccionario para guardar los bigramas y su frecuencia
    bigramas = {}
    
    i = 0
    while i < len(palabras) - 1: #terminar en i-1(no hay mas palabras para formar el par)
        #crea el bigrama uniendo dos palabras con espacio
        bigrama = palabras[i] + " " + palabras[i + 1]
        
        #si ya existe suma 1 al contador
        if bigrama in bigramas:
            bigramas[bigrama] += 1
        #else inicializa el contador en 1
        else:
            bigramas[bigrama] = 1
        
        #avanza a la siguiente palabra
        i += 1

    print("\nBigramas (pares de palabras):")
    for bigrama, cantidad in bigramas.items():
        print(f"  '{bigrama}': {cantidad}")
    return bigramas

#EJECUCCION

texto_limpio = limpiar_texto(texto)
frecuencias = frecuencia_palabras(texto_limpio)
top = top_n_palabras(frecuencias, n=10)
diversidad = diversidad_lexica(texto_limpio)
bigramas = calcular_bigramas(texto_limpio)
