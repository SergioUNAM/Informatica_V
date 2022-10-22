"""Universidad Nacional Autónoma de México
Facultad de Contaduría y Administración
Sistema de Universidad Abierta y Educación a Distancia
Licenciatura en Informática
Semestre 2023-1


Sergio Alberto Castelar Fernández
Cuenta: 309065638
Materia: Informática V (Programación Orientada a Objetos)
Unidad 4: Excepciones
Actividad 2
"""

# Crea en una clase llamada MovilException que tenga como Padre Exception, usando el constructor de la clase Exception para crear tu propia excepción personalizada. En la clase Movil estable dos atributos (si no los tienes), bateria_serie y horas_uso con sus respectivos métodos set y get, establecer con sethorasuso() a varios modelos y crear un método revisarHorasUso(tiempo_uso) en este método establece una condicion en donde si el horas es mayor a 17,000 lance la excepción MovilException cuyo mensaje sea "Este móvil" + marca + modelo necesita que se le realice el cambio de bateria".

# Desde la clase principal del código que tiene las instancias de los móviles llama al método revisarHorasUso(tiempo_uso) si ocurre la situación excepcional usa el mecanismo para cachar las excepciones por ejemplo en java (try, catch y finally) e imprime el mensaje que lanza la clasey en el finally muestra el total de móviles que debe de hacer el cambio de batería.


import random
from re import M
import string
import time



class Exception:
    def __init__(self, message):
        self.message = message


class MovilException(Exception):
    def __init__(self, message):
        super().__init__(message)

    # Creamos un método que retorna el paramentro de la excepción
    def __str__(self):
        return self.message


