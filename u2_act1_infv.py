"""Crear una clase móvil que tenga los siguientes atributos “estados”: marca, modelo, color, precio, cámara, procesador, huella digital, tipo de sensores para cada uno de los atributos definir los métodos set y get.

Crear en la misma clase métodos “comportamiento” como: encender, apagar, usarSensor(TIPO_SENSOR), tomarFoto(), realizarLlama(num_telefono), bloquer(), desbloquer() y otros 3 métodos que tú consideres que necesita contener.

Crear tres constructores diferentes de móvil con base a algunos atributos definidos."""


class Movil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
