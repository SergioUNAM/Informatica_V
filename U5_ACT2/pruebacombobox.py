import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# Configuramos la ventana root

root.geometry("300x200")
root.resizable(False, False)
root.title("Combobox prueba")

# label
label = ttk.Label(text="Seleccione un mes por favor:")
label.pack(fill=tk.X, padx=5, pady=5)

# Creamos el combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# Obtenemos las 3 primeras letras de cada mes
month_cb["values"] = [month_name[m][0:3] for m in range(1, 13)]

# Prevent typing a value
month_cb["state"] = "readonly"

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """handle the month changed event"""
    showinfo(
        title="Result",
        message=f"You selected {selected_month.get()}!"
    )


month_cb.bind("<<ComboboxSelected>>", month_changed)

root.mainloop()