class Movil:
    # Clase Movil que hereda de DispositivoElectronico

    on_off_estado = True
    reconocimiento_facial = False

    # Constructor de la clase Movil
    def __init__(self, marca, modelo, color, precio, camara, procesador, huella_digital,
                 tipo_sensores, bateria_serie, horas_uso):

        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__precio = precio
        self.__camara = camara
        self.__procesador = procesador
        self.__huella_digital = huella_digital
        self.__tipo_sensores = tipo_sensores
        self.__bateria_serie = bateria_serie
        self.__horas_uso = horas_uso

    def __str__(self):
        return f"Atributos de clase {self.__class__.__name__} Marca: {self.__marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Camara: {self.camara}, Procesador: {self.procesador}, Huella digit+al: {self.huella_digital}, Sensores: {self.tipo_sensores}, Bateria: {self.bateria_serie}, Horas de uso: {self.horas_uso}"

    # Metodo para crear una imagen ascii sobre el estado de la bateria del dispositivo
    def cantidadUso(self):
        print("Método cantidadUso")
        if self.on_off_estado:
            print("Cantidad de uso")
            # Creamos una imagen ascii con la cantidad de uso de la bateria
            for i in range(0, self.horas_uso):
                print("=", end="")
            print()
        else:
            print("El dispositivo esta apagado")
        print()

    # GETTERS Y SETTERS

    # bateria_serie y horas_uso con sus respectivos métodos set y get
    @property  # getter bateria_serie
    def bateria_serie(self):
        return self.__bateria_serie

    @bateria_serie.setter  # setter bateria_serie
    def bateria_serie(self, bateria_serie):
        self.__bateria_serie = bateria_serie

    @property  # getter horas_uso
    def horas_uso(self):
        return self.__horas_uso

    @horas_uso.setter  # setter horas_uso
    def horas_uso(self, horas_uso):
        self.__horas_uso = horas_uso

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

    def __str__(self):
        return f"Atributos de clase {self.__class__.__name__} Marca: {self.__marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Camara: {self.camara}, Procesador: {self.procesador}, Huella digital: {self.huella_digital}, Sensores: {self.tipo_sensores}"

    # Metodo para encender el Movil con una animación en terminal
    def encender(self):
        print("Método encender")

        # animamos el encendido con simbolos
        if not self.on_off_estado:
            print("Encendiendo dispositivo")
            # Simulamos el encendido con una animación con simbolos
            for i in range(1, 6):
                print(f"{i} ...")
                time.sleep(1)
            self.on_off_estado = True
            print("Dispositivo encendido")
        else:
            print("El dispositivo ya esta encendido")
        print()

    def apagar(self):
        print("Método apagar")
        if self.on_off_estado:
            print("Apagando dispositivo")
            for i in range(1, 6):
                print(f"{i} ...")
                time.sleep(1)
            self.on_off_estado = False
            print("Dispositivo apagado")
        else:
            print("El dispositivo ya esta apagado")
        print()

    # Metodo para simular el uso de un sensor del telefono
    def usarSensor(self, sensor):
        print("Método usarSensor")
        if self.on_off_estado:
            if sensor in self.tipo_sensores:
                print(f"Usando sensor {sensor}")
            else:
                print(f"No se puede usar el sensor {sensor}")
        else:
            print("El dispositivo esta apagado")
        print()

    def tomarFoto(self):
        print("Método tomarFoto")
        if self.on_off_estado:
            if self.camara:
                print("Tomando foto")
            else:
                print("No se puede tomar foto")
        else:
            print("El dispositivo esta apagado")
        print()

    def realizarLlamada(self):
        print("Método realizarLlamada")
        if self.on_off_estado:
            print("Realizando llamada")
        else:
            print("El dispositivo esta apagado")
        print()

    def bloquear(self):
        print("Método bloquear")
        if self.on_off_estado:
            print("Bloqueando dispositivo")
        else:
            print("El dispositivo esta apagado")
        print()

    def desbloquear(self):
        print("Método desbloquear")
        if self.on_off_estado:
            print("Desbloqueando dispositivo")
        else:
            print("El dispositivo esta apagado")
        print()

    def abrirApp(self, nombreApp):
        print("Método abrirApp")
        if self.on_off_estado:
            print(f"Abrir app {nombreApp}")
        else:
            print("El dispositivo esta apagado")
        print()

    def subeVolumen(self, niveles):
        print("Método subeVolumen")
        if self.on_off_estado:
            print(f"Subiendo volumen {niveles} niveles")
        else:
            print("El dispositivo esta apagado")
        print()

    def bajaVolumen(self, niveles):
        print("Método bajaVolumen")
        if self.on_off_estado:
            print(f"Bajando volumen {niveles} niveles")
        else:
            print("El dispositivo esta apagado")
        print()

    # Metodo revisarHorasUso(tiempo_uso) que establece una condición en donde si tiempo_uso es mayor a 17000 horas lance cree un instancia de la clase MovilException cuyo mensaje sea "Este móvil" + marca + modelo necesita que se le realice el cambio de bateria"
    def revisarHorasUso(self, tiempo_uso):
        print("Revisando horas de uso")
        # Animamos la carga de la información
        for i in range(1, 6):
            print(f"{i} ...")
            time.sleep(1)
        if tiempo_uso > 17000:
            try:
                movilexception = MovilException(
                    f"Este móvil {self.marca} {self.modelo} necesita que se le realice el cambio de bateria")
            except:
                print("Error en la excepción")
            print(f"Tiempo de uso: {tiempo_uso}")
            print(movilexception.__str__())

        else:
            print(f"Tiempo de uso: {tiempo_uso}")
            print(f"{self.marca} {self.modelo} no necesita que se le realice el cambio de bateria")


def main():
    # Creamos varios objetos de la clase Movil, las lineas sentencias ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000) nos ayudan a generar valores aleatorios para los atributos num_serie y horas_uso respectivamente

    movil1 = Movil("Samsung", "Galaxy S10", "Negro", 5999, "12 MP", "Snapdragon 855", True,
                   ["Brillo", "Giroscopio", "Huella digital"],
                   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000))

    movil1.revisarHorasUso(movil1.horas_uso)

    movil2 = Movil("Huawei", "P30", "Blanco", 7999, "40 MP", "Kirin 980", True,
                   ["Brillo", "Giroscopio", "Huella digital"],
                   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000))
    movil2.revisarHorasUso(movil2.horas_uso)

    movil3 = Movil("Apple", "Iphone 11", "Gris", 12999, "12 MP", "A13 Bionic", True,
                   ["Brillo", "Giroscopio", "Huella digital"],
                   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000))
    movil3.revisarHorasUso(movil3.horas_uso)

    movil4 = Movil("Xiaomi", "Redmi Note 8", "Azul", 3999, "48 MP", "Snapdragon 665", True,
                   ["Brillo", "Giroscopio", "Huella digital"],
                   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000))
    movil4.revisarHorasUso(movil4.horas_uso)

    movil5 = Movil("Motorola", "G8", "Verde", 4999, "16 MP", "Snapdragon 665", True,
                   ["Brillo", "Giroscopio", "Huella digital"],
                   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), random.randint(16700, 20000))
    movil5.revisarHorasUso(movil5.horas_uso)


# Entry point
if __name__ == "__main__":
    main()
