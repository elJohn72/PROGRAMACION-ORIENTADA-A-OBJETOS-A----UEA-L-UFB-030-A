# Clase que representa la información diaria del clima
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Inicializa una lista vacía para almacenar las temperaturas

    # Método para agregar una temperatura a la lista
    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)  # Agrega la temperatura proporcionada a la lista

    # Método para calcular el promedio semanal de temperaturas
    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:  # Verifica si la lista está vacía
            return 0  # Retorna 0 si no hay temperaturas registradas
        return sum(self.temperaturas) / len(self.temperaturas)  # Calcula el promedio semanal

# Programa principal
def main():
    print("Programa de cálculo de promedio semanal de temperaturas (POO)")
    clima = ClimaDiario()  # Crea una instancia de la clase ClimaDiario

    # Solicita al usuario que ingrese la temperatura de cada día de la semana
    for dia in range(7):  # Itera a través de los 7 días
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))  # Solicita la temperatura del día
        clima.ingresar_temperatura(temp)  # Agrega la temperatura al objeto clima

    promedio = clima.calcular_promedio_semanal()  # Calcula el promedio semanal usando el método de la clase
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")  # Muestra el promedio al usuario

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecuta la función principal
