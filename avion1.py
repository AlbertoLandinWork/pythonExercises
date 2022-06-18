class Vehiculo:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self, vel, fren):
        self.velocidad += vel
        self.velocidad -= fren
    
    def girar(self, der, izq):
        self.direccion += der
        self.direccion -= izq


auto1 = Vehiculo('Tesla', 'Negro', '3')

auto1.acelerar(60, 0)
auto1.girar(45, 0)

print("-" * 55)
print("La velocidad del auto es " + str(auto1.velocidad) + " kilometros")
print("El auto ha girado " + str(auto1.direccion) + " grados")
print("-" * 55)

auto1.acelerar(0, 50)
auto1.girar(0, 55)

print("-" * 55)
print("La velocidad del auto es " + str(auto1.velocidad) + " kilometros")
print("El auto ha girado " + str(auto1.direccion) + " grados")
print("-" * 55)

class Vehiculo_aereo(Vehiculo):
    def __init__(self, marca, color, modelo, alt):
        super().__init__(marca, color, modelo)
        self.alt = alt
    
    def altura(self, sub, baj):
        self.alt += sub
        self.alt -= baj

avion1 = Vehiculo_aereo('boeing', 'blanco', '737', 0)

avion1.acelerar(5000, 0)
avion1.girar(23, 0)
avion1.altura(5000, 0)

print("-" * 55)
print("La velocidad del avion es " + str(avion1.velocidad) + " kilometros")
print("La dirección del avion es " + str(avion1.direccion) + " grados")
print("La altura del avíon es " + str(avion1.alt) + " pies.")
print("-" * 55)