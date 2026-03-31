# 1E REPORTE ESTADISTICO INTEGRADO
while True:
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
