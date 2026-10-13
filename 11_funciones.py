##FUNCIONES
def activar_sistema():
    print("== Sistema de Naboo ==")
    print("Sistema de control activado")

activar_sistema()

#FUNCIONES CON PARAMETRO

def saludar_jedi(nombre):
    print("Que la fuerza te acompañe : {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")

mostrar_nave("Caza N-1", 80)


#FUNCIONES QUE DEVUELVEN DATO O INFORMACION
#RETURN


def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante

resultado = calcular_combustible(100,25)
print(f"Combustible : {resultado}")

resultado = calcular_combustible(100,35)
print(f"Combustible : {resultado}")

resultado = calcular_combustible(100,15)
print(f"Combustible : {resultado}")