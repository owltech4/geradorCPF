import tkinter as tk
from tkinter import messagebox
from validator import CPFValidator, CPFGenerator

def validar_cpf():
    cpf = entry.get()
    validator = CPFValidator(cpf)
    valido, msg = validator.validar()
    messagebox.showinfo("Resultado da Validação", msg)

def gerar_cpf():
    cpf_gerado = CPFGenerator.gerar()
    messagebox.showinfo("CPF Gerado", f"CPF Gerado: {cpf_gerado}")

# Interface Gráfica
root = tk.Tk()
root.title("Validador de CPF")

frame = tk.Frame(root, padx=50, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Insira o CPF:")
label.pack(pady=5)

entry = tk.Entry(frame, width=30)
entry.pack(pady=5)

validate_button = tk.Button(frame, text="Validar CPF", command=validar_cpf)
validate_button.pack(pady=5)

generate_button = tk.Button(frame, text="Gerar CPF", command=gerar_cpf)
generate_button.pack(pady=5)

root.mainloop()
