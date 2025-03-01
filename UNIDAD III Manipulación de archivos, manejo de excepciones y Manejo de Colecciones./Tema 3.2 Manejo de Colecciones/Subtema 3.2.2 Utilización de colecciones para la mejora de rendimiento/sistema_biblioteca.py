class Libro:
    """
    Representa un libro con título, autor, categoría e ISBN.
    Se usa una tupla para almacenar título y autor, ya que son inmutables.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} - {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    """
    Representa un usuario de la biblioteca con nombre, ID único y libros prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario  # ID único
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}), Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Gestiona la biblioteca, incluyendo libros, usuarios y préstamos.
    Utiliza:
    - Diccionario para libros disponibles (ISBN como clave).
    - Conjunto para IDs de usuario únicos.
    - Diccionario para el historial de préstamos.
    """
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios = set()  # Conjunto para IDs de usuarios
        self.historial_prestamos = {}  # Diccionario de préstamos

    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca si no está registrado."""
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca si existe."""
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca si su ID es único."""
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """Elimina un usuario de la biblioteca si existe."""
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.historial_prestamos[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario si ambos existen en la biblioteca."""
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.historial_prestamos[id_usuario]
            usuario.libros_prestados.append(self.libros_disponibles[isbn])
            del self.libros_disponibles[isbn]
            print(f"Libro {isbn} prestado a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Devuelve un libro prestado a la biblioteca."""
        if id_usuario in self.usuarios:
            usuario = self.historial_prestamos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro {isbn} devuelto por {usuario.nombre}")
                    return
            print("Libro no encontrado en los préstamos del usuario.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, keyword):
        """Busca libros por título, autor o categoría."""
        resultados = [libro for libro in self.libros_disponibles.values() if keyword.lower() in libro.datos[0].lower() or keyword.lower() in libro.datos[1].lower() or keyword.lower() in libro.categoria.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, id_usuario):
        """Lista los libros actualmente prestados a un usuario."""
        if id_usuario in self.usuarios:
            usuario = self.historial_prestamos[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("No tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Ejemplo de uso:
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario
usuario1 = Usuario("Juan Pérez", "U001")
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("U001", "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver libro
biblioteca.devolver_libro("U001", "12345")

# Buscar libro
biblioteca.buscar_libro("Novela")
