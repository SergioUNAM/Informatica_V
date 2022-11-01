from tkinter import ttk
import tkinter as tk

# Definimos a la clase Celular con los siguientes parametros: marca, modelo, precio, color, almacenamiento, compraSeguro, renta, compra
class Celular:
    marcas = ["Apple", "Samsung", "Xiaomi", "Motorola", "Huawei"]

# Definimos a la clase Compra donde se seleecionaran los celulares que se desean comprar a traves de un metodo para cada marca de celulares, se mostrara el total a pagar y se le preguntara al usuario si desea realizar la compra, habra 5 marcas, 3 modelos por marca, 5 colores a elegir, 3 capacidades de almacenamiento, seguro de compra, y si renta o compra el celular

class Compra:
    def __init__(self, num_compra):
        self.num_compra = num_compra
        
    #definimos el metodo ventanan donde se implementará la estructura de la interfaz grafica
    def ventana(self):
        self.ventana = tk.Tk()
        self.ventana.config(width = 300, height = 300)
        self.ventana.title("Compra de Celulares")
        self.combo = ttk.Combobox(self.ventana, values = Celular.marcas)
        self.combo.place(x = 100, y = 100)
        self.combo.bind("<<ComboboxSelected>>", self.seleccionar_marca)
        self.ventana.mainloop()
        

    def apple(self):
        modelos_disponible = ["Iphone 11", "Iphone 12", "Iphone 13"]
        # Damos a elegir una opción al usuario de los modelos disponibles
        print("Modelos disponibles: ", modelos_disponible)
        modelo = input("Elija un modelo: ")
        # Si el modelo elegido no esta en la lista de modelos disponibles, se le pedira que elija uno de los modelos disponibles
        while modelo not in modelos_disponible:
            print("Elija un modelo de los modelos disponibles")
            modelo = input("Elija un modelo: ")
        # Damos a elegir una opción al usuario de los colores disponibles
        colores_disponibles = ["blanco", "gris espacial", "plata", "verde medianoche", "rojo"]
        print("Colores disponibles: ", colores_disponibles)
        color = input("Elija un color: ")
        # Si el color elegido no esta en la lista de colores disponibles, se le pedira que elija uno de los colores disponibles
        while color not in colores_disponibles:
            print("Elija un color de los colores disponibles")
            color = input("Elija un color: ")
        # Damos a elegir una opción al usuario de las capacidades de almacenamiento disponibles
        almacenamiento_disponible = ["32GB", "64GB", "128GB"]
        print("Capacidades de almacenamiento disponibles: ", almacenamiento_disponible)
        almacenamiento = input("Elija una capacidad de almacenamiento: ")
        # Si la capacidad de almacenamiento elegida no esta en la lista de capacidades de almacenamiento disponibles, se le pedira que elija una de las capacidades de almacenamiento disponibles
        while almacenamiento not in almacenamiento_disponible:
            print("Elija una capacidad de almacenamiento de las capacidades de almacenamiento disponibles")
            almacenamiento = input("Elija una capacidad de almacenamiento: ")
        # Damos a elegir una opción al usuario de si desea o no el seguro de compra
        seguro_disponible = ["si", "no"]
        print("Seguro de compra disponible: ", seguro_disponible)
        seguro = input("Desea el seguro de compra: ")
        # Si la respuesta no es si o no, se le pedira que elija una de las opciones disponibles
        while seguro not in seguro_disponible:
            print("Elija una de las opciones disponibles")
            seguro = input("Desea el seguro de compra: ")
        # Damos a elegir una opción al usuario de si desea o no rentar el celular
        renta_disponible = ["si", "no"]
        print("Renta disponible: ", renta_disponible)
        renta = input("Desea rentar el celular: ")
        # Si la respuesta no es si o no, se le pedira que elija una de las opciones disponibles
        while renta not in renta_disponible:
            print("Elija una de las opciones disponibles")
            renta = input("Desea rentar el celular: ")
        # Si el usuario desea rentar el celular, se le pedira que elija una de las opciones disponibles
        if renta == "si":
            renta_disponible = ["1 mes", "3 meses", "6 meses", "12 meses"]
            print("Renta disponible: ", renta_disponible)
            renta = input("Elija una opcion: ")
            # Si la respuesta no es si o no, se le pedira que elija una de las opciones disponibles
            while renta not in renta_disponible:
                print("Elija una de las opciones disponibles")
                renta = input("Elija una opcion: ")
        # Si el usuario desea comprar el celular, se le pedira que elija una de las opciones disponibles
        if renta == "no":
            compra_disponible = ["1 mes", "3 meses", "6 meses", "12 meses"]
            print("Compra disponible: ", compra_disponible)
            compra = input("Elija una opcion: ")
            # Si la respuesta no es si o no, se le pedira que elija una de las opciones disponibles
            while compra not in compra_disponible:
                print("Elija una de las opciones disponibles")
                compra = input("Elija una opcion: ")
        # Se le mostrara al usuario el total a pagar
        print("El total a pagar es de: $", 1000)
        # Se le preguntara al usuario si desea realizar la compra
        compra_disponible = ["si", "no"]
        print("Compra disponible: ", compra_disponible)
        compra = input("Desea realizar la compra: ")
        # Si la respuesta no es si o no, se le pedira que elija una de las opciones disponibles
        while compra not in compra_disponible:
            print("Elija una de las opciones disponibles")
            compra = input("Desea realizar la compra: ")
        # Si el usuario desea realizar la compra, se le mostrara un mensaje de compra exitosa
        if compra == "si":
            print("Compra exitosa")
        # Si el usuario no desea realizar la compra, se le mostrara un mensaje de compra cancelada
        if compra == "no":
            print("Compra cancelada")

    # Clase Ventan para implementar la interfaz grafica

    

    # Creamos el método en el que se implementará un interfaz gráfica para el usuario
    #def apple_grafico():
        





# class Compra:
#     almacenamiento = ["32GB", "64GB", "128GB"]
#     def __init__(self, inventario = {"Apple":[
#                 {"Iphone 11":
#                     [{"color":
#                         ["blanco", "gris espacial", "plata", "verde medianoche", "rojo"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"Iphone 12": [{"color":
#                         ["blanco", "negro", "verde", "azul", "rojo"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"Iphone 13": [{"color":
#                         ["blanco estelar", "rosa", "verde olivo", "azul medianoche", "rojo"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]}],
#             "Samsung":[
#                 {"S20":
#                     [{"color":
#                         ["blanco", "gris", "azul", "rojo", "verde"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"S21": [{"color":
#                         ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"A51": [{"color":
#                         ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]}],
#             "Huawei":[
#                 {"P40":
#                     [{"color":
#                         ["blanco", "naranja", "azul", "rojo", "verde"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"P50": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"P60": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]}],
#             "Xiaomi":[
#                 {"Redmi Note 9":
#                     [{"color":
#                         ["blanco", "gris", "azul", "rojo", "verde"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"Redmi Note 10": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"Redmi Note 11": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]}],
#             "Motorola":[
#                 {"G10":
#                     [{"color":
#                         ["blanco", "gris", "azul", "rojo", "verde"]}, 
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"G20": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]},
#                 {"G30": [{"color":
#                     ["blanco", "gris", "azul", "rojo", "verde"]},
#                     {"almacenamiento": 
#                         almacenamiento}]}]}, seguro = None, renta = None, compra = None):
        
#         self.inventario = inventario
#         self.seguro = seguro
#         self.renta = renta
#         self.compra = compra



#Entry point
def main():
    compra = Compra("e")
    compra.apple()

if __name__ == "__main__":
    main()