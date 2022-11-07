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
    def __init__(self,parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.combo = ttk.Combobox(self, values=["Samsung", "Apple", "Huawei", "Xiaomi", "Motorola"])
        self.combo2 = ttk.Combobox(self)
        self.combo.grid(row=0, column=0)
        self.combo2.grid(row=1, column=0)
        self.combo.bind("<<ComboboxSelected>>", self.combo2_update)

    def combo2_update(self, event):
        now = self.combo2.get()
        if (combo_sel:=self.combo.get()) == "Samsung":
                values=["Galaxy S21", "Galaxy S21+", "Galaxy S21 Ultra"]
        elif combo_sel == "Apple":
                values=["iPhone 12", "iPhone 12 Pro", "iPhone 12 Pro Max"]
        else:
            values = ()
        
        if now not in values:
            self.combo2.set("")
            self.combo2.config(values=values)
            

# Método principal del programa
def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(False, False)
    #Creamos un titulo con formato
    root.title("Tienda de celulares")
    
    
    App(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()

    # Creamos un objeto de la clase TelefonoCelular
    telefono = TelefonoCelular()

    #Interfaz1(telefono)

    print("marca", telefono.marca)
    print("modelo", telefono.modelo)


# Entry point del programa
if __name__ == "__main__":
    main()
