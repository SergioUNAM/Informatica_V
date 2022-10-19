# Sergio Alberto Castelar Fernández
# Cuenta: 309065638
# Materia: Informática V (Programación Orientada a Objetos)
# Unidad 3: Herencia
# Actividad 1


"""Empleando el mismo programa “código fuente” de la unidad 1, realiza la herencia creando una clase padre llamada DipositivoElectronico y dos clases hija (al mismo nivel de la clase Movil) llamadas: Computadora y ConsolaVideoJuego, a partir de la clase Movil crea dos subclases “clases hijas” Tablet y Warable, para la clase Warable se crean “derivan” dos clases hija una llamada Reloj y otra LentesVR. Crear para cada una de las subclases diferentes dos atributos únicos que los caractericen y crear un constructor para cada clase.



Desde la clase principal crea diferentes warables relojes y lentesVR que a través del uso de la herencia puedan establecer a través de la clase padre valores como el modelo, la marca, etc. y también ocupe los métodos para acceder a los valores propios de la clase, crear en estas clases hija dos constructores y en estas clases definir un método para realizar sobre carga y otro método para realizar sobre escritura. Para la sobre escritura el mismo método debe de estar definido también en las clases padre, es decir, en las clases Móvil, Tablet y Warable. A partir de ellos crear 2 tipos de dispositivos electrónicos uno para Computadora y otro para ConsolaVideoJuego, también para las otras clases (Móvil, Tablet y Warable), utilizar los constructores y los métodos set y get; y de la relación de las clases preguntar si (if) una Tablet es un tipo de DispositivoElectronico, si un Warable es un tipo de Movil y si una Computadora es un tipo de Movil, para esto emplear instanceof o su equivalente, e imprimir la salida en pantalla.



Realiza el código en un lenguaje orienta a objetos en un editor de textos o IDE, los códigos fuente comprímelos en un archivo .zip o .rar. Utiliza comentarios para poner tu nombre completo y comenta las líneas principales de cómo creaste los objetos y manejaste los constructores y los métodos, al final sube el archivo a la sección de la actividad correspondiente."""

from datetime import date
import time


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

# Crear dos clases al mismo nivel de la clase Movil llamadas Computadora y ConsolaVideojuego

# Clase Computadora que hereda de DispositivoElectronico
class Computadora(DispositivoElectronico):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, ram, tamaño_memoria):
        super().__init__(num_serie, sistema_operativo)
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.tamaño_memoria = tamaño_memoria
    
    def __str__(self):
        return f"Computadora: {self.marca} {self.modelo}, {self.tipo}, {self.ram}, {self.tamaño_memoria} \n"

    def verificar_estado_garantia(self):
        print("Método verificar_estado_garantia")
        print(f"La computadora {self.marca} {self.modelo} con número de serie {self.num_serie} tiene garantía hasta el 31 de diciembre de 2023")
        print("Desea ampliar la garantía? (S/N)")
        respuesta = input()
        if respuesta == "S":
            try:
                print("Digite el número de meses que desea ampliar la garantía")
                meses = int(input())
                print(f"La garantía del producto con número de serie {self.num_serie} se ha ampliado por {meses} meses")
                print(f"Fecha de renovación {date.today()}")
                print(f"Graacias por confiar en nosotros")
            except ValueError:
                print("El número de serie y el número de meses deben ser números enteros")
        else:
            print("Recuerde que la garantía de su producto termina el 31 de diciembre de 2023")
        print()


# Clase ConsolaVideoJuego que hereda de DispositivoElectronico
class ConsolaVideoJuego(DispositivoElectronico):
    def __init__(self, num_serie, sistema_operativo, plataforma, almacenamiento, año_lanzamiento):
        super().__init__(num_serie, sistema_operativo)
        self.plataforma = plataforma
        self.almacenamiento = almacenamiento
        self.año_lanzamiento = año_lanzamiento

    #Método para inicializar un juego para la consola
    def inicializarJuego(self, nombreJuego):
        print("Método inicializarJuego")
        print(f"Inicializando {nombreJuego}")
        print()

    def __str__(self):
        return f"Consola de videojuegos: {self.plataforma}, {self.almacenamiento}, {self.año_lanzamiento} \n"

    #Método para actualizar el sistema operativo de la consola
    def actualizarSistemaOperativo(self):
        print("Método actualizarSistemaOperativo")
        print(f"Actualizando sistema operativo {self.sistema_operativo}")
        print("Descargando actualización")
        print("Instalando actualización")
        print("Reiniciando consola")
        print("Sistema operativo actualizado")
        print()

    #Método para actualizar el juego de la consola
    def actualizarJuego(self, nombreJuego):
        print("Método actualizarJuego")
        print(f"Actualizando {nombreJuego}")
        print("Descargando actualización")
        print("Instalando actualización")
        print("Reiniciando consola")
        print(f"{nombreJuego} actualizado")
        print()

