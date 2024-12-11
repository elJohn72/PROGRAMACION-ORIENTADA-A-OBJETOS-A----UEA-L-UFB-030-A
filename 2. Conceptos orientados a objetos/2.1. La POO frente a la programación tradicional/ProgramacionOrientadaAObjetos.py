# Función para ingresar temperaturas diarias
# Solicita al usuario las temperaturas de cada día de la semana y las almacena en una lista
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    for dia in range(7):  # Itera a través de los 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))  # Solicita la temperatura del día
        temperaturas.append(temp)  # Agrega la temperatura a la lista
    return temperaturas  # Retorna la lista de temperaturas

# Función para calcular el promedio semanal
# Recibe una lista de temperaturas y devuelve su promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Calcula el promedio sumando las temperaturas y dividiendo por la cantidad de días

# Programa principal
# Controla el flujo principal del programa
def main():
    print("Programa de cálculo de promedio semanal de temperaturas (Tradicional)")
    temperaturas = ingresar_temperaturas()  # Llama a la función para ingresar las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcula el promedio semanal
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")  # Muestra el promedio al usuario

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecuta la función principal
