import tkinter as tk
from tkinter import ttk, messagebox

def analizar():
    funcion = entrada.get()

    if not funcion.strip():
        messagebox.showwarning("Error", "Por favor ingresa una función .")
        return

    variables_encontradas = set()
    cantidad_operaciones = 0
    terminos = []

    for i, caracter in enumerate(funcion):
        if caracter.isalpha():
            variables_encontradas.add(caracter)

        if caracter in "+-*/^":
            cantidad_operaciones += 1

        if i < len(funcion) - 1:
            siguiente = funcion[i + 1]
            if caracter.isdigit() and siguiente.isalpha():
                cantidad_operaciones += 1
            elif caracter.isalpha() and siguiente.isdigit():
                cantidad_operaciones += 1

    terminos = funcion.replace("-", "+-").split("+")
    terminos = [t.strip() for t in terminos if t.strip()]

    resultado.set(
        f"Función ingresada: {funcion}\n"
        f"Variables encontradas: {', '.join(sorted(variables_encontradas))}\n"
        f"Cantidad de variables: {len(variables_encontradas)}\n"
        f"Cantidad de operaciones: {cantidad_operaciones}\n"
        f"Términos: {', '.join(terminos)}"
    )

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Analizador de Funciones Matemáticas")
ventana.geometry("500x350")
ventana.configure(bg="#f4f6f7")

# --- Estilos ---
estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12), padding=6)
estilo.configure("TLabel", font=("Arial", 12))

# --- Título ---
etiqueta_titulo = tk.Label(
    ventana,
    text="Analizador de Funciones",
    font=("Arial", 16, "bold"),
    bg="#f4f6f7",
    fg="#2c3e50"
)
etiqueta_titulo.pack(pady=10)

# --- Entrada ---
entrada = ttk.Entry(ventana, font=("Consolas", 14))
entrada.pack(pady=10, ipadx=20, ipady=5)

# --- Botón ---
boton_analizar = ttk.Button(ventana, text="Analizar", command=analizar)
boton_analizar.pack(pady=10)

# --- Resultado ---
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(
    ventana,
    textvariable=resultado,
    font=("Consolas", 12),
    bg="#ecf0f1",
    fg="#2c3e50",
    relief="groove",
    justify="left",
    anchor="w"
)
etiqueta_resultado.pack(fill="both", expand=True, padx=20, pady=10)

ventana.mainloop()