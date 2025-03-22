import tkinter as tk
from tkinter import messagebox

# Creamos la clase principal de la aplicación
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")  # Título de la ventana

        # Campo de entrada para escribir nuevas tareas
        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.pack(pady=10)  # Espaciado vertical
        self.entrada_tarea.bind("<Return>", self.agregar_tarea_evento)  # Manejo del evento Enter

        # Componente de lista para mostrar las tareas actuales
        self.lista_tareas = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=5)
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)  # Evento: doble clic = completar tarea

        # Botón para añadir una tarea
        self.boton_aniadir = tk.Button(root, text="Añadir Tarea", width=20, command=self.agregar_tarea)
        self.boton_aniadir.pack(pady=5)

        # Botón para marcar como completada
        self.boton_completar = tk.Button(root, text="Marcar como Completada", width=20, command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

    # ---------------------- FUNCIONALIDAD DE LOS BOTONES Y EVENTOS ----------------------

    # Función para agregar tarea al presionar el botón
    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()  # Obtenemos el texto ingresado
        if tarea != "":
            self.lista_tareas.insert(tk.END, tarea)  # Agregamos la tarea al final de la lista
            self.entrada_tarea.delete(0, tk.END)  # Limpiamos el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribe una tarea antes de añadirla.")

    # Función que se ejecuta al presionar Enter en el campo de entrada
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()  # Llama a la función agregar_tarea

    # Función para marcar una tarea como completada
    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()  # Obtener el índice de la tarea seleccionada
        if seleccion:
            indice = seleccion[0]
            tarea = self.lista_tareas.get(indice)
            if not tarea.startswith("✔️ "):  # Evitar marcar varias veces
                self.lista_tareas.delete(indice)
                self.lista_tareas.insert(indice, f"✔️ {tarea}")  # Añade el símbolo de completado
        else:
            messagebox.showinfo("Seleccionar Tarea", "Selecciona una tarea para marcar como completada.")

    # Función que se ejecuta al hacer doble clic en una tarea
    def marcar_completada_evento(self, event):
        self.marcar_completada()  # Llama a la misma función que el botón

    # Función para eliminar una tarea seleccionada
    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion[0])  # Elimina la tarea del Listbox
        else:
            messagebox.showinfo("Seleccionar Tarea", "Selecciona una tarea para eliminar.")

# ---------------------- PUNTO DE ENTRADA PRINCIPAL ----------------------
# Creamos la ventana principal de la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()  # Instancia de la ventana
    app = ListaTareasApp(ventana)  # Creamos la app
    ventana.mainloop()  # Inicia el bucle principal de la GUI