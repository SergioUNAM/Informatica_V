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
        print(self.__marca, self.__modelo, self.__color, self.__precio, self.__camara, self.__procesador, self.__huella_digital,
              self.__tipo_sensores)

    def encender(self):
        print("Método encender:")
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
        print("*" * 25)

    def apagar(self):
        print("Método apagar")
        if self.on_off_estado:
            self.on_off_estado = not self.on_off_estado
            print(f"{self.__marca} {self.__modelo}, apagado")
        print("*" * 25)

    def usarSensor(self, sensor):
        print("Método usarSensor")
        if sensor == 1:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, modificando brillo")
        elif sensor == 2:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, girando pantalla")
        elif sensor == 3:
            print(f"Utilizando el sensor {self.tipo_sensores[sensor - 1]}, desbloquendo teléfono")
        print("*" * 25)

    def tomarFoto(self):
        print("Método tomarFoto")
        print("Iniciando cámara")
        print("Capturando imagen")
        print("Guardando imagen")
        print("*" * 25)

    def realizarLlamada(self):
        print("Método realizarLlamada")
        num_telefono = input("Digite el telefono al que se desea marcar: ")
        print(f"Llamando al número {num_telefono}")
        print("*" * 25)

    def bloquear(self):
        print("Método bloquear")
        print("Bloqueando teléfono")
        print("Apagando pantalla")
        print("*" * 25)

    def desbloquear(self):
        print("Método desbloquear")
        if self.huella_digital == False:
            self.usarSensor(3)
        else:
            print("Utilizando sensor de huella digital")
        print("*" * 25)

    def abrirApp(self, nombreApp):
        print("Método abrirApp")
        print(f"Abriendo {nombreApp}")
        print("*" * 25)

    def subeVolumen(self, niveles):
        print("Método subeVolumen")
        print(f"Subiendo el volumen {niveles} niveles")
        print("*" * 25)

    def bajaVolumen(self, niveles):
        print("Método bajaVolumen")
        print(f"Bajando el volumen {niveles} niveles")
        print("*" * 25)


# Entry point, desde donde se ejecuta el programa principal
if __name__ == "__main__":

    # Teléfono 1
    Samsung = Movil("Samsung", "A13 4G", "Negro", 3600, "50 MP", "Octa core de 2,2GHz", True,
                    ["Acelerometro, Giroscopio"])
    print(f"Muestra información teléfono 1")
    Samsung.muestra_informacion()
    print()

    # Teléfono 2
    Xiaomi = Movil("Xiaomi", "Redmi note 8", "Negro", 3600, "48 MP", "Qualcomm Snapdragon 665", True,
                   ["Sensor de proximidad", "Sensor de luz", "Acelerometro", "Giroscopio",
                    "Lector de huellas dactilares"])
    print(f"Muestra información teléfono 2:")
    Xiaomi.muestra_informacion()
    print()

    # Telefono 3
    Apple = Movil("Apple", "Iphone 11", "blanco", 10999, "12 MP", "A13 Bionic", False,
                  ["Luz ambiental", "Giroscopio", "Reconocimiento Facial"])


    # Funciones especificas iphone
    #La manera correcta de implentar las funciones especificas es creando una nueva clase para los telefonos apple y aplicando la herencia de la clase general Movil, para el alcance de este ejercicio se hara de esta forma
    def llamado_métodos_apple():
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

    # Llama a todos los métodos de la instancia iphone
    llamado_métodos_apple()

    # Modificación de atributos mediante get y set
    print(f"GET\n "
          f"Modelo:{Apple.modelo}\n"
          f"Marca: {Apple.marca}")
    print("Modificamos el atributo marca")
    Apple.modelo = "Iphone 13 pro max"

    # Se muestran los nuevos atributos
    print("Mostramos los nuevos atributos")
    print(f"GET\n "
          f"Modelo:{Apple.modelo}\n"
          f"Marca: {Apple.marca}")
