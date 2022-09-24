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

    # Metodo constructor predefinido

    def __init__(self, marca="Apple", modelo="11", color="White", precio=10900, camara="12 MP", procesador="A14 Bionic",
                 huella_digital=False,
                 tipo_sensores=None):
        if tipo_sensores is None:
            tipo_sensores = ["Acelerometro", "Giroscopio", "Sensor de proximidad", "Sensor de luz ambiental"]

        self.__marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.camara = camara
        self.procesador = procesador
        self.huella_digital = huella_digital
        self.tipo_sensores = tipo_sensores

    # GETTERS Y SETTERS

    # marca
    @property  # getter atributo marca
    def marca(self):
        return self.__marca

    @marca.setter  # setter atributo marca
    def marca(self, value):
        self.__marca = value

    # modelo
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value

    # color
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    # precio
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    # camara
    @property
    def camara(self):
        return self.__camara

    @camara.setter
    def camara(self, value):
        self.__camara = value

    # procesador
    @property
    def procesador(self):
        return self.__procesador

    @procesador.setter
    def procesador(self, value):
        self.__procesador = value

    # huella_digital
    @property
    def huella_digital(self):
        return self.__huella_digital

    @huella_digital.setter
    def huella_digital(self, value):
        self.__huella_digital = value

    # tipo_sensores
    @property
    def tipo_sensores(self):
        return self.__tipo_sensores

    @tipo_sensores.setter
    def tipo_sensores(self, value):
        self.__tipo_sensores = value

    # Métodos de la clase Movil
    def muestra_datos(self):
        # Método para comprobar algunos de los datos de las instancias creadas
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
    Apple = Movil(modelo="11")  # Se genera el objeto con todos los datos predefinidos en el constructor
    Apple.muestra_datos()

    Samsung = Movil("Samsung", "A13 4G", "Negro", 3600, "50 MP", "Octa core de 2,2GHz", True,
                    ["Acelerometro, Giroscopio"])
    Samsung.muestra_datos()

    Xiaomi = Movil("Xiaomi", "Redmi note 8", "Negro", 3600, "48 MP", "Qualcomm Snapdragon 665", True,
                   ["Sensor de proximidad", "Sensor de luz", "Acelerometro", "Giroscopio",
                    "Lector de huellas dactilares"])
    Xiaomi.muestra_datos()

    movilx = Movil(modelo="1fjasoifao")
    movilx.muestra_datos()