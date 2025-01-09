# Programa para calcular el área de un círculo.
# Este programa solicita el radio del círculo al usuario y calcula su área.

import math  # Importa la biblioteca matemática para usar la constante pi

def calcular_area_circulo(radio):
    """
    Función que calcula el área de un círculo dado su radio.
    Parámetro:
    - radio (float): El radio del círculo.
    Retorno:
    - area (float): El área calculada.
    """
    if radio <= 0:
        print("El radio debe ser mayor a 0.")
        return None
    area = math.pi * (radio ** 2)
    return area

# Solicitar el radio al usuario
radio_circulo = float(input("Ingresa el radio del círculo en centímetros: "))

# Calcular el área del círculo
area_circulo = calcular_area_circulo(radio_circulo)

# Comprobar y mostrar el resultado
if area_circulo is not None:
    print(f"El área del círculo con radio {radio_circulo} cm es {area_circulo:.2f} cm².")
    # Tipo de dato booleano
    print(f"¿El área es mayor a 50 cm²? {'Sí' if area_circulo > 50 else 'No'}")