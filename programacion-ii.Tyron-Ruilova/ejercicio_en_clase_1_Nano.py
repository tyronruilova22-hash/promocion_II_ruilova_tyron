class RadarDragon:
    

    def __init__(self, region1, region2):
        self.region1 = region1
        self.region2 = region2
        
    def buscar_esferas(self):
        esferas_encontradas = self.region1 + self.region2
        esferas_faltantes = 7 - esferas_encontradas
        return esferas_encontradas, esferas_faltantes

radar_bulma = RadarDragon(3, 2)

encontradas, faltantes = radar_bulma.buscar_esferas()

print("--- Resultados del Radar de Bulma ---")
print(f"Esferas encontradas: {encontradas}")
print(f"Esferas faltantes para completar las 7: {faltantes}")