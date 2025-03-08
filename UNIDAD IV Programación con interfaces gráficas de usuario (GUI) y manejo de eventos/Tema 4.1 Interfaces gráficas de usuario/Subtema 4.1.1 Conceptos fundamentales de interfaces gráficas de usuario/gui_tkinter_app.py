import tkinter as tk  # Importamos la librería Tkinter para crear la GUI
from tkinter import messagebox  # Importamos messagebox para mostrar mensajes emergentes

# Función para agregar un elemento a la lista
def agregar_elemento():
    texto = entrada.get()  # Obtener el texto ingresado por el usuario
    if texto:  # Verificar que el campo de texto no esté vacío
        lista.insert(tk.END, texto)  # Agregar el texto a la lista
        entrada.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar un campo vacío.")  # Mostrar advertencia

# Función para limpiar la lista de elementos
def limpiar_lista():
    lista.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Función para limpiar el campo de texto
def limpiar_texto():
    entrada.delete(0, tk.END)  # Vaciar el contenido del campo de entrada

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Crear y posicionar la etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un elemento:")
etiqueta.pack(pady=5)

# Crear y posicionar el campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Crear y posicionar el botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Crear y posicionar la lista para mostrar elementos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=5)

# Crear y posicionar el botón "Limpiar Lista"
boton_limpiar_lista = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar_lista.pack(pady=5)

# Crear y posicionar el botón "Limpiar Texto"
boton_limpiar_texto = tk.Button(ventana, text="Limpiar Texto", command=limpiar_texto)
boton_limpiar_texto.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
