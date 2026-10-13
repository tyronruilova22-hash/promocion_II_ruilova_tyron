# ciclo for

naves = [
    "Caza N-1",
    "Nave real de Naboo",
    "Transporte"
]
for nave in naves:
    print("INspeccionado", nave)

print("INspeccion realizada")


print("Inspeccion realizada")

droides = range(1,17,3)

print("Tipos de droides: ", type(droides))
for droide in droides:
    print(f"Reparar: droide B1- {droide}")
    print(f"Tipo de dato ronda: {type(droide)}")


planetas = [
    "Naboo", 
    "Tatooine", 
    "Coruscant",
    ]
recorrido = enumerate(planetas, start=1)

for position, planeta in recorrido:
    print(f"Planeta {position}: {planeta}")
    print(f"Tipo de dato planeta: {type(position)}: {type(planeta)}")

paises = [
    "Ecuador", 
    "Venezuela", 
    "Chile", 
    "Brazil",
    "Estados Unidos",
    ]

for pais in paises: 
    if pais == "Chile":
        continue
    if pais == "Brazil":
        break
    print(f"Pais Visitado: {pais}")

jedi = {}
print(jedi)

jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": "120",
    "estilo_pelea": "Sumurai",
    "misiones": ["guerra alderan", "secuestro palpatine", "Escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}
print(jedi_activo)

nave = dict(nombre="AZ-1", capacidad=8, turbo_laser=2)
print(nave)


jedi["nombre"] = "Luck"
jedi["fuerza"] = 150
print(jedi)



for clave, valor in jedi_activo.items():
    print(f"{clave} - {valor}")
