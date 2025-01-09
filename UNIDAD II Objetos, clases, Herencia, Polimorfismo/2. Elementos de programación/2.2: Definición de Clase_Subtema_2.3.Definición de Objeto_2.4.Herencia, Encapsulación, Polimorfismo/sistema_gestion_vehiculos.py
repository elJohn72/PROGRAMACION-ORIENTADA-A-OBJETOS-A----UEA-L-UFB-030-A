# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase derivada (herencia)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas  # Atributo encapsulado

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        if puertas > 0:
            self.__puertas = puertas
        else:
            print("El número de puertas debe ser mayor que cero.")

    # Sobrescritura de método (polimorfismo)
    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Puertas: {self.__puertas}"

# Clase derivada (polimorfismo adicional)
class Motocicleta(Vehiculo):
    def mostrar_informacion(self):
        return super().mostrar_informacion() + ", Tipo: Motocicleta"

# Creación de objetos
auto = Automovil("Toyota", "Corolla", 4)
moto = Motocicleta("Yamaha", "R6")

# Uso de métodos
print(auto.mostrar_informacion())
auto.set_puertas(5)
print(f"Número de puertas actualizado: {auto.get_puertas()}")

print(moto.mostrar_informacion())
