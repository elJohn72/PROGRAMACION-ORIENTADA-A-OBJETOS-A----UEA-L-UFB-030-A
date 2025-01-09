# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, disponible=True):
        self.numero = numero  # Número de habitación
        self.tipo = tipo  # Tipo de habitación (individual, doble, suite)
        self.disponible = disponible  # Estado de disponibilidad

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo} - {'Disponible' if self.disponible else 'Ocupada'}"

# Clase que representa el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []  # Lista para almacenar habitaciones

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)  # Agrega una nueva habitación al sistema

    def mostrar_habitaciones_disponibles(self):
        print("\nHabitaciones disponibles:")
        for hab in self.habitaciones:
            if hab.disponible:
                print(hab)

    def reservar_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero and hab.disponible:
                hab.disponible = False
                print(f"\n¡Reserva confirmada! Habitación {numero} reservada con éxito.")
                return
        print("\nHabitación no disponible o no existe.")

# Crear instancias de habitaciones y sistema de reservas
sistema = SistemaReservas()
sistema.agregar_habitacion(Habitacion(101, "Individual"))
sistema.agregar_habitacion(Habitacion(102, "Doble"))
sistema.agregar_habitacion(Habitacion(103, "Suite"))

# Mostrar habitaciones disponibles
sistema.mostrar_habitaciones_disponibles()

# Reservar una habitación
sistema.reservar_habitacion(102)

# Verificar nuevamente las habitaciones
sistema.mostrar_habitaciones_disponibles()