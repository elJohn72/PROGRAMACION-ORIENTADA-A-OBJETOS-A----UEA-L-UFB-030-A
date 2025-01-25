import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD I Fundamentos de la programación orientada a objetos/1.2. Tecnicas de programacion/ejercicio1.py',
        '2': 'UNIDAD I Fundamentos de la programación orientada a objetos/2. Conceptos orientados a objetos/2.1. La POO frente a la programación tradicional/ProgramacionOrientadaAObjetos.py',
        '3': 'UNIDAD I Fundamentos de la programación orientada a objetos/2. Conceptos orientados a objetos/2.1. La POO frente a la programación tradicional/ProgramacionTradicional.py',
        '4': 'UNIDAD I Fundamentos de la programación orientada a objetos/2. Conceptos orientados a objetos/2.2. Características de la programación orientada a objetos/EjemplosMundoReal_POO/ReservaDeHotel.py',
        '5': 'UNIDAD II Objetos, clases, Herencia, Polimorfismo/2. Elementos de programación/2.1. Tipos de datos, Identificadores/calculo_area.py',
        '6': 'UNIDAD II Objetos, clases, Herencia, Polimorfismo/2. Elementos de programación/2.2: Definición de Clase_Subtema_2.3.Definición de Objeto_2.4.Herencia, Encapsulación, Polimorfismo/constructores_destructores.py',
        '7': 'UNIDAD II Objetos, clases, Herencia, Polimorfismo/2. Elementos de programación/2.2: Definición de Clase_Subtema_2.3.Definición de Objeto_2.4.Herencia, Encapsulación, Polimorfismo/sistema_gestion_vehiculos.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()