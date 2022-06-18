class Jarra:
    def __init__(self, capacidad, contenido):
        self.capacidad = capacidad
        self.contenido = contenido
    
    def llenarJarra(self):
        self.contenido = self.capacidad
    
    def mostrarContenido(self):
        print(self.contenido)

    def vertirEntreJarras(self, otra_jarra):
        otra_jarra = self.contenido

jarra5 = Jarra(5, 0)
jarra3 = Jarra(3, 0)
