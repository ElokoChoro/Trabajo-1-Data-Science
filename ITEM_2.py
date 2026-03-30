estudiantes = [
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
# 2A Reporte de Rendimiento 
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


def promedio_estudiante(estudiante):
        notas_estudiantes = estudiante["notas"]
        promedio = calcular_promedio(notas_estudiantes)
        return promedio
    
def clasificar_rendimiento(promedio):
        if promedio >= 6.0:
                return "Destacado"
        elif promedio >= 4.0 and promedio <= 4.9:
                return "Sufiente"
        elif promedio >= 5.0 and promedio <= 5.9:
                return "Aprobado"
        else:
                return "Reprobado"
for persona in estudiantes:
        prom= promedio_estudiante (persona)
        rendimiento = clasificar_rendimiento(prom)
        print(f"Estudiante: {persona['nombre']} | promedio_{prom:.2f} |")
        
        
def generar_reporte(estudiantes):
        reporte = []
        for est in estudiantes:
                notas_almunos = est["notas"]
                promedio = calcular_promedio(notas_almunos)
                notas_maxima = calcular_maximo(notas_almunos)
                notas_minima = calcular_minimo(notas_almunos)
                estado = clasificar_rendimiento(promedio)
                rango = notas_maxima - notas_minima
                nuevo_dict = {
                        "nombre": est["nombre"],
                        "promedio": round(promedio, 2),
                        "estado": estado,
                        "nota_max": notas_maxima,
                        "nota_min": notas_minima,
                        "rango": round(rango, 2)
                }
                reporte.append(nuevo_dict)
        return reporte
# 2B CONTEO Y FILTRADO

def contar_por_estado(reporte):
    conteo = {}
    for estudiante in reporte:
        estado = estudiante["estado"]
        if estado in conteo:
            conteo[estado] += 1
        else:
            conteo[estado] = 1
    return conteo 


def filtrar_por_estado(reporte, estado_buscado):
    estudiantes_filtrados = []
    for estudiante in reporte:
        if estudiante["estado"] == estado_buscado:
            estudiantes_filtrados.append(estudiante)
    return estudiantes_filtrados
#2C Ordenamiento del reporte ( ya no cuenta, pero si se logra hacer el profe da un punto)







#2D BUSQUEDA DE ESTUDIANTES

def buscar_estudiante(reporte):
    nombre_buscado = input("\nIngresa el nombre del estudiante que deseas buscar: ")
    
    # Buscamos en el reporte
    for alumno in reporte:
        #.lower es para todo sea minisculas y compare mas facil y no falle
        if alumno["nombre"].lower() == nombre_buscado.lower(): 
            return alumno
        
    return None


def buscar_por_rango_promedio (reporte, minimo, maximo):
    estudiantes_rango_proemdio = []
    for estudiante in reporte:
        promedio =estudiante ['promedio']
        if promedio >= minimo and promedio<= maximo :
            estudiantes_rango_proemdio.append(estudiante)
    return estudiantes_rango_proemdio

