import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        entry_fecha.set_date('')
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos")

# Función para eliminar evento seleccionado
def eliminar_evento():
    item_seleccionado = tree.selection()
    if item_seleccionado:
        if messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el evento seleccionado?"):
            tree.delete(item_seleccionado)
    else:
        messagebox.showwarning("Ningún evento seleccionado", "Selecciona un evento para eliminar")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("700x400")

# --- Frame principal para TreeView ---
frame_lista = tk.Frame(ventana)
frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# TreeView para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill=tk.BOTH, expand=True)

# --- Frame para entradas ---
frame_entradas = tk.Frame(ventana)
frame_entradas.pack(padx=10, pady=5, fill=tk.X)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entradas, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entradas, date_pattern='yyyy-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entradas, text="Hora:")
label_hora.grid(row=0, column=2, padx=5, pady=5)
entry_hora = tk.Entry(frame_entradas)
entry_hora.grid(row=0, column=3, padx=5, pady=5)

label_descripcion = tk.Label(frame_entradas, text="Descripción:")
label_descripcion.grid(row=1, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entradas, width=60)
entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# --- Frame para botones ---
frame_botones = tk.Frame(ventana)
frame_botones.pack(padx=10, pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar aplicación
ventana.mainloop()
