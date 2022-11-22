# Importación de librerías
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *


# Creamos una clase abstracta llamada VentaMovil con un método llamado revisarPromocion
class VentaMovil:
    def revisarPromocion(self, precio_venta):
        if precio_venta > 10000:
            return True

# Creamos la clase Cliente con los siguientes atributos privados nombre, apellido paterno y apellido materno, correo electrónico y teléfono.
class Cliente:
    def __init__(self, nombre=None, apellidoPaterno=None, apellidoMaterno=None, correoElectronico=None, telefono=None):
        self.__nombre = nombre
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__correoElectronico = correoElectronico
        self.__telefono = telefono

    # GETTERS Y SETTERS

    # nombre
    @property  # getter atributo nombre
    def nombre(self):
        return self.__nombre

    @nombre.setter  # setter atributo nombre
    def nombre(self, nombre):
        self.__nombre = nombre

    # apellidoPaterno
    @property  # getter atributo apellidoPaterno
    def apellidoPaterno(self):
        return self.__apellidoPaterno

    @apellidoPaterno.setter  # setter atributo apellidoPaterno
    def apellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno

    # apellidoMaterno
    @property  # getter atributo apellidoMaterno
    def apellidoMaterno(self):
        return self.__apellidoMaterno

    @apellidoMaterno.setter  # setter atributo apellidoMaterno
    def apellidoMaterno(self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno

    # correoElectronico
    @property  # getter atributo correoElectronico
    def correoElectronico(self):
        return self.__correoElectronico

    @correoElectronico.setter  # setter atributo correoElectronico
    def correoElectronico(self, correoElectronico):
        self.__correoElectronico = correoElectronico

    # telefono
    @property  # getter atributo telefono
    def telefono(self):
        return self.__telefono

    @telefono.setter  # setter atributo telefono
    def telefono(self, telefono):
        self.__telefono = telefono


# Creamos la clase TelefonoCelular con los siguientes atrbutos privados: marca, modelo, color, capacidad de almacenamiento, precio, plan_renta, seguro, precio_total
class TelefonoCelular:

    def __init__(self, marca=None, modelo=None, color=None, capacidad_almacenamiento=None, precio=0, plan_renta=False,
                 seguro=0, precio_total=0):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__capacidad_almacenamiento = capacidad_almacenamiento
        self.__precio = precio
        self.__plan_renta = plan_renta
        self.__seguro = seguro
        self.__precio_total = precio_total

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


# Clase App que despliega la primera interfaz solicitada
class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Inicializamos los atributos de la clase TelefonoCelular
        self.precio = None
        self.telefono = TelefonoCelular()

        # Combos solicitados
        # Marca
        self.label_marca = tk.Label(self, text="Marca")
        self.label_marca.grid(row=0, column=0, padx=5, pady=5)
        self.comboMarca = ttk.Combobox(self, values=["Apple", "Samsung", "Huawei", "Xiaomi", "Motorola"],
                                       state='readonly')
        self.comboMarca.grid(row=1, column=0)

        # Modelo
        self.label_modelo = tk.Label(self, text="Modelo")
        self.label_modelo.grid(row=2, column=0, padx=5, pady=5)
        self.comboModelo = ttk.Combobox(self, state='readonly')
        self.comboModelo.grid(row=3, column=0)

        # Color
        self.label_color = tk.Label(self, text="Color")
        self.label_color.grid(row=4, column=0, padx=5, pady=5)
        self.comboColor = ttk.Combobox(self, state='readonly')
        self.comboColor.grid(row=5, column=0)

        # Capacidad de almacenamiento
        self.label_capacidad_almacenamiento = tk.Label(self, text="Capacidad de almacenamiento")
        self.label_capacidad_almacenamiento.grid(row=6, column=0, padx=5, pady=5)
        self.comboAlmacenamiento = ttk.Combobox(self, values=["32 gb", "64 gb", "128 gb"], state='readonly')
        self.comboAlmacenamiento.grid(row=7, column=0)

        # Manejo de eventos
        self.comboMarca.bind("<<ComboboxSelected>>", self.comboModelo_update)
        self.comboModelo.bind("<<ComboboxSelected>>", self.comboColor_update)
        self.comboAlmacenamiento.bind("<<ComboboxSelected>>", self.precio_update)

        # Agregamos un espacio
        self.espacio = tk.Label(self, text="")
        self.espacio.grid(row=8, column=0, padx=5, pady=5)

        # Creamos un label vacio donde se mostrará el precio
        self.label_precio = tk.Label(self, text="")
        self.label_precio.grid(row=13, column=0)

        # Creamos un label para mostrar si se eligio el plan de renta
        self.label_plan_renta = tk.Label(self, text="")
        self.label_plan_renta.grid(row=14, column=0)

        # Creamos un label para mostrar si se eligio el seguro
        self.label_seguro = tk.Label(self, text="")
        self.label_seguro.grid(row=15, column=0)

        # Centramos los combobox    
        self.grid_columnconfigure(0, weight=1)

        # Checkbox solicitados
        # Checkbox si adquiere un plan de renta
        self.checkbox_plan_renta = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Desea adquirir un plan de renta",
                                        variable=self.checkbox_plan_renta,
                                        command=self.checkbox_clicked_plan_renta)
        self.checkbox.grid(row=10, column=0)
        self.place(width=300, height=200)

        # Checkbox si adquiere un seguro
        self.checkbox_seguro = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Desea adquirir un seguro",
                                        variable=self.checkbox_seguro,
                                        command=self.checkbox_clicked_seguro)
        self.checkbox.grid(row=11, column=0)
        self.place(width=300, height=200)

        # Creamos un boton para proceder a la compra
        self.boton_comprar = tk.Button(self, text="Comprar", command=self.comprar)
        self.boton_comprar.grid(row=16, column=0)

    # Metodo comprar donde se desplegara la segunda interfaz gráfica
    def comprar(self):

        root = tk.Tk()
        root.geometry("725x725")
        root.resizable(False, False)

        # Creamos un titulo con formato
        root.title("Unidad 5, Actividad 2")
        label = tk.Label(root, text="Tienda de Celulares FCA", font=("Arial", 25))
        label.grid(row=0, column=0, columnspan=2, pady=10)
        label.pack(fill=tk.X, padx=5, pady=5)

        Interfaz2(root, self.telefono.marca, self.telefono.modelo, self.telefono.color, self.telefono.capacidad_almacenamiento, self.telefono.precio, self.telefono.plan_renta, self.telefono.seguro, self.telefono.precio_total).pack(expand=True, fill=tk.BOTH)

        print("Total a pagar")

        root.mainloop()

    def precio_update(self, event):
        # Modelos iphone ["iPhone 12", "iPhone 11", "iPhone X", "iPhone XR", "iPhone 8"]
        # Modelos Samsung [Galaxy S21", "Galaxy S20", "Galaxy S10", "Galaxy S9", "Galaxy S8"]
        # Modelos Huawei ["P40", "P30", "P20", "P10", "P9"]
        # Modelos Xiaomi ["Mi 10", "Mi 9", "Mi 8", "Mi 7", "Mi 6"]
        # Modelos Motorola ["Moto G9", "Moto G8", "Moto G7", "Moto G6", "Moto G5"]
        if (combo_sel := self.comboModelo.get()) == "iPhone 12":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 16499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 19, 499
        elif (combo_sel := self.comboModelo.get()) == "iPhone 11":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 10900
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 11900
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 12900
        elif (combo_sel := self.comboModelo.get()) == "iPhone X":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "iPhone XR":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 9499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 10499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 11499
        elif (combo_sel := self.comboModelo.get()) == "iPhone 8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S21":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S20":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "P40":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "P30":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "P20":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "P10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "P9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Mi 10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Mi 9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Mi 8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Mi 7":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Mi 6":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Moto G9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Moto G8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Moto G7":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Moto G6":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Moto G5":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                self.precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                self.precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                self.precio = 7999

        self.telefono.marca = self.comboMarca.get()
        self.telefono.modelo = self.comboModelo.get()
        self.telefono.precio = self.precio
        self.telefono.capacidad_almacenamiento = self.comboAlmacenamiento.get()
        self.telefono.color = self.comboColor.get()

        # Mostramos el precio en la interfaz
        self.label_precio.config(
            text=f"\nElegiste un {self.telefono.marca} {self.telefono.modelo} de {self.telefono.capacidad_almacenamiento} con un precio de ${self.telefono.precio} mxn")

    def comboModelo_update(self, event):
        now = self.comboModelo.get()
        if (combo_sel := self.comboMarca.get()) == "Apple":
            values = ["iPhone 12", "iPhone 11", "iPhone X", "iPhone XR", "iPhone 8"]
        elif combo_sel == "Samsung":
            values = ["Galaxy S21", "Galaxy S20", "Galaxy S10", "Galaxy S9", "Galaxy S8"]
        elif combo_sel == "Huawei":
            values = ["P40", "P30", "P20", "P10", "P9"]
        elif combo_sel == "Xiaomi":
            values = ["Mi 10", "Mi 9", "Mi 8", "Mi 7", "Mi 6"]
        elif combo_sel == "Motorola":
            values = ["Moto G9", "Moto G8", "Moto G7", "Moto G6", "Moto G5"]
        else:
            values = ()

        if now not in values:
            self.comboModelo.set("")
            self.comboModelo.config(values=values)

    def comboColor_update(self, event):
        now = self.comboColor.get()
        if (combo_sel := self.comboMarca.get()) == "Apple":
            values = ["Gris espacial", "Dorado", "Rojo (PRODUCT RED)", "Plata", "Verde Noche"]
        elif combo_sel == "Samsung":
            values = ["Phantom black", "Phantom white", "Green", "Pink gold", "Graphite"]
        elif combo_sel == "Huawei":
            values = ["Blanco hielo", "Azul marino profundo", "Plata frost", "Blush gold", "Negro"]
        elif combo_sel == "Xiaomi":
            values = ["Carbon gray", "Ocean green", "Sunset purple", "Pearl white", "Pearl blue"]
        elif combo_sel == "Motorola":
            values = ["Negro", "Blanco", "Azul Opalo", "Verde Jade", "Dorado"]
        else:
            values = ()

        if now not in values:
            self.comboColor.set("")
            self.comboColor.config(values=values)

    def checkbox_clicked_plan_renta(self):
        if self.checkbox_plan_renta.get():
            self.telefono.plan_renta = True
            self.label_plan_renta.config(
                text=f"\nPlan de renta seleccionado\n El precio del equipo será dividido en 12 mensualidades. \nEl precio ${self.telefono.precio} mxn dividido entre 12 rentas da un total de {round(float(self.telefono.precio / 12), 2)} mxn \nAl terminar el plazo el equipo podra ser tuyo. \nConsulta términos y condiciones en la tienda.")
        else:
            self.telefono.plan_renta = False
            self.label_plan_renta.config(text="\nNo elegiste el plan de renta, el precio del equipo será el total")

    def checkbox_clicked_seguro(self):
        if self.checkbox_seguro.get():
            self.telefono.seguro = 750
            self.telefono.precio_total = self.telefono.precio + self.telefono.seguro
            self.label_seguro.config(
                text=f"\nElegiste el seguro con un costo adicional de $750.00 mxn. \nEl precio total del equipo + seguro es de ${self.telefono.precio} mxn + ${self.telefono.seguro} mxn = ${self.telefono.precio_total} mxn\nConsulta términos y condiciones")
        else:
            self.telefono.seguro = 0
            self.telefono.precio_total = self.telefono.precio + self.telefono.seguro
            self.label_seguro.config(
                text=f"\nElegiste no contratar el seguro, \ntoma en cuenta que en caso de robo o extravío u algún otro incidente \nno podrás reclamar el equipo.\nEl precio total del equipo + seguro es de ${self.telefono.precio} mxn + ${self.telefono.seguro} mxn = ${self.telefono.precio_total} mxn\nConsulta términos y condiciones")
        print(self.telefono)


