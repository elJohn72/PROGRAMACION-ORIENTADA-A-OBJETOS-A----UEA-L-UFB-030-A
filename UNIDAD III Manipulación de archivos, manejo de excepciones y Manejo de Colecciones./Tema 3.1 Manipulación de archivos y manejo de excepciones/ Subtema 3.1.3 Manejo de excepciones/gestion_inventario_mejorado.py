import json
import os

class Inventario:
    """
    Clase para manejar un inventario de productos y almacenarlo en un archivo.
    Permite agregar, actualizar, eliminar y mostrar productos de forma persistente.
    """
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde un archivo JSON si existe, o crea un archivo vacío si no."""
        if not os.path.exists(self.archivo):
            print("Archivo no encontrado, creando un nuevo inventario.")
            self.guardar_inventario()
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.productos = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Error al leer el archivo, el inventario se inicializará vacío.")
            self.productos = {}

    def guardar_inventario(self):
        """Guarda el estado actual del inventario en un archivo JSON con manejo de excepciones."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4)
            print("Inventario guardado correctamente.")
        except OSError as e:
            print(f"Error al guardar el archivo: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario si no existe, luego guarda los cambios en el archivo."""
        if nombre in self.productos:
            print("El producto ya existe. Use la función de actualizar.")
            return
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto {nombre} agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad, precio):
        """Actualiza la cantidad y el precio de un producto existente."""
        if nombre not in self.productos:
            print("El producto no existe en el inventario.")
            return
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto {nombre} actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario si existe."""
        if nombre not in self.productos:
            print("El producto no existe en el inventario.")
            return
        del self.productos[nombre]
        self.guardar_inventario()
        print(f"Producto {nombre} eliminado correctamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario con su cantidad y precio."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for nombre, detalles in self.productos.items():
            print(f"Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")

# Interfaz de usuario en entorno sin input
if __name__ == "__main__":
    inventario = Inventario()
    acciones = [
        ("agregar", "Producto1", 10, 5.99),
        ("actualizar", "Producto1", 15, 6.49),
        ("eliminar", "Producto1"),
        ("mostrar",)
    ]

    for accion in acciones:
        if accion[0] == "agregar":
            inventario.agregar_producto(accion[1], accion[2], accion[3])
        elif accion[0] == "actualizar":
            inventario.actualizar_producto(accion[1], accion[2], accion[3])
        elif accion[0] == "eliminar":
            inventario.eliminar_producto(accion[1])
        elif accion[0] == "mostrar":
            inventario.mostrar_inventario()

    print("Ejecución completada.")
