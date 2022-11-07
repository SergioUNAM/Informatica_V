import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from turtle import title


# Creamos la clase TelefonoCelular con los siguientes atrbutos privados: marca, modelo, color, capacidad de almacenamiento, precio, plan_renta, seguro, precio_total
class TelefonoCelular:

    def __init__(self, marca=None, modelo=None, color=None, capacidad_almacenamiento=None, precio=100, plan_renta=100,
                 seguro=100):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__capacidad_almacenamiento = capacidad_almacenamiento
        self.__precio = precio
        self.__plan_renta = plan_renta
        self.__seguro = seguro

    # GETTERS Y SETTERS

    # marca
    @property  # getter atributo marca
    def marca(self):
        return self.__marca

    @marca.setter  # setter atributo marca
    def marca(self, value):
        self.__marca = value

    # modelo
    @property  # getter atributo modelo
    def modelo(self):
        return self.__modelo

    @modelo.setter  # setter atributo modelo
    def modelo(self, value):
        self.__modelo = value

    # color
    @property  # getter atributo color
    def color(self):
        return self.__color

    @color.setter  # setter atributo color
    def color(self, value):
        self.__color = value

    # capacidad_almacenamiento
    @property  # getter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self):
        return self.__capacidad_almacenamiento

    @capacidad_almacenamiento.setter  # setter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self, value):
        self.__capacidad_almacenamiento = value

    # precio
    @property  # getter atributo precio
    def precio(self):
        return self.__precio

    @precio.setter  # setter atributo precio
    def precio(self, value):
        self.__precio = value

    # plan_renta
    @property  # getter atributo plan_renta
    def plan_renta(self):
        return self.__plan_renta

    @plan_renta.setter  # setter atributo plan_renta
    def plan_renta(self, value):
        self.__plan_renta = value

    # seguro
    @property  # getter atributo seguro
    def seguro(self):
        return self.__seguro

    @seguro.setter  # setter atributo seguro
    def seguro(self, value):
        self.__seguro = value

    # precio_total
    @property  # getter atributo precio_total
    def precio_total(self):
        return self.__precio_total

    @precio_total.setter  # setter atributo precio_total
    def precio_total(self, value):
        self.__precio_total = value

    # Definimos el método __str__ para imprimir los atributos de la clase TelefonoCelular
    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}, Capacidad de almacenamiento: {self.__capacidad_almacenamiento}, Precio: {self.__precio}, Plan de renta: {self.__plan_renta}, Seguro: {self.__seguro}, Precio total: {self.__precio_total}"


# Creamos la función Interfaz1
def Interfaz1(telefono):
    # Creamos la ventana
    def ventana():
        ventana = tk.Tk()
        ventana.geometry('500x500')
        ventana.resizable(False, False)
        ventana.title('Tienda de Celulares')

        # Creamos un titulo con formato atractivo
        etiqueta = tk.Label(ventana, text='Tienda de Celulares', font=('Arial', 20, 'bold'))
        etiqueta.pack(fill=tk.X, padx=5, pady=5)

        

        # Ejecutamos los combos solicitados
        comboMarca(ventana)
        comboModelo(ventana)


        # Creamos un boton para cerrar la ventana
        boton = tk.Button(ventana, text='Cerrar', command=ventana.destroy)
        boton.pack(fill=tk.X, padx=5, pady=5)

        ventana.mainloop()

    # Combobox Marca
    def comboMarca(ventana):
        # Creamos una lista con 5 marcas de teléfonos celulares
        lista_marcas = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Motorola']

        # Creamos la función que asignara el valor de la marca al objeto telefono
        def seleccionMarca(event):
            telefono.marca = comboMarca.get()
            
        # combobox marca
        comboMarca = ttk.Combobox(ventana, values=lista_marcas, state='readonly')
        comboMarca.pack(fill=tk.X, padx=5, pady=5)
        comboMarca.bind('<<ComboboxSelected>>', seleccionMarca, telefono)

    def comboModelo(ventana):
        # Creamos una lista con 5 modelos de teléfonos celulares segun la marca seleccionada
        if telefono.marca == 'Apple':
            lista_modelos = ['iPhone 12', 'iPhone 11', 'iPhone X', 'iPhone 8', 'iPhone 7']

        # Creamos la función que asignara el valor del modelo al objeto telefono
        def seleccionModelo(event):
            telefono.modelo = comboModelo.get()
            
        # combobox modelo
        comboModelo = ttk.Combobox(ventana, values=lista_modelos, state='readonly')
        comboModelo.pack(fill=tk.X, padx=5, pady=5)
        comboModelo.bind('<<ComboboxSelected>>', seleccionModelo, telefono)
    
    

    # Ejecutamos la función ventana
    ventana()


# Método principal del programa
def main():
    # Creamos un objeto de la clase TelefonoCelular
    telefono = TelefonoCelular()

    Interfaz1(telefono)

    print("marca", telefono.marca)
    print("modelo", telefono.modelo)


# Entry point del programa
if __name__ == "__main__":
    main()
