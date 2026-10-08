peso_paquete = float(input("Ingrese el peso del paquete en kilogramos: "))

print("Ingrese un número del 1 al 3:")
print("Zona 1 (América): $5 por kg")
print("Zona 2 (Europa): $7.5 por kg")
print("Zona 3 (Resto del mundo): $10.0 por kg")

zona_destino = int(input("Seleccione la zona de destino: "))

if zona_destino == 1:
    tarifa = 5.0
    nombre_zona = "América"
elif zona_destino == 2:
    tarifa = 7.5
    nombre_zona = "Europa"
elif zona_destino == 3:
    tarifa = 10.0
    nombre_zona = "Resto del mundo"
else:
    tarifa = 0
    nombre_zona = "Desconocida"
    print(" Zona no válida. Debe ingresar 1, 2 o 3.")


if tarifa > 0:
    costo_total = peso_paquete * tarifa
    print(f"\n Paquete de {peso_paquete} kg")
    print(f" Zona: {nombre_zona}")
    print(f" Tarifa: ${tarifa} por kg")
    print(f"Costo total: ${costo_total}")
