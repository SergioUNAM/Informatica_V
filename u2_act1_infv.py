# Sergio Alberto Castelar Fernandez
# Informatica V
# Semestre 2023-1
# Unidad 2
# Actividad 1

"""Crear una clase móvil que tenga los siguientes atributos “estados”: marca, modelo, color, precio, cámara, procesador, huella digital, tipo de sensores para cada uno de los atributos definir los métodos set y get.

Crear en la misma clase métodos “comportamientos” como: encender, apagar, usarSensor(TIPO_SENSOR), tomarFoto(), realizarLlama(num_telefono), bloquear(), desbloquear() y otros 3 métodos que tú consideres que necesita contener.

Crear tres constructores diferentes de móvil con base a algunos atributos definidos."""


class Movil:
    def __init__(self, marca="Apple", modelo="11", color="White", precio=10900, camara="12 MP", procesador="A14 Bionic",
                 huella_digital=False,
                 tipo_sensores=None):
        if tipo_sensores is None:
            tipo_sensores = ["Acelerometro", "Giroscopio", "Sensor de proximidad", "Sensor de luz ambiental"]
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.camara = camara
        self.procesador = procesador
        self.huella_digital = huella_digital
        self.tipo_sensores = tipo_sensores

    # Método para comprobar algunos de los datos de las instancias creadas
    def muestra_datos(self):
        print(self.marca, self.modelo, self.color)

    def encender(self):
        pass

    def apagar(self):
        pass

    def usarSensor(self, tipo_sensor):
        pass

    def tomarFoto(self):
        pass

    def realizarLlamada(self, num_telefono):
        pass

    def bloquear(self, contraseña):
        pass

    def desbloquear(self):
        pass

    def abrirApp(self):
        pass

    def subeVolumen(self):
        pass

    def bajaVolumen(self):
        pass


# Entry point, desde donde se ejecuta el programa principal
if __name__ == "__main__":
    movil1 = Movil()
    movil1.muestra_datos()

    movil2 = Movil("Samsung")
    movil2.muestra_datos()
