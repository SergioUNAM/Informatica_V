import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def show_selection():
    # Obtenemos la opción seleccionada en el combobox
    seleccion = combo.get()
    showinfo(message=f'La opción seleccionada es {seleccion}', title="Selección")


marca = ['1', '2', '3']

ventana = tk.Tk()
ventana.geometry('300x300')
ventana.resizable(False, False)
ventana.title('Combobox')

label = tk.Label(text="Seleccione: ")
label.pack(fill=tk.X, padx=5, pady=5)

# Creamos el combobox
combo = ttk.Combobox(state='readonly', values=marca)
combo.place(x=50, y=50)

ventana.mainloop()

combo.bind('<<ComboboxSelected>>', show_selection)