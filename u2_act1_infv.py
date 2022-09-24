# Sergio Alberto Castelar Fernandez
# Informatica V
# Semestre 2023-1
# Unidad 2
# Actividad 1

"""Crear una clase móvil que tenga los siguientes atributos “estados”: marca, modelo, color, precio, cámara, procesador, huella digital, tipo de sensores para cada uno de los atributos definir los métodos set y get.

Crear en la misma clase métodos “comportamientos” como: encender, apagar, usarSensor(TIPO_SENSOR), tomarFoto(), realizarLlama(num_telefono), bloquear(), desbloquear() y otros 3 métodos que tú consideres que necesita contener.

Crear tres constructores diferentes de móvil con base a algunos atributos definidos."""


class Movil:
    # Clase movil

    """ Clase que modelo un teléfono movil con los siguientes parametros:

    marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores

    """

    # Nota para contructores multiples en caso del lenguaje de programación Python

    """ Desafortunadamente, no podemos definir varios constructores para una sola clase en Python. Un método general para sortear esta limitación es utilizar un constructor de parámetros predeterminado. Un constructor de parámetros predeterminado es el que asigna automáticamente un valor a sus atributos de clase si no se pasa ningún parámetro al crear el objeto de clase. El constructor de parámetros predeterminado asigna el valor especificado al atributo de clase si se especifica algún valor durante la creación del objeto."""

    def __init__(self, marca="Apple", modelo="11", color="White", precio=10900, camara="12 MP", procesador="A14 Bionic",
                 huella_digital=False,
                 tipo_sensores=None):
        if tipo_sensores is None:
            tipo_sensores = ["Acelerometro", "Giroscopio", "Sensor de proximidad", "Sensor de luz ambiental"]
        self.__marca = marca  # Atributo privado
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.camara = camara
        self.procesador = procesador
        self.huella_digital = huella_digital
        self.tipo_sensores = tipo_sensores

    @property  # getter atributo marca
    def marca(self):
        return self.__marca

    @marca.setter  # setter atributo marca
    def marca(self, value):
        self.__marca = value

    # Método para comprobar algunos de los datos de las instancias creadas
    def muestra_datos(self):
        print(self.marca, self.modelo, self.color, self.tipo_sensores)

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
    Apple = Movil()  # Se genera el objeto con todos los datos predefinidos en el constructor
    Apple.muestra_datos()

    Samsung = Movil("Samsung", "A13 4G", "Negro", 3600, "50 MP", "Octa core de 2,2GHz", True,
                    ["Acelerometro, Giroscopio"])
    Samsung.muestra_datos()

    Xiaomi = Movil("Xiaomi", "Redmi note 8", "Negro", 3600, "48 MP", "Qualcomm Snapdragon 665", True,
                   ["Sensor de proximidada", "Sensor de luz", "Acelerometro", "Giroscopio",
                    "Lector de huellas dactilares"])
    Xiaomi.muestra_datos()

    Apple.marca = input("Digite la marca: ")
    print(f"La marca es {Apple.marca}")
