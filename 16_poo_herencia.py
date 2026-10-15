class Guerrero:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi poderoso nombre es: ", self.nombre)

class Saiyajin(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def transformarse(self):
        print("self.nombre", "Se transforma en Super Saiyajin")

goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse()

class Androide:
    nombre: str
    energia: str

    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia

    def mostrar_energia(self):
        print("Androide: ", self.nombre)
        print("Energia: ", self.energia)

class AndroideRecargable(Androide):
    def __init__(self, nombre, energia):
        super().__init__(nombre, energia)

    def recargar(self, cantidad: int):
        if cantidad >0:
            self.energia += cantidad

Androide17 = AndroideRecargable("Numero 17", 600)
print("========= ANTES DE RECARGAR ============")
Androide17.mostrar_energia()
Androide17.recargar(100)
print("========= ANTES DE RECARGAR ============")
Androide17.mostrar_energia()