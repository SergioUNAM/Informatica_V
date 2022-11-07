import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from turtle import title

# Creamos la clase TelefonoCelular con los siguientes atrbutos privados: marca, modelo, color, capacidad de almacenamiento, precio, plan_renta, seguro, precio_total
class TelefonoCelular:
    
    def __init__(self, marca=None , modelo= None, color= None, capacidad_almacenamiento= None, precio= 100, plan_renta= 100, seguro= 100):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__capacidad_almacenamiento = capacidad_almacenamiento
        self.__precio = precio
        self.__plan_renta = plan_renta
        self.__seguro = seguro

   # GETTERS Y SETTERS

   # marca
    @property # getter atributo marca
    def marca(self):
        return self.__marca

    @marca.setter # setter atributo marca
    def marca(self, value):
        self.__marca = value

    # modelo
    @property # getter atributo modelo
    def modelo(self):
        return self.__modelo

    @modelo.setter # setter atributo modelo
    def modelo(self, value):
        self.__modelo = value

    # color
    @property # getter atributo color
    def color(self):
        return self.__color

    @color.setter # setter atributo color
    def color(self, value):
        self.__color = value

    # capacidad_almacenamiento
    @property # getter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self):
        return self.__capacidad_almacenamiento

    @capacidad_almacenamiento.setter # setter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self, value):
        self.__capacidad_almacenamiento = value

    # precio
    @property # getter atributo precio
    def precio(self):
        return self.__precio

    @precio.setter # setter atributo precio
    def precio(self, value):
        self.__precio = value

    # plan_renta
    @property # getter atributo plan_renta
    def plan_renta(self):
        return self.__plan_renta

    @plan_renta.setter # setter atributo plan_renta
    def plan_renta(self, value):
        self.__plan_renta = value
    
    # seguro
    @property # getter atributo seguro
    def seguro(self):
        return self.__seguro

    @seguro.setter # setter atributo seguro
    def seguro(self, value):
        self.__seguro = value

    # precio_total
    @property # getter atributo precio_total
    def precio_total(self):
        return self.__precio_total

    @precio_total.setter # setter atributo precio_total
    def precio_total(self, value):
        self.__precio_total = value

    # Definimos el método __str__ para imprimir los atributos de la clase TelefonoCelular
    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}, Capacidad de almacenamiento: {self.__capacidad_almacenamiento}, Precio: {self.__precio}, Plan de renta: {self.__plan_renta}, Seguro: {self.__seguro}, Precio total: {self.__precio_total}"

# Creamos la función Interfaz1
def Interfaz1(telefono, lista_marcas):
    # Creamos la ventana
    def ventana():
        ventana = tk.Tk()
        ventana.geometry('500x500')
        ventana.resizable(False, False)
        ventana.title('Tienda de Celulares')
    
        # Creamos un titulo con formato atractivo
        etiqueta = tk.Label(ventana, text = 'Tienda de Celulares', font = ('Arial', 20, 'bold'))
        etiqueta.pack(fill=tk.X, padx=5, pady=5)
    

        # Invocamos a la función comboMarca
        comboMarca(ventana, lista_marcas)

        # Creamos un boton para cerrar la ventana
        boton = tk.Button(ventana, text = 'Cerrar', command = ventana.destroy)
        boton.pack(fill=tk.X, padx=5, pady=5)

        ventana.mainloop()
        
    # Combobox Marca
    def comboMarca(ventana, lista_marcas):
        # Creamos la función que asignara el valor de la marca al objeto telefono
        def seleccionMarca(event):
            seleccion = comboMarca.get()
            telefono.marca = seleccion
        
        # combobox marca
        comboMarca = ttk.Combobox(ventana, values = lista_marcas, state = 'readonly')
        comboMarca.pack(fill=tk.X, padx=5, pady=5)
        comboMarca.bind('<<ComboboxSelected>>', seleccionMarca, telefono)

    

    # Ejecutamos la función ventana
    ventana()
    
    
# Método principal del programa
def main():
    marcas = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'LG']

    # Creamos un objeto de la clase TelefonoCelular
    telefono = TelefonoCelular()

    Interfaz1(telefono, marcas)

    
    # Creamos una lista de 5 modelos por cada una de las marcas para pasarlaas como parametro a la función interfaz1
    if telefono.marca == 'Apple':
        modelos = ["Iphone X", "Iphone 11", "Iphone 12", "Iphone 12 mini", "Iphone 13"]
    elif telefono.marca == 'Samsung':
        modelos = ["Galaxy S21", "Galaxy S21+", "Galaxy S21 Ultra", "Galaxy S20", "Galaxy S20+"]
    elif telefono.marca == 'Huawei':
        modelos = ["P40", "P40 Pro", "P40 Pro+", "P30", "P30 Pro"]
    elif telefono.marca == 'Xiaomi':
        modelos = ["Mi 10", "Mi 10 Pro", "Mi 10T", "Mi 10T Pro", "Mi 11"]
    elif telefono.marca == 'LG':
        modelos = ["G8X ThinQ", "V60 ThinQ", "K92", "K52", "K42"]

    
    print(telefono.marca)

# Entry point del programa
if __name__ == "__main__":
    main()