# Clase ejemplo que utiliza constructores (__init__) y destructores (__del__)
class Archivo:
    def __init__(self, nombre):
        """
        Constructor: Se ejecuta al crear una nueva instancia de la clase.
        Inicializa el nombre del archivo y abre el archivo para escritura.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' creado y abierto para escritura.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        self.archivo.write(texto)
        print(f"Texto escrito en el archivo '{self.nombre}'.")

    def __del__(self):
        """
        Destructor: Se ejecuta al eliminar la instancia.
        Cierra el archivo abierto, asegurándose de liberar recursos.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase Archivo
    mi_archivo = Archivo("mi_archivo.txt")
    mi_archivo.escribir("Este es un ejemplo de uso de constructores y destructores en Python.\n")
    # La instancia será eliminada automáticamente al finalizar el programa, llamando al destructor.
