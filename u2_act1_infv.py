# Sergio Alberto Castelar Fernandez
# Informatica V
# Semestre 2023-1
# Unidad 2
# Actividad 1

"""Crear una clase móvil que tenga los siguientes atributos “estados”: marca, modelo, color, precio, cámara, procesador, huella digital, tipo de sensores para cada uno de los atributos definir los métodos set y get.

Crear en la misma clase métodos “comportamiento” como: encender, apagar, usarSensor(TIPO_SENSOR), tomarFoto(), realizarLlama(num_telefono), bloquer(), desbloquer() y otros 3 métodos que tú consideres que necesita contener.

Crear tres constructores diferentes de móvil con base a algunos atributos definidos."""


class Movil:
    def __init__(self, marca, modelo, color, precio, camara, procesador, huella_digital, tipo_sensores):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self. precio = precio
        self.camara = camara
        self.procesador = procesador
        self.huella_digital = huella_digital
        self.tipo_sensores = tipo_sensores