# Clase Interfaz2 que genera la segunda ventana solicitada
class Interfaz2(tk.Frame, TelefonoCelular):

    # Creamos el constructor de la clase
    def __init__(self, parent, marca, modelo, color, capacidad_almacenamiento, precio, plan_renta, seguro, precio_total):
        #super().__init__(parent, marca, modelo, color, capacidad_almacenamiento, precio, plan_renta, seguro, precio_total)
        super().__init__(parent)
        self.telefono = TelefonoCelular(marca, modelo, color, capacidad_almacenamiento, precio, plan_renta, seguro, precio_total)


        # Inicializamos los atributos de la clase Cliente
        self.cliente = Cliente()

        # Creamos los widgets de la interfaz

        # Subtitulo
        self.subtitulo = tk.Label(self, text="Datos del cliente y facturación", font=("Arial", 20))
        self.subtitulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Nombre
        self.label_nombre = tk.Label(self, text="Nombre")
        self.label_nombre.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        # Apellido Paterno
        self.label_apellido_paterno = tk.Label(self, text="Apellido Paterno")
        self.label_apellido_paterno.grid(row=2, column=0, padx=5, pady=5)
        self.entry_apellido_paterno = tk.Entry(self)
        self.entry_apellido_paterno.grid(row=2, column=1, padx=5, pady=5)

        # Apellido Materno
        self.label_apellido_materno = tk.Label(self, text="Apellido Materno")
        self.label_apellido_materno.grid(row=3, column=0, padx=5, pady=5)
        self.entry_apellido_materno = tk.Entry(self)
        self.entry_apellido_materno.grid(row=3, column=1, padx=5, pady=5)

        # CorreoElectronico
        self.label_correo_electronico = tk.Label(self, text="Correo Electrónico")
        self.label_correo_electronico.grid(row=4, column=0, padx=5, pady=5)
        self.entry_correo_electronico = tk.Entry(self)
        self.entry_correo_electronico.grid(row=4, column=1, padx=5, pady=5)

        # Telefono
        self.label_telefono = tk.Label(self, text="Teléfono")
        self.label_telefono.grid(row=5, column=0, padx=5, pady=5)
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.grid(row=5, column=1, padx=5, pady=5)

        # Creamos los combobox de los datos bancarios

        # bancos
        self.label_banco = tk.Label(self, text="Banco")
        self.label_banco.grid(row=6, column=0, padx=5, pady=5)
        self.comboBanco = ttk.Combobox(self, state="readonly", values=["BBVA", "Banorte", "HSBC"])
        self.comboBanco.grid(row=6, column=1, padx=5, pady=5)

        # número de tarjeta con un ancho de 16 dígitos
        self.label_numero_tarjeta = tk.Label(self, text="Número de tarjeta")
        self.label_numero_tarjeta.grid(row=13, column=0, padx=5, pady=5)
        self.entry_numero_tarjeta = tk.Entry(self)
        self.entry_numero_tarjeta.grid(row=13, column=1, padx=5, pady=5)

        # Campo de texto digito verificador 
        self.label_digito_verificador = tk.Label(self, text="Digito verificador")
        self.label_digito_verificador.grid(row=15, column=0, padx=5, pady=5)
        self.entry_digito_verificador = tk.Entry(self)
        self.entry_digito_verificador.grid(row=15, column=1, padx=5, pady=5)
        
        # Combobox para el mes de vencimiento
        self.label_mes_vencimiento = tk.Label(self, text="Mes de vencimiento")
        self.label_mes_vencimiento.grid(row=16, column=0, padx=5, pady=5)
        self.comboMesVencimiento = ttk.Combobox(self, state="readonly", values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.comboMesVencimiento.grid(row=16, column=1, padx=5, pady=5)

        # Combobox para el año de vencimiento
        self.label_anio_vencimiento = tk.Label(self, text="Año de vencimiento")
        self.label_anio_vencimiento.grid(row=17, column=0, padx=5, pady=5)
        self.comboAnioVencimiento = ttk.Combobox(self, state="readonly", values=["2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"])
        self.comboAnioVencimiento.grid(row=17, column=1, padx=5, pady=5)

        # Combobox para emisor
        self.label_tipo_tarjeta = tk.Label(self, text="Emisor")
        self.label_tipo_tarjeta.grid(row=18, column=0, padx=5, pady=5)
        self.comboTipoTarjeta = ttk.Combobox(self, state="readonly", values=["Visa", "Mastercard", "American Express"])
        self.comboTipoTarjeta.grid(row=18, column=1, padx=5, pady=5)

        # Boton para mostrar los atributos del objeto telefono de la clase TelefonoCelular
        self.boton_mostrar = tk.Button(self, text="Realizar pago", command=self.pago)
        self.boton_mostrar.grid(row=19, column=0, columnspan=2, pady=10)

        # Centramos los widgets
        self.grid_columnconfigure(0, weight=3)

    def pago(self):
        # Creamos un objeto de la clase abstract VentaMovil
        self.venta_movil = VentaMovil()

        # se invoca al metodo revisar_pago de la clase abstracta VentaMovil se le pasa como parametro el attributo precio_total del objeto telefono de la clase Telefonocelular
        if self.venta_movil.revisarPromocion(self.telefono.precio_total):
            showinfo("Pago exitoso", "El pago se realizó correctamente")
        


        # asignamos los valores de los cuadros de texto a los atributos del objeto cliente de la clase Cliente
        self.cliente.nombre = self.entry_nombre.get()
        self.cliente.apellido_paterno = self.entry_apellido_paterno.get()
        self.cliente.apellido_materno = self.entry_apellido_materno.get()
        self.cliente.correo_electronico = self.entry_correo_electronico.get()
        self.cliente.telefono = self.entry_telefono.get()
        
        # Asignamos los valores bancarios a variables locales de la función mostrar
        banco = self.comboBanco.get()
        numero_tarjeta = self.entry_numero_tarjeta.get()
        digito_verificador = self.entry_digito_verificador.get()
        mes_vencimiento = self.comboMesVencimiento.get()
        anio_vencimiento = self.comboAnioVencimiento.get()
        tipo_tarjeta = self.comboTipoTarjeta.get()

        # creamos variable llamada tarjeta_socio que será generada aleatoriamente
        tarjeta_socio = str(random.randint(1000000000000000, 9999999999999999))

        # Mostramos en un cuador de dialogo mostrando todos los datos de compra
        showinfo("Datos de compra", "Nombre: " + self.cliente.nombre + " " + self.cliente.apellido_paterno + " " + self.cliente.apellido_materno )







# Método principal del programa
def main():
    root = tk.Tk()
    root.geometry("525x625")
    root.resizable(False, False)

    # Creamos un titulo con formato
    root.title("Unidad 5, Actividad 2")
    label = tk.Label(root, text="Tienda de Celulares FCA\nSeleccione su telefono:", font=("Arial", 25))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.pack(fill=tk.X, padx=5, pady=5)
    App(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()


# Entry point del programa
if __name__ == "__main__":
    main()
