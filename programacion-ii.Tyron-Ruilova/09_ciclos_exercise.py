flota = [
    {
        "nombre": "Nave Exploradora",
        "combustible": 50,
        "droides": ["R2-D2", "R2-A6"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 35,
        "droides": ["R2-N3"]
    },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droides": ["R2-D2", "R2-A6"]
    }
]

naves_listas = 0
naves_recarga = 0
total_droides = 0
total_ciclos = 0

for numero, nave in enumerate(flota, start=1):
    print(f"--- Nave {numero}: {nave['nombre']} ---")
    print(f"Combustible inicial: {nave['combustible']} unidades")

    if nave["combustible"] >= 50:
        print("Estado inicial: LISTA ")
        naves_listas += 1

    else:
        print("Estado inicial: RECARGA ")
        naves_recarga += 1

        ciclo = 0
        while nave["combustible"] < 50:
            ciclo += 1
            nave["combustible"] += 10
            if nave["combustible"] > 100:
                nave["combustible"] = 100

        total_ciclos += ciclo
        print(f"Recarga completada en {ciclo} ciclos")
        print(f"Estado final: LISTA (combustible: {nave['combustible']})")

    total_droides += len(nave["droides"])
    for droide in nave["droides"]:
        print(f"  - Droide: {droide}")

print("=======================================")
print("             RESUMEN")
print("=======================================")
print(f"Total de naves:              {len(flota)}")
print(f"Naves listas inicialmente:   {naves_listas}")
print(f"Naves que necesitaron recarga: {naves_recarga}")
print(f"Total de droides:            {total_droides}")
print(f"Total de ciclos de recarga:  {total_ciclos}")
print(f"¿Toda la flota lista?:       {'SÍ' if all(n['combustible'] >= 50 for n in flota) else 'NO'}")

