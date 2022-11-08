import tkinter as tk
from tkinter import ttk


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


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Combos solicitados
        self.comboMarca = ttk.Combobox(self, values=["Apple", "Samsung", "Huawei", "Xiaomi", "Motorola"])
        self.comboModelo = ttk.Combobox(self)
        self.comboColor = ttk.Combobox(self)
        self.comboAlmacenamiento = ttk.Combobox(self, values=["32 gb", "64 gb", "128 gb"])
        self.comboMarca.grid(row=0, column=0)
        self.comboModelo.grid(row=1, column=0)
        self.comboColor.grid(row=2, column=0)
        self.comboAlmacenamiento.grid(row=3, column=0)
        self.comboMarca.bind("<<ComboboxSelected>>", self.comboModelo_update)
        self.comboModelo.bind("<<ComboboxSelected>>", self.comboColor_update)

        # Centramos los combobox    
        self.grid_columnconfigure(0, weight=1)

        # Check box solicitados
        # Checkbox si adquiere un plan de renta
        self.checkbox_value = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Opción",
                                        variable=self.checkbox_value,
                                        command=self.checkbox_clicked)
        self.checkbox.grid(row=4, column=0)

        self.place(width=300, height=200)

    def checkbox_clicked(self):
        print(self.checkbox_value.get())

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


# Método principal del programa
def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(False, False)

    # Creamos un titulo con formato
    root.title("Unidad 5, Actividad 2")
    label = tk.Label(root, text="Tienda de Celulares FCA", font=("Arial", 30))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.pack(fill=tk.X, padx=5, pady=5)

    App(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()

    # Creamos un objeto de la clase TelefonoCelular
    telefono = TelefonoCelular()


# Entry point del programa
if __name__ == "__main__":
    main()
