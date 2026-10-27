class Guerrero:
    nombre: str 
    poder_inicial: int
    horas: int
    
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        self.nombre = nombre
        self.poder_inicial = poder_inicial
        self.horas = horas

    def atacar(self):
        print(f"{self.nombre} realiza un ataque")

    def calcular_poder(self):
        return self.poder_inicial
    

class Goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "Utiliza Kamehameha")

    def calcular_pode(self):
        return self.poder_inicial + self.horas * 100
    
class Vegeta(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "utiliza final flash")

    def calcular_poder(self):
        return self.poder_inicial + self.horas * 150

goku = Goku("Gran goku", 150, 50)
vegueta = Vegeta("Vegeta", 200, 80)

goku.atacar()
vegueta.atacar()

goku.calcular_poder()
vegueta.calcular_poder()

print(goku.calcular_poder())
print(vegueta.calcular_poder())

