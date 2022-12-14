# Sergio Alberto Castelar Fernández
# Cuenta: 309065638
# Materia: Informática V (Programación Orientada a Objetos)
# Unidad 3: Herencia
# Actividad 1


"""Empleando el mismo programa “código fuente” de la unidad 1, realiza la herencia creando una clase padre llamada DipositivoElectronico y dos clases hija (al mismo nivel de la clase Movil) llamadas: Computadora y ConsolaVideoJuego, a partir de la clase Movil crea dos subclases “clases hijas” Tablet y Warable, para la clase Warable se crean “derivan” dos clases hija una llamada Reloj y otra LentesVR. Crear para cada una de las subclases diferentes dos atributos únicos que los caractericen y crear un constructor para cada clase.



Desde la clase principal crea diferentes warables relojes y lentesVR que a través del uso de la herencia puedan establecer a través de la clase padre valores como el modelo, la marca, etc. y también ocupe los métodos para acceder a los valores propios de la clase, crear en estas clases hija dos constructores y en estas clases definir un método para realizar sobre carga y otro método para realizar sobre escritura. Para la sobre escritura el mismo método debe de estar definido también en las clases padre, es decir, en las clases Móvil, Tablet y Warable. A partir de ellos crear 2 tipos de dispositivos electrónicos uno para Computadora y otro para ConsolaVideoJuego, también para las otras clases (Móvil, Tablet y Warable), utilizar los constructores y los métodos set y get; y de la relación de las clases preguntar si (if) una Tablet es un tipo de DispositivoElectronico, si un Warable es un tipo de Movil y si una Computadora es un tipo de Movil, para esto emplear instanceof o su equivalente, e imprimir la salida en pantalla.



Realiza el código en un lenguaje orienta a objetos en un editor de textos o IDE, los códigos fuente comprímelos en un archivo .zip o .rar. Utiliza comentarios para poner tu nombre completo y comenta las líneas principales de cómo creaste los objetos y manejaste los constructores y los métodos, al final sube el archivo a la sección de la actividad correspondiente."""


import time
import random

class DispositivoElectronico:

    def __init__(self, num_serie, sistema_operativo):
        self.num_serie = num_serie
        self.sistema_operativo = sistema_operativo


class Movil(DispositivoElectronico):
    # Clase Movil que hereda de DispositivoElectronico

    on_off_estado = False
    reconocimiento_facial = False

    def __init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                 tipo_sensores):
        super().__init__(num_serie, sistema_operativo)
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
        print(self.__marca, self.__modelo, self.__color, self.__precio, self.__camara, self.__procesador,
              self.__huella_digital,
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
        if not self.huella_digital:
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


class Tablet(Movil):
    def __init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                 tipo_sensores, tamaño_pantalla, capacidad_bateria):
        super().__init__(num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                         tipo_sensores)
        self.tamaño_pantalla = tamaño_pantalla
        self.capacidad_bateria = capacidad_bateria


class Wearable(Movil):
    def __int__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                tipo_sensores, categoria, conexion):
        super().__init__(num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                         tipo_sensores)
        self.categoria = categoria
        self.conexion = conexion

class Reloj(Wearable):  # Herencia multiple python
    def __init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                 tipo_sensores, categoria, conexion, gama, peso):
        super().__init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador,
                         huella_digital, tipo_sensores)
        super().__init__(self,categoria, conexion)
        self.gama = gama
        self.peso = peso

    # Sobreescritura y sobrecarga del método muestra información de la clase padre Movil
    def muestra_informacion(self):
        super().muestra_informacion()


#Clase LentesVR que hereda de Wearable con dos atributos adicionales
class LentesVR(Wearable):
    def __init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador, huella_digital,
                 tipo_sensores, categoria, conexion, tipo_lente, tipo_pantalla):
        super().__init__(self, num_serie, sistema_operativo, marca, modelo, color, precio, camara, procesador,
                         huella_digital, tipo_sensores)
        super().__init__(self, categoria, conexion)
        self.tipo_lente = tipo_lente
        self.tipo_pantalla = tipo_pantalla

    # Sobreescritura y sobrecarga del método muestra información de la clase padre Movil
    def muestra_informacion(self):
        super().muestra_informacion()


class Computadora(DispositivoElectronico):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, ram, tamaño_memoria):
        super().__init__(num_serie, sistema_operativo)
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.tamaño_memoria = tamaño_memoria


class ConsolaVideoJuego(DispositivoElectronico):
    def __init__(self, num_serie, sistema_operativo, plataforma, almacenamiento, año_lanzamiento):
        super().__init__(num_serie, sistema_operativo)
        self.plataforma = plataforma
        self.almacenamiento = almacenamiento
        self.año_lanzamiento = año_lanzamiento
    
    #Método para inicializar un juego
    def iniciarJuego(self):
        catalogo = ["Halo", "Gears of War", "Forza", "Fifa", "Minecraft"]
        #Seleccionar un juego al azar
        juego = random.choice(catalogo)


# Clase principal python
def main():
    # Instanciación 1 de un objeto de la clase Weareable, se asignan todos los atributos heredados de la clase Movil
    appleWatch = Wearable("F23IOSF", "Watch OS 7", "Apple", "Series 7", "Space Gray", 8999, "N/A",
                          "Apple S8 (doble núcleo de 64 bits)", "N/A",
                          ["Giroscopio", "Sensor de temperatura", "Detector de choques", "Frecuencia cardiaca"])

    # Instanciación 2 de un objeto de la clase Weareable, se asignan todos los atributos heredados de la clase Movil
    galaxyWatch = Wearable("EP43L3_302", "Wear OS", "Samsung", "Galaxy Watch5", "Negro", 5999, "N/A", "Exynos W920",
                           "N/A", ["Frecuencia cardíaca", "Señal eléctrica cardíaca", "Bioimpedancia eléctrica",
                                   "Sensor de temperatura", "Acelerómetro", "Barómetro", "Giroscopio",
                                   "Sensor magnético"])



    print(appleWatch.modelo, appleWatch.marca)
    appleWatch.muestra_informacion()
    print(appleWatch.modelo)
    print(appleWatch.num_serie)
    print(appleWatch.huella_digital)


# Entry point python
if __name__ == "__main__":
    main()
