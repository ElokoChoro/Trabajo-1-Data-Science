#1A FUNCIONES BASICAS 

def calcular_suma(datos): 
        suma = 0
        for numeros in datos: 
                suma += numeros
        return suma

def calcular_largo(datos):
        contador = 0
        for _ in datos:
                contador += 1
        return contador

def calcular_promedio(datos):
        promedio = calcular_suma(datos) / calcular_largo(datos)
        return promedio

def calcular_minimo(datos):
        minimo = None
        for numeros in datos:
                if minimo is None or numeros < minimo:
                        minimo = numeros 
        return minimo
def calcular_maximo(datos):
        maximo = None
        for numeros in datos:
                if maximo is None or numeros > maximo:
                        maximo = numeros
        return maximo

# 1B Ordenamiento Bubble Sort
def bubble_sort(datos, descendente=False):
    lista_ordenada = datos.copy()
    cantidad = calcular_largo(lista_ordenada)
    
    for pasada in range(cantidad - 1):
        intercambio_hecho = False
        
        for posicion in range(0, cantidad - pasada - 1):
            if descendente:
                if lista_ordenada[posicion] < lista_ordenada[posicion + 1]:
                    temp = lista_ordenada[posicion]
                    lista_ordenada[posicion] = lista_ordenada[posicion + 1]
                    lista_ordenada[posicion + 1] = temp
                    intercambio_hecho = True
            else:
                if lista_ordenada[posicion] > lista_ordenada[posicion + 1]:
                    temp = lista_ordenada[posicion]
                    lista_ordenada[posicion] = lista_ordenada[posicion + 1]
                    lista_ordenada[posicion + 1] = temp
                    intercambio_hecho = True
                    
        if not intercambio_hecho:
            break
    
    return lista_ordenada

#1B la función hace una copia de la lista original y realiza varias pasadas sobre la lista,
# en cada pasada va comparando los elementos y si están incorrectos, se intercambian, hasta que una pasada termine sin intercambios y retorna la lista ordenada.

# 1C Mediana y Desviación Estándar
def calcular_mediana(datos):
    
    lista_ordenada = bubble_sort(datos)
    cantidad = calcular_largo(lista_ordenada)
    
    if cantidad % 2 == 1:
        posicion_medio = cantidad // 2
        return lista_ordenada[posicion_medio]
    else:
        posicion_izq = cantidad // 2 - 1
        posicion_der = cantidad // 2
        return (lista_ordenada[posicion_izq] + lista_ordenada[posicion_der]) / 2

#1C al tener datos, ordena la lista usando la función creada anteriormente(bubble sort) y si la cantidad es impar retornara el valor del medio, 
# caso contrario se promediaran los dos valores centrales por lo cual es de tipo float.

def calcular_desviacion_estandar(datos):
        
    maximo_iteraciones=50
    cantidad = calcular_largo(datos)
    if cantidad == 0:
        return 0
    
    promedio = calcular_promedio(datos)
    suma_cuadrados = 0
        
    for elemento in datos:
        diferencia = elemento - promedio
        suma_cuadrados = suma_cuadrados + diferencia * diferencia
    
    varianza = suma_cuadrados / cantidad
    
    if varianza == 0:
        return 0
    
    aproximacion = varianza / 2 
    for _ in range(maximo_iteraciones):
        aproximacion = (aproximacion + varianza / aproximacion) / 2
    
    return aproximacion
        
#1C Si tiene datos, se calcula el promedio de los valores, luego se recorre cada elemento de la lista y se calcula la diferencia entre cada valor y el promedio dado,
# ese valor sera la diferencia y se usara para la suma de diferencias al cuadrado, con esa misma suma se calcula la varianza con la cantidad de datos, para terminar calculando la desviacion estandar.

# 1D Conversión de Temperaturas
def celsius_a_fahrenheit(grados_c):
    lista_fahrenheit = []
    for celsius in grados_c: 
        fahrenheit = celsius * 9 / 5 + 32
        lista_fahrenheit.append(fahrenheit)
    return lista_fahrenheit
#1D se crea una lista vacía para guardar resultados, luego recorre cada temperatura en Celsius y se aplica la formula de conversión, 
# ese resultado se agrega a la nueva lista, una vez finalizado el recorrido, se retorna la lista final.

# 1E REPORTE ESTADISTICO INTEGRADO
    while true:
        print("------------------------------------")
        print("    MENÚ DE ANÁLISIS CLIMÁTICO")
        print("------------------------------------")
        print("1. Ver Reporte Estadístico Integrado")
        print("2. Salir del programa")
        print("------------------------------------")

        opcion= input("ingresa la opcion")

        if opcion == "1":
                ciudades = [
                    {"ciudad": "Santiago", "temperaturas": [30.2, 28.5, 25.1, 18.3, 12.7, 9.5, 8.8, 10.1, 14.6, 19.3, 24.8, 28.9]},
                    {"ciudad": "Valparaiso", "temperaturas": [22.1, 21.8, 20.5, 17.2, 14.3, 12.1, 11.5, 12.0, 13.8, 16.5, 19.2, 21.0]},
                    {"ciudad": "Concepcion", "temperaturas": [20.5, 19.8, 17.2, 13.5, 10.8, 8.5, 7.9, 9.2, 11.5, 14.8, 17.5, 19.8]},
                    {"ciudad": "Temuco", "temperaturas": [22.3, 21.5, 18.0, 13.2, 9.5, 7.0, 6.5, 8.0, 10.5, 14.0, 17.8, 20.5]},
                    {"ciudad": "Punta Arenas", "temperaturas": [14.2, 13.5, 11.0, 7.5, 4.2, 2.0, 1.5, 3.0, 6.5, 9.8, 12.0, 13.8]},]

                for ciudad_Nombre in ciudades:
                    nombre = ciudad_Nombre["ciudad"]
                    lista_temp = ciudad_Nombre["temperaturas"]
                
                    largo = calcular_largo(lista_temp)
                    suma = calcular_suma(lista_temp)
                    promedio = calcular_promedio(lista_temp)
                    minimo = calcular_minimo(lista_temp)
                    maximo = calcular_maximo(lista_temp)
                    print("------------------------------------------------------")
                    print(f"Nombre de la ciudad: {nombre}")
                    print(f"El largo del arreglo es: {largo}")
                    print(f"La suma de las temperaturas es: {suma:.2f}")
                    print(f"El promedio de las temperaturas es: {promedio:.2f}")
                    print(f"La temepraturas minima de {nombre} es: {minimo}")
                    print(f"La temperatura masximi de {nombre} es : {maximo}")
        elif opcion == "2":
         print("Se cerro el programa adios")
        break
    else:
        print("por favor ingre una de las opciones dadas 1 o 2")
    






