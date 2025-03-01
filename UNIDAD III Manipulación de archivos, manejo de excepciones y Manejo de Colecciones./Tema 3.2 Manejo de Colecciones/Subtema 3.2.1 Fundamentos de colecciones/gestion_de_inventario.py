import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo = "inventario.json"
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto.to_dict())

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos.values()], archivo)
        except OSError as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as archivo:
                productos = json.load(archivo)
                self.productos = {p["id"]: Producto.from_dict(p) for p in productos}
        except (FileNotFoundError, OSError):
            self.productos = {}

# Interfaz de usuario
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar inventario\n6. Salir")
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                id_producto = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            elif opcion == "2":
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)
            elif opcion == "3":
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
                precio = input("Nuevo precio (dejar vacío para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            elif opcion == "4":
                nombre = input("Nombre del producto a buscar: ")
                print(inventario.buscar_producto(nombre))
            elif opcion == "5":
                inventario.mostrar_productos()
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except OSError as e:
            print(f"Error de entrada/salida: {e}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores correctos.")
