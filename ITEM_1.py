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
    lista_ordenada = datos[:]
    cantidad = len(lista_ordenada)
    
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

# 1C Mediana y Desviación Estándar
def calcular_mediana(datos):
    
    lista_ordenada = bubble_sort(datos)
    cantidad = len(lista_ordenada)
    
    if cantidad % 2 == 1:
        posicion_medio = cantidad // 2
        return lista_ordenada[posicion_medio]
    else:
        posicion_izq = cantidad // 2 - 1
        posicion_der = cantidad // 2
        return (lista_ordenada[posicion_izq] + lista_ordenada[posicion_der]) / 2

def calcular_desviacion_estandar(datos):
    
    cantidad = len(datos)
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
    for _ in range(20):  
        aproximacion = (aproximacion + varianza / aproximacion) / 2
    
    return aproximacion

# 1E REPORTE ESTADISTICO INTEGRADO
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
    

    






