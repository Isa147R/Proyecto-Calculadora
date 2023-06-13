import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = combo_operacion.get()

        if operacion == 'Suma':
            resultado = num1 + num2
        elif operacion == 'Resta':
            resultado = num1 - num2
        elif operacion == 'Multiplicación':
            resultado = num1 * num2
        elif operacion == 'División':
            resultado = num1 / num2

        label_resultado.config(text="Resultado: " + str(resultado))

    except ValueError:
        label_resultado.config(text="Error: Ingresa números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear los widgets
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()

label_operacion = tk.Label(ventana, text="Operación:")
label_operacion.pack()
combo_operacion = ttk.Combobox(ventana, values=['Suma', 'Resta', 'Multiplicación', 'División'])
combo_operacion.pack()

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
