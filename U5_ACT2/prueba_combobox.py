import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

app = tk.Tk()  # CREAMOS LA VENTANA

# Configuramos la ventana
app.geometry('600x400')
app.resizable(False, False)
app.title('PRUEBA COMBOBOX')

# label
label = ttk.Label(text="SELECCIONE UN MES DE LA LISTA:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
combobox = ttk.Combobox(app, textvariable=selected_month, state="readonly", values= ["adfdf", "dsjfiasf", "ofij8349fjvm"])


# Definimos la posicion del CB
combobox.pack(fill=tk.X, padx=50, pady=5)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )


combobox.bind('<<ComboboxSelected>>', month_changed)

app.mainloop()
