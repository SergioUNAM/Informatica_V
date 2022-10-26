almacenamiento = ["32GB", "64GB", "128GB"]

diccionario_prueba = {"Apple":[
                {"Iphone 11":
                    [{"color":
                        ["blanco", "gris espacial", "plata", "verde medianoche", "rojo"]}, 
                    {"almacenamiento": 
                        almacenamiento}]},
                {"Iphone 12": [{"color":
                        ["blanco", "negro", "verde", "azul", "rojo"]}, 
                    {"almacenamiento": 
                        almacenamiento}]},
                {"Iphone 13": [{"color":
                        ["blanco estelar", "rosa", "verde olivo", "azul medianoche", "rojo"]}, 
                    {"almacenamiento": 
                        almacenamiento}]}]}

i = 1

# Imprimimos los elementos del diccionario
for marca in diccionario_prueba:
    print("Marca", type(marca), marca)
    for diccionario_modelo in diccionario_prueba[marca]:
        for modelo in diccionario_modelo:
            print("Modelo", type(modelo), modelo)
            for diccionario_color in diccionario_modelo[modelo]:
                for color in diccionario_color:
                    print("Color", type(color), color)
                for almacenamiento in diccionario_color["almacenamiento"]:
                    print("Almacenamiento", type(almacenamiento), almacenamiento)    