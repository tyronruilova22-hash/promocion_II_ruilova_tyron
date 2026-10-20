flota = [
    {"codigo": "B1-000", "modelo": "B1", "energia": 80, "activo": True}, 
    {"codigo": "DRO-000", "modelo": "D0", "energia": 100, "activo": True},
    {
        "codigo": "B1-001",
        "modelo": "B1",
        "energia": 90,
        "activo": True
    },
    {
        "codigo": "B1-002",
        "modelo": "B1",
        "energia": 40,
        "activo": True
    },
    {
        "codigo": "DRO-001",
        "modelo": "D0",
        "energia": 90,
        "activo": True
    }
]

cantidad_droides = len (droides)
print(cantidad_droides)
nuevo_droide = {
        {
        "codigo": "B1-004",
        "modelo": "B1",
        "energia": 100,
        "activo": True
    }

}
# CRUD
# CREATE
droides.append(nuevo_droide)
print(len(droides))
print(droides)
# READ
droide = droides[0]
print(f"Codigo : {droide["codigo"]}")
print(f"modelo : {droide["modelo"]}")
print(f"Energia : {droide["energia"]}")
print(f"Activo : {droide["activo"]}")
# UPDATE
droide = droides[2]
droide["codigo"]="DRO-002"
droide["energia"]=85
droide["activo"]=False
print(f"droides : {droides}")

#DELETE

eliminado = droide.pop(2)
print(f"droides : {droides}")