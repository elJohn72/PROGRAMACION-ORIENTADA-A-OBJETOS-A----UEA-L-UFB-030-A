class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


def menu():
    inventario = Inventario()
    opciones = ["1", "2", "3", "4", "5", "6"]
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        try:
            opcion = input("Seleccione una opción: ") if hasattr(__builtins__, 'input') else "6"
        except OSError:
            opcion = "6"

        if opcion not in opciones:
            print("Opción no válida, intente nuevamente.")
            continue

        if opcion == "1":
            id = input("Ingrese ID único del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje vacío si no quiere cambiar): ")
            precio = input("Ingrese nuevo precio (deje vacío si no quiere cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    menu()
