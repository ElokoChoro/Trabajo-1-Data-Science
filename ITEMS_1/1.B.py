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
