# Importación de librerías
import tkinter as tk
from tkinter import ttk


# Creamos la clase TelefonoCelular con los siguientes atrbutos privados: marca, modelo, color, capacidad de almacenamiento, precio, plan_renta, seguro, precio_total
class TelefonoCelular:

    def __init__(self, marca=None, modelo=None, color=None, capacidad_almacenamiento=None, precio=0, plan_renta=False,
                 seguro=False, precio_total=0):
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

    # Creamos un objeto de la clase TelefonoCelular
    # telefono = TelefonoCelular()
    # print(telefono)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Inicializamos los atributos de la clase TelefonoCelular
        self.telefono = TelefonoCelular()

        # Combos solicitados
        self.comboMarca = ttk.Combobox(self, values=["Apple", "Samsung", "Huawei", "Xiaomi", "Motorola"], state='readonly')
        self.comboModelo = ttk.Combobox(self, state='readonly')
        self.comboColor = ttk.Combobox(self, state='readonly')
        self.comboAlmacenamiento = ttk.Combobox(self, values=["32 gb", "64 gb", "128 gb"], state='readonly')
        self.comboMarca.grid(row=0, column=0)
        self.comboModelo.grid(row=1, column=0)
        self.comboColor.grid(row=2, column=0)
        self.comboAlmacenamiento.grid(row=3, column=0)
        self.comboMarca.bind("<<ComboboxSelected>>", self.comboModelo_update)
        self.comboModelo.bind("<<ComboboxSelected>>", self.comboColor_update)
        self.comboAlmacenamiento.bind("<<ComboboxSelected>>", self.precio_update)
        
        #Creamos un label vacio donde se mostrará el precio
        self.label_precio = tk.Label(self, text="")
        self.label_precio.grid(row=10, column=0)


        # Creamos un label para mostrar si se eligio el plan de renta
        self.label_plan_renta = tk.Label(self, text="")
        self.label_plan_renta.grid(row=11, column=0)

        # Creamos un label para mostrar si se eligio el seguro
        self.label_seguro = tk.Label(self, text="")
        self.label_seguro.grid(row=12, column=0)

    
        # Centramos los combobox    
        self.grid_columnconfigure(0, weight=1)

        # Check box solicitados
        # Checkbox si adquiere un plan de renta
        self.checkbox_plan_renta = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Desea adquirir un plan de renta",
                                        variable=self.checkbox_plan_renta,
                                        command=self.checkbox_clicked_plan_renta)
        self.checkbox.grid(row=7, column=0)
        self.place(width=300, height=200)

        # Checkbox si adquiere un seguro
        self.checkbox_seguro = tk.BooleanVar(self)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Desea adquirir un seguro",
                                        variable=self.checkbox_seguro,
                                        command=self.checkbox_clicked_seguro)
        self.checkbox.grid(row=8, column=0)
        self.place(width=300, height=200)

    def precio_update(self, event):
        # Modelos iphone ["iPhone 12", "iPhone 11", "iPhone X", "iPhone XR", "iPhone 8"]
        # Modelos Samsung [Galaxy S21", "Galaxy S20", "Galaxy S10", "Galaxy S9", "Galaxy S8"]
        # Modelos Huawei ["P40", "P30", "P20", "P10", "P9"]
        # Modelos Xiaomi ["Mi 10", "Mi 9", "Mi 8", "Mi 7", "Mi 6"]
        # Modelos Motorola ["Moto G9", "Moto G8", "Moto G7", "Moto G6", "Moto G5"]
        if (combo_sel := self.comboModelo.get()) == "iPhone 12":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 16499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 19, 499
        elif (combo_sel := self.comboModelo.get()) == "iPhone 11":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 10900
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 11900
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 12900
        elif (combo_sel := self.comboModelo.get()) == "iPhone X":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "iPhone XR":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 9499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 10499
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 11499
        elif (combo_sel := self.comboModelo.get()) == "iPhone 8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S21":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S20":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Galaxy S8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "P40":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "P30":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "P20":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "P10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "P9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Mi 10":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Mi 9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Mi 8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Mi 7":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Mi 6":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 7999
        elif (combo_sel := self.comboModelo.get()) == "Moto G9":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 14999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 15999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 16999
        elif (combo_sel := self.comboModelo.get()) == "Moto G8":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 12999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 13999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 14999
        elif (combo_sel := self.comboModelo.get()) == "Moto G7":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 9999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 10999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 11999
        elif (combo_sel := self.comboModelo.get()) == "Moto G6":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 7999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 8999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 9999
        elif (combo_sel := self.comboModelo.get()) == "Moto G5":
            if (combo_sel := self.comboAlmacenamiento.get()) == "32 gb":
                precio = 5999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "64 gb":
                precio = 6999
            elif (combo_sel := self.comboAlmacenamiento.get()) == "128 gb":
                precio = 7999
        
        self.telefono.marca = self.comboMarca.get()
        self.telefono.modelo = self.comboModelo.get()
        self.telefono.precio = precio
        self.telefono.capacidad_almacenamiento = self.comboAlmacenamiento.get()
        self.telefono.color = self.comboColor.get()

        

        # Mostramos el precio en la interfaz
        self.label_precio.config(text=f"\nElegiste un {self.telefono.marca} {self.telefono.modelo} de {self.telefono.capacidad_almacenamiento} con un precio de ${self.telefono.precio}")


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
            self.label_plan_renta.config(text=f"\nPlan de renta seleccionado\n El precio del equipo será dividido en 12 mensualidades. \nEl precio ${self.telefono.precio} mxn dividido entre 12 rentas da un total de {round(float(self.telefono.precio / 12), 2)} mxn \nAl terminar el plazo el equipo podra ser tuyo. \nConsulta términos y condiciones en la tienda.")
        else:
            self.telefono.plan_renta = False
            self.label_plan_renta.config(text="\nNo elegiste el plan de renta, el precio del equipo será el total")

    def checkbox_clicked_seguro(self):
        if self.checkbox_seguro.get():
            self.telefono.seguro = 750
            self.telefono.precio_total = self.telefono.precio + self.telefono.seguro
            self.label_seguro.config(text=f"\nElegiste el seguro con un costo adicional de $750.00 mxn. \nEl precio total del equipo + seguro es de ${self.telefono.precio} mxn + ${self.telefono.seguro} mxn = ${self.telefono.precio_total} mxn\nConsulta términos y condiciones")
        else:
            self.telefono.seguro = 0
            self.telefono.precio_total = self.telefono.precio + self.telefono.seguro
            self.label_seguro.config(text=f"\nElegiste no contratar el seguro, \ntoma en cuenta que en caso de robo o extravío u algún otro incidente \nno podrás reclamar el equipo.\nEl precio total del equipo + seguro es de ${self.telefono.precio} mxn + ${self.telefono.seguro} mxn = ${self.telefono.precio_total} mxn\nConsulta términos y condiciones")
        print(self.telefono)


# Método principal del programa
def main():
    root = tk.Tk()
    root.geometry("525x525")
    root.resizable(False, False)

    # Creamos un titulo con formato
    root.title("Unidad 5, Actividad 2")
    label = tk.Label(root, text="Tienda de Celulares FCA", font=("Arial", 30))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.pack(fill=tk.X, padx=5, pady=5)

    App(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()


# Entry point del programa
if __name__ == "__main__":
    main()
