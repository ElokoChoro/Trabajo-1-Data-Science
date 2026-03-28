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
