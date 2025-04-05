import tkinter as tk
from tkinter import messagebox  # Para mostrar mensajes de advertencia o información

# Clase principal que contiene toda la lógica de la aplicación
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")  # Título de la ventana
        self.root.geometry("400x400")        # Tamaño de la ventana

        # Campo de entrada para escribir nuevas tareas
        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10)  # Margen vertical
        self.task_entry.focus()        # El cursor inicia aquí

        # Marco contenedor de los botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        # Botón para añadir tareas
        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Botón para marcar tareas como completadas
        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(expand=True, fill=tk.BOTH, pady=10)

        # Atajos de teclado (eventos de teclado)
        self.root.bind("<Return>", lambda event: self.add_task())     # Enter = Añadir tarea
        self.root.bind("<c>", lambda event: self.complete_task())     # 'c' minúscula = Completar
        self.root.bind("<C>", lambda event: self.complete_task())     # 'C' mayúscula = Completar
        self.root.bind("<d>", lambda event: self.delete_task())       # 'd' minúscula = Eliminar
        self.root.bind("<D>", lambda event: self.delete_task())       # 'D' mayúscula = Eliminar
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla Delete = Eliminar
        self.root.bind("<Escape>", lambda event: self.root.quit())    # Escape = Cerrar aplicación

    # Función para añadir una nueva tarea
    def add_task(self):
        task = self.task_entry.get().strip()  # Obtiene el texto del campo
        if task:
            self.task_listbox.insert(tk.END, task)  # Añade la tarea al final de la lista
            self.task_entry.delete(0, tk.END)       # Limpia el campo de entrada
        else:
            # Muestra advertencia si no se escribió nada
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

    # Función para marcar una tarea como completada
    def complete_task(self):
        selected = self.task_listbox.curselection()  # Obtiene el índice de la tarea seleccionada
        if selected:
            task = self.task_listbox.get(selected)
            if not task.startswith("[✔] "):  # Verifica si ya está marcada
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, f"[✔] {task}")  # Añade check visual
        else:
            messagebox.showinfo("Sin Selección", "Selecciona una tarea para marcarla como completada.")

    # Función para eliminar una tarea
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)  # Elimina la tarea de la lista
        else:
            messagebox.showinfo("Sin Selección", "Selecciona una tarea para eliminarla.")

# Punto de inicio del programa
if __name__ == "__main__":
    root = tk.Tk()            # Se crea la ventana principal
    app = TaskManager(root)   # Se instancia la clase TaskManager
    root.mainloop()           # Se inicia el bucle principal de la GUI
