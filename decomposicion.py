# Creación de la clase Automovil

class Automovil:
    # Constructor
    def __init__(self, modelo, marca, color):
        # Inicializamos las variables de instancia
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"  # Clave privada
        self._motor = Motor(cilindros = 4)  # Clave privada

    def acelerar(self, tipo="despacio"):
        if tipo == "rapido":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = "en movimiento"


class Motor:
    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
