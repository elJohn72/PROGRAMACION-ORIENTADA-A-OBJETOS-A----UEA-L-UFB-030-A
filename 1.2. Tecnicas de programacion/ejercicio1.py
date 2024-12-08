class EspacioNave:
    def __init__(self, nombre, potencia, escudo, energia):
        self.nombre = nombre
        self.potencia = potencia
        self.escudo = escudo
        self.energia = energia

    def mostrar_atributos(self):
        print(f"Nave: {self.nombre}")
        print(f"Potencia de Ataque: {self.potencia}")
        print(f"Escudo: {self.escudo}")
        print(f"Energía: {self.energia}")

    def esta_operativa(self):
        return self.energia > 0

    def recibir_dano(self, dano):
        dano_real = max(0, dano - self.escudo)
        self.energia -= dano_real
        self.energia = max(0, self.energia)  # Evita energía negativa
        print(f"{self.nombre} recibe {dano_real} de daño. Energía restante: {self.energia}")

    def atacar(self, objetivo):
        print(f"{self.nombre} dispara a {objetivo.nombre} con potencia {self.potencia}.")
        objetivo.recibir_dano(self.potencia)

# Simulación de batalla espacial entre dos naves

def iniciar_batalla(nave1, nave2):
    ronda = 1
    while nave1.esta_operativa() and nave2.esta_operativa():
        print(f"\nRonda {ronda}")
        nave1.atacar(nave2)
        if nave2.esta_operativa():
            nave2.atacar(nave1)
        ronda += 1

    if nave1.esta_operativa():
        print(f"\n{nave1.nombre} gana la batalla!")
    elif nave2.esta_operativa():
        print(f"\n{nave2.nombre} gana la batalla!")
    else:
        print("\nAmbas naves han sido destruidas!")

# Crear naves espaciales
nave1 = EspacioNave("Interceptor", 15, 8, 50)
nave2 = EspacioNave("Destructor", 12, 10, 60)

# Mostrar atributos iniciales
nave1.mostrar_atributos()
nave2.mostrar_atributos()

# Iniciar batalla
iniciar_batalla(nave1, nave2)
