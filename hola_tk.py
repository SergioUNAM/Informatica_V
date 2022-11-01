import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.messagebox import showinfo
import random

# Creamos un clase telefono celular con sus atributos privados

class Celular:
    def __init__(self, marca, modelo, color, pantalla, bateria, camara):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pantalla = pantalla
        self.__bateria = bateria
        self.__camara = camara

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def get_pantalla(self):
        return self.__pantalla

    def get_bateria(self):
        return self.__bateria

    def get_camara(self):
        return self.__camara

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_color(self, color):
        self.__color = color

    def set_pantalla(self, pantalla):
        self.__pantalla = pantalla

    def set_bateria(self, bateria):
        self.__bateria = bateria

    def set_camara(self, camara):
        self.__camara = camara

# Creamos una clase para la aplicacion de la interfaz grafica

# class CelularApp:
#     celulares = []
#     def __init__(self):
#         self.ventana = tk.Tk()
#         self.ventana.geometry("400x400")
#         self.ventana.title("Celulares")
#         self.marca = tk.StringVar()
#         self.modelo = tk.StringVar()
#         self.color = tk.StringVar()
#         self.pantalla = tk.StringVar()
#         self.bateria = tk.StringVar()
#         self.camara = tk.StringVar()
#         self.marca.set("Samsung")
#         self.modelo.set("Galaxy S21")
        
#         self.marca_label = tk.Label(self.ventana, text="Marca: ")
#         self.marca_label.grid(column=0, row=0, padx=5, pady=5)
#         self.marca_entry = tk.Entry(self.ventana, textvariable=self.marca, width=20)
#         self.marca_entry.grid(column=1, row=0, padx=5, pady=5)
#         self.modelo_label = tk.Label(self.ventana, text="Modelo: ")
#         self.modelo_label.grid(column=0, row=1, padx=5, pady=5)
#         self.modelo_entry = tk.Entry(self.ventana, textvariable=self.modelo, width=20)
#         self.modelo_entry.grid(column=1, row=1, padx=5, pady=5)
#         self.color_label = tk.Label(self.ventana, text="Color: ")
#         self.color_label.grid(column=0, row=2, padx=5, pady=5)
#         self.color_entry = tk.Entry(self.ventana, textvariable=self.color, width=20)
#         self.color_entry.grid(column=1, row=2, padx=5, pady=5)
#         self.pantalla_label = tk.Label(self.ventana, text="Pantalla: ")
#         self.pantalla_label.grid(column=0, row=3, padx=5, pady=5)
#         self.pantalla_entry = tk.Entry(self.ventana, textvariable=self.pantalla, width=20)
#         self.pantalla_entry.grid(column=1, row=3, padx=5, pady=5)
#         self.bateria_label = tk.Label(self.ventana, text="Bateria: ")
#         self.bateria_label.grid(column=0, row=4, padx=5, pady=5)
#         self.bateria_entry = tk.Entry(self.ventana, textvariable=self.bateria, width=20)
#         self.bateria_entry.grid(column=1, row=4, padx=5, pady=5)
#         self.camara_label = tk.Label(self.ventana, text="Camara: ")
#         self.camara_label.grid(column=0, row=5, padx=5, pady=5)
#         self.camara_entry = tk.Entry(self.ventana, textvariable=self.camara, width=20)
#         self.camara_entry.grid(column=1, row=5, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Crear", command=self.crear)
#         self.boton.grid(column=0, row=6, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Mostrar", command=self.mostrar)
#         self.boton.grid(column=1, row=6, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Modificar", command=self.modificar)
#         self.boton.grid(column=0, row=7, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Eliminar", command=self.eliminar)
#         self.boton.grid(column=1, row=7, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Salir", command=self.salir)
#         self.boton.grid(column=0, row=8, padx=5, pady=5)
#         self.boton = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
#         self.boton.grid(column=1, row=8, padx=5, pady=5)
#         self.ventana.mainloop()

#     def crear(self):
#         marca = self.marca.get()
#         modelo = self.modelo.get()
#         color = self.color.get()
#         pantalla = self.pantalla.get()
#         bateria = self.bateria.get()
#         camara = self.camara.get()
#         celular = Celular(marca, modelo, color, pantalla, bateria, camara)
#         celulares.append(celular)
#         self.limpiar()

#     def mostrar(self):
#         for celular in celulares:
#             print(celular.get_marca())
#             print(celular.get_modelo())
#             print(celular.get_color())
#             print(celular.get_pantalla())
#             print(celular.get_bateria())
#             print(celular.get_camara())
        

#     def modificar(self):
#         marca = self.marca.get()
#         modelo = self.modelo.get()
#         color = self.color.get()
#         pantalla = self.pantalla.get()
#         bateria = self.bateria.get()
#         camara = self.camara.get()
#         for celular in celulares:
#             if celular.get_marca() == marca:
#                 celular.set_modelo(modelo)
#                 celular.set_color(color)
#                 celular.set_pantalla(pantalla)
#                 celular.set_bateria(bateria)
#                 celular.set_camara(camara)
#                 self.limpiar()
#                 break
            
#     def eliminar(self):
#         marca = self.marca.get()
#         for celular in celulares:
#             if celular.get_marca() == marca:
#                 celulares.remove(celular)
#                 self.limpiar()
#                 break

#     def limpiar(self):
#         self.marca.set("")
#         self.modelo.set("")
#         self.color.set("")
#         self.pantalla.set("")
#         self.bateria.set("")
#         self.camara.set("")

#     def salir(self):
#         self.ventana.destroy()

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        self.combo = ttk.Combobox(self,state="readonly", values=["1", "2", "3", "4"])
        self.combo.place(x=50, y=50)
        self.button = ttk.Button(text="Mostrar seleccion", command=self.show_selection)
        self.button.place(x=50, y=100)
        main_window.config(width=300, height=200)

    def show_selection(self):
        #Obtener la opción seleccionada
        selection = self.command.get()
        messagebox.showinfo(message=f"La opción seleccionada es {selection}", title="Selection")




# Método principal del programa
def main():
    main_window = tk.Tk()
    app = Application(main_window)
    app.mainloop()

# Entry point del programa
if __name__ == "__main__":
    main()
