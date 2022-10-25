# Definimos a la clase Celular con los siguientes parametros: marca, modelo, precio, color, almacenamiento, compraSeguro, renta, compra
class Celular:
    def __init__(self, marca : str, modelo : str, precio : float, color : str, almacenamiento : str, compraSeguro : bool, renta : bool, compra : bool):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.almacenamiento = almacenamiento
        self.compraSeguro = compraSeguro
        self.renta = renta
        self.compra = compra

# Definimos a la clase Compra donde se seleecionaran los celulares que se desean comprar, se mostrara el total a pagar y se le preguntara al usuario si desea realizar la compra, habra 5 marcas, 3 modelos por marca, 5 colores a elegir, 3 capacidades de almacenamiento, seguro de compra, y si renta o compra el celular

class Compra:
    def __init__(self, inventario = {"Apple":[
                {"Iphone 11":
                    [{"color":
                        ["blanco", "gris espacial", "plata", "verde medianoche", "rojo"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"Iphone 12": [{"color":
                        ["blanco", "negro", "verde", "azul", "rojo"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"Iphone 13": [{"color":
                        ["blanco estelar", "rosa", "verde olivo", "azul medianoche", "rojo"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]}],
            "Samsung":[
                {"S20":
                    [{"color":
                        ["blanco", "gris", "azul", "rojo", "verde"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"S21": [{"color":
                        ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"A51": [{"color":
                        ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]}],
            "Huawei":[
                {"P40":
                    [{"color":
                        ["blanco", "naranja", "azul", "rojo", "verde"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"P50": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"P60": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]}],
            "Xiaomi":[
                {"Redmi Note 9":
                    [{"color":
                        ["blanco", "gris", "azul", "rojo", "verde"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"Redmi Note 10": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"Redmi Note 11": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]}],
            "Motorola":[
                {"G10":
                    [{"color":
                        ["blanco", "gris", "azul", "rojo", "verde"]}, 
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"G20": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]},
                {"G30": [{"color":
                    ["blanco", "gris", "azul", "rojo", "verde"]},
                    {"almacenamiento": 
                        ["32 GB", "64 GB", "128 GB"]}]}]}, seguro = None, renta = None, compra = None):
        self.inventario = inventario
        self.seguro = seguro
        self.renta = renta
        self.compra = compra

    # Método para mostrar el inventario de celulares
    def mostrarInventario(self):
        print("Inventario de celulares")
        print("Marca\t\tModelo\t\tColor\t\tAlmacenamiento\t\tPrecio")
        for marca in self.inventario:
            for modelo in self.inventario[marca]:
                for color in modelo[modelo[0]["color"][0]]:
                    for almacenamiento in color[color[0]["almacenamiento"][0]]:
                        print(f"{marca}\t\t{modelo}\t\t{color}\t\t{almacenamiento}\t\t${self.inventario[marca][modelo][color][almacenamiento]}")

#Entry point
def main():
    #Creamos un objeto de la clase Compra
    compra = Compra()
    #Mostramos el inventario de celulares
    compra.mostrarInventario()

if __name__ == "__main__":
    main()