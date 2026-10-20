#OPERADORES 
"""
Operadores aritméticos: +, -, *, /, %, **, //
"""

valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicación = valor1 * valor2
división = valor1 / valor2
módulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicación)
print("División:", división)
print("Módulo:", módulo)
print("Potencia:", potencia)


print("Tabla de multiplicar del 5")
multiplicador = 5
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)


print("Area de un triangulo con base 5 y altura 10: ", (5 * 10 / 2))

# Operador de comparación: ==, !=, >, <, >=, <=
"""
- == : Igual a
- != : Diferente de
- >  : Mayor que
- <  : Menor que
- >= : Mayor o igual que
- <= : Menor o igual que
"""

velocidad_anakin = 950
velocidad_sebulda = 900

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulda)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulda)
print("¿Anakin es igual a Sebulba?", velocidad_anakin == velocidad_sebulda)
print("¿Anakin es diferente a Sebulba?", velocidad_anakin != velocidad_sebulda)
print("¿Anakin es mas ràpido o igual a Sebulba?", velocidad_anakin >= velocidad_sebulda)
print("¿Anakin es maslento o igual a Sebulba?", velocidad_anakin <= velocidad_sebulda)

resultado = velocidad_anakin > velocidad_sebulda
print("Resultado de la comparación:", resultado)
print("Tipo de dato del resultado:", type(resultado))


#operadores logicos: and, or, not

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("Todos los sistemas funcionando:", motores_funcionando and escudos_funcionando)
print("Algunos sistemas estan funcionando:", motores_funcionando or escudos_funcionando)
print("Los motores no están funcionando:", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

cantidad_motores = 2
cantidad_alas = 4
combustible = 60

print("¿La nave tiene 2 motores y 4 alas?")
print(cantidad_motores == 2 and cantidad_alas == 4)

print("¿La nave tiene 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas == 4)

print("¿La nave no tiene 2 motores?")
print(not cantidad_motores >= 2)

print("¿La nave no tiene 2 motores y combustible >= 50?")
print(not cantidad_motores >= 2 and combustible >= 50)

velocidad = 100
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

# PRECENCIA DE OPERADORES
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""

resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)


# condicioal simple if
# simple

combustible = 10
if combustible >= 0:
    print("Puedes despegar")

# condicional if-else
creditos = 100 
precio_repuesto = 150
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto")


tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and tipo_repuesto != "ala" and tipo_repuesto != "escudo":
    print("El repuesto es un motor")
elif tipo_repuesto == "ala" and tipo_repuesto != "motor" and tipo_repuesto != "escudo":
    print("El repuesto es un ala")
elif tipo_repuesto == "escudo" and tipo_repuesto != "motor" and tipo_repuesto != "ala":
    print("El repuesto es un escudo")
else:
    print("Tipo de repuesto no válido")