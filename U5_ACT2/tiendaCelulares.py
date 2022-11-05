import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Definimos una clase abstracta llamada VentaMovil con un metodo llamado revisarPromocion
class VentaMovil:
    def revisarPromocion(self):
        pass

# Creamos la clase Celular con los atributos marca, modelo, color, capacidad_alamacenamiento, precio
class Celular:
    def __init__(self, marca = None, modelo = None, color = None, capacidad_almacenamiento = None, precio = None, renta = None, seguro = None,):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__capacidad_almacenamiento = capacidad_almacenamiento
        self.__precio = precio
        self.__renta = renta
        self.__seguro = seguro
        
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def get_capacidad_almacenamiento(self):
        return self.__capacidad_almacenamiento

    def get_precio(self):
        return self.__precio
    
    def get_renta(self):
        return self.__renta
    
    def set_seguro(self, seguro):
        self.__seguro = seguro

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_color(self, color):
        self.__color = color

    def set_capacidad_almacenamiento(self, capacidad_almacenamiento):
        self.__capacidad_almacenamiento = capacidad_almacenamiento

    def set_precio(self, precio):
        self.__precio = precio
        
    def set_renta(self, renta):
        self.__renta = renta
    
    def set_seguro(self, seguro):
        self.__seguro = seguro

    # Creamos el método eleccion, en el cual se determinarán los atributos del celular
    def eleccion(self):
        self.set_marca(input("Ingrese la marca del celular: "))
        self.set_modelo(input("Ingrese el modelo del celular: "))
        self.set_color(input("Ingrese el color del celular: "))
        self.set_capacidad_almacenamiento(input("Ingrese la capacidad de almacenamiento del celular: "))
        self.set_precio(input("Ingrese el precio del celular: "))
        self.set_renta(input("Ingrese la renta del celular: "))
        self.set_seguro(input("Ingrese el seguro del celular: "))
    
    # Creamos el metodo mostrar eleccion, en el cual se mostrarán los atributos del celular
    def mostrar_eleccion(self):
        print("Marca: ", self.get_marca())
        print("Modelo: ", self.get_modelo())
        print("Color: ", self.get_color())
        print("Capacidad de almacenamiento: ", self.get_capacidad_almacenamiento())
        print("Precio: ", self.get_precio())


# Creamos la clase Cliente con los siguientes atributos privados nombre, apellido_paterno, apellido_materno, correo_electronico, telefono
class Cliente:
    def __init__(self, nombre = None, apellido_paterno = None, apellido_materno = None, correo_electronico = None, telefono = None):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__correo_electronico = correo_electronico
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_correo_electronico(self):
        return self.__correo_electronico

    def get_telefono(self):
        return self.__telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_correo_electronico(self, correo_electronico):
        self.__correo_electronico = correo_electronico

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido Paterno: {self.__apellido_paterno}, Apellido Materno: {self.__apellido_materno}, Correo Electronico: {self.__correo_electronico}, Telefono: {self.__telefono}"

 # definimos una funcion para desplegar distintos combobox en una interfaz grafica
def menu():
    marcas = ["Apple", "Samsung", "Xiaomi", "Huawei", "Motorola"]
    ventana = tk.Tk()
    ventana.title("Menu")
    ventana.geometry("400x400")
    ventana.configure(background = "light blue")
    ventana.resizable(0,0)

    label = ttk.Label(text = "Bienvenido a la tienda de celulares", background = "light blue")
    label.pack(fill=tk.X, expand=True)

    #Creamos el combobox
    combo = ttk.Combobox(ventana, values = marcas)
    combo.pack(fill=tk.X, expand=True)

    ventana.mainloop()


def main():
    # Creamos un objeto de la clase Celular
    celular = Celular()
    menu()

if __name__ == "__main__":
    main()