# Crear una clase llamada Tablet que herede de Movil
class Tablet(Movil):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores, tamaño_pantalla, capacidad_bateria):
        super().__init__(num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador,
                         huella_digital, tipo_sensores)
        self.tamaño_pantalla = tamaño_pantalla
        self.capacidad_bateria = capacidad_bateria

# Crear una clase llamada Wearable que herede de Movil
class Wearable(Movil):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores, categoria, conexion):
        super().__init__(num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador,huella_digital, tipo_sensores)
        self.__categoria = categoria
        self.__conexion = conexion
    
# Getters y Setters para la clase Wearable

# categoria
    @property # getter atributo categoria
    def categoria(self):
        return self.__categoria
    
    @categoria.setter # setter atributo categoria
    def categoria(self, value):
        self.__categoria = value

# Crear una clase llamada Reloj que herede de Wearable con los atributos adicionaes: gama y peso
class Reloj(Wearable):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores, categoria, conexion, gama, peso):
        super().__init__(num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador,
                         huella_digital, tipo_sensores, categoria, conexion)
        self.gama = gama
        self.peso = peso


    # Sobreescribir el método muestra_información de la clase Movil
    def muestra_informacion(self):
        print("Método muestra_informacion de la clase Reloj")
        print(f"gama: {self.gama}, peso: {self.peso}")
        super().muestra_informacion()

    
# Crear una clase llamada LentesVR que herede de Wearable con los atributos adicionales: tipo_lente y tipo_pantalla
class LentesVR(Wearable):
    def __init__(self, num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores, categoria, conexion, tipo_lente, tipo_pantalla):
        super().__init__(num_serie, sistema_operativo, tipo, marca, modelo, color, precio, camara, procesador,
                         huella_digital, tipo_sensores, categoria, conexion)
        self.__tipo_lente = tipo_lente
        self.__tipo_pantalla = tipo_pantalla

# Getters y Setters para la clase LentesVR
# tipo_lente
    @property # getter atributo tipo_lente
    def tipo_lente(self):
        return self.__tipo_lente

    @tipo_lente.setter # setter atributo tipo_lente
    def tipo_lente(self, value):
        self.__tipo_lente = value

# tipo_pantalla
    @property # getter atributo tipo_pantalla
    def tipo_pantalla(self):
        return self.__tipo_pantalla
    
    @tipo_pantalla.setter # setter atributo tipo_pantalla
    def tipo_pantalla(self, value):
        self.__tipo_pantalla = value


    # Sobreescribir el método muestra_información de la clase Movil
    def muestra_informacion(self):
        print("Método muestra_informacion dentro de la clase lentesVR")
        super().muestra_informacion()

#Función principal
def main():

    #Función que nos permite verificar a que clase pertenece cada instancia
    #Lista de todas las clases creadas
    def verificarInstancia(instancia):
        clases = [DispositivoElectronico, Movil, Computadora, ConsolaVideoJuego, Tablet, Wearable, Reloj, LentesVR]
        for clase in clases:
            if isinstance(instancia, clase):
                print(f"La instancia pertenece a la clase {clase.__name__}")
            else:
                continue
        print()

    # Crear dos instancias de la clase Computadora
    # Instancia 1 de la clase Computadora
    print("Primera instancia de la clase Computadora")
    computadora1 = Computadora("123456", "Windows", "Escritorio", "HP", "Pavilion", "8GB", "1TB")
    print(computadora1)

    # Verificamos a que instancia pertenece el objeto computadora1
    verificarInstancia(computadora1)

    # Aplicamos los metodos de la clase Computadora
    computadora1.verificar_estado_garantia()

    #Instancia 2 de la clase Computadora
    print("Segunda instancia de la clase Computadora")
    computadora2 = Computadora("654321", "Linux", "Portatil", "Lenovo", "Thinkpad", "16GB", "2TB")
    print(computadora2)
    # Verificamos a que instancia pertenece el objeto computadora2
    verificarInstancia(computadora2)


    #Crear dos intancias de la clase ConsolaVideoJuego
    #Instancia 1 de la clase ConsolaVideoJuego
    print("Primera instancia de la clase ConsolaVideoJuego")
    consola1 = ConsolaVideoJuego("XB-1938", "Windows 10 ONECORE", "Xbox One", "2TB", "10-11-2020")
    print(consola1)

    #verificamos a que instancia pertenece el objeto consola1
    verificarInstancia(consola1)

    # Aplicamos los métodos de la clase ConsolaVideoJuego
    consola1.actualizarSistemaOperativo()
    consola1.actualizarJuego("Gears 5")

    #Instancia 2 de la clase ConsolaVideoJuego
    print("Segunda instancia de la clase ConsolaVideoJuego")
    consola2 = ConsolaVideoJuego("PS-1938", "Orbis OS FreeBSD", "Playstation 4", "2TB", "15-11-2013")
    print(consola2)
    # Verificamos a que instancia pertenece el objeto
    verificarInstancia(consola2)

#Entry point
if __name__ == "__main__":
    main()

