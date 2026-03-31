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
