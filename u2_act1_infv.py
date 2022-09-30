import time

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

    on_off_estado = False
    reconocimiento_facial = False
    def __init__(self, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__precio = precio
        self.__camara = camara
        self.__procesador = procesador
        self.__huella_digital = huella_digital
        self.__tipo_sensores = tipo_sensores

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
        return self._color

    @color.setter
    def color(self, value):
        self.__color = value

    # precio
    @property
    def precio(self):
        return self._precio

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
    def muestra_informacion(self):
        # Método para comprobar algunos de los datos de las instancias creadas
        print(self.marca, self.modelo, self.color, self.precio, self.camara, self.procesador, self.huella_digital,
              self.tipo_sensores)

    def encender(self):
        if not self.on_off_estado:
            self.on_off_estado = True
            print("Encendiendo", end=".")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(f"{self.marca} {self.modelo} está encendido")
        else:
            print(f"{self.marca} {self.modelo} está encendido")
        print()

    def apagar(self):
        if self.on_off_estado:
            self.on_off_estado = not self.on_off_estado
            print(f"{self.__marca} {self.__modelo}, apagado")
        print()

    def usarSensor(self, sensor):
        if sensor == 1:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, modificando brillo")
        elif sensor == 2:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, girando pantalla")

        elif sensor == 3:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, desbloquendo teléfono")
        print()

    def tomarFoto(self):
        print("Iniciando cámara")
        print("Capturando imagen")
        print("Guardando imagen")
        print()

    def realizarLlamada(self):
        num_telefono = input("Digite el telefono al que se desea marcar")
        print(f"Llamando al número {num_telefono}")
        print()

    def bloquear(self):
        print("Bloqueando teléfono")
        print("Apagando pantalla")
        print()

    def desbloquear(self):
        if self.huella_digital == False:
            self.usarSensor(3)
        else:
            print("Utilizando sensor de huella digital")
        print()

    def abrirApp(self, nombreApp):
        print(f"Abriendo {nombreApp}")
        print()

    def subeVolumen(self, niveles):
        print(f"Subiendo el volumen {niveles} niveles")
        print()

    def bajaVolumen(self, niveles):
        print(f"Bajando el volumen {niveles} niveles")
        print()


# Entry point, desde donde se ejecuta el programa principal
if __name__ == "__main__":
    Apple = Movil("Apple", "Iphone 11", "blanco", 10999, "12 MP", "A13 Bionic", False,
                  ["Luz ambiental", "Giroscopio", "Reconocimiento Facial"])


    # Funciones especificas iphone
    #La manera correcta de implentar las funciones especificas es creando una nueva clase para los telefonos apple y aplicando la herencia de la clase general Movil, para el alcance de este ejercicio se hara de esta forma
    def cambio_de_luz_iphone():
        Apple.usarSensor(1)

    def girar_pantalla_iphone():
        Apple.usarSensor(2)

    # Utilizando los métodos solicitados
    Apple.encender()
    Apple.apagar()
    Apple.desbloquear()
    Apple.tomarFoto()
    cambio_de_luz_iphone()
    girar_pantalla_iphone()
    Apple.realizarLlamada()
    Apple.abrirApp("Facebook")
    Apple.subeVolumen(3)
    Apple.bajaVolumen(4)


    #Teléfono 2
    Samsung = Movil("Samsung", "A13 4G", "Negro", 3600, "50 MP", "Octa core de 2,2GHz", True,
                    ["Acelerometro, Giroscopio"])

    #Teléfono 3
    Xiaomi = Movil("Xiaomi", "Redmi note 8", "Negro", 3600, "48 MP", "Qualcomm Snapdragon 665", True,
                   ["Sensor de proximidad", "Sensor de luz", "Acelerometro", "Giroscopio",
                    "Lector de huellas dactilares"])
