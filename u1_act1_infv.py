# Creación de la clase persona
class Persona:
    def __int__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def saludo(self.nombre):
        print(nombre)


# Instanciación de la clase persona, es decir, se crea un objeto de la clase Persona
if __name__ == "__main__":
    Persona1 = Persona
    Persona1.nombre = "Sergio"
    Persona1.apellido = "Castelar"
    Persona1.edad = 30
    Persona1.ciudad = "CDMX"

    print(Persona1.nombre)
    Persona.saludo()
