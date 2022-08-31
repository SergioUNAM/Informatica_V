# Clase Auto
class Auto:
    # Constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def Encender(self):
        print("Auto encendido")

    def Arrancar(self):
        pass

    def Frenar(self):
        pass


# Entry point
if __name__ == "__main__":
    auto = Auto("Chevrolet", "Corvette", 2022)
    print()
    print("Datos del vehiculo: ", auto.marca, auto.modelo, auto.año)

    auto.Encender()
