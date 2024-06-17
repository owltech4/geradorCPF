import tkinter as tk
from tkinter import messagebox


def geradorCPF():
    import random
    
    CPF_gerado = ''
    for char in range(9):
        CPF_gerado += str(random.randint(0,9))
    digito1 = calcular_digito(somaCPF(CPF_gerado, 9))
    CPF_gerado += str(digito1)
    digito2 = calcular_digito(somaCPF(CPF_gerado, 10))
    CPF_gerado += str(digito2)
    print("CPF Gerado:", CPF_gerado)
    validadorCPF(CPF_gerado,digito1,digito2)

def somaCPF(CPF, length):
    soma = 0
    for i in range(length):
        multiplicador = (length + 1) - i
        soma += int(CPF[i]) * multiplicador
    return soma

def calcular_digito(soma):
    digito = (soma * 10) % 11
    return digito if digito < 10 else 0

def multipleReplace(text):
    for char in ".!?,-":
        text = text.replace(char, "")
    return text

def onlynumbers(text):
    import re
    text = re.sub(r'[^0-9]','',text) #Expressão regular que vai substituir tudo aquilo que não for entre 0 e 9 por vazio
    return text

def validadorInput(text):
    import sys
    entrada_e_sequencial = text == text[0] * len(text)
    if entrada_e_sequencial:
        print('Você enviou dados sequenciais')
        sys.exit()

def somaCPF1(CPF):
    soma = 0
    for i in range(9):
        multiplicador = 10 - i
        soma += int(CPF[i]) * multiplicador
    return soma

def somaCPF2(CPF):
    soma = 0
    for i in range(10):
        multiplicador = 11 - i
        soma += int(CPF[i]) * multiplicador
    return soma

def validadorDigito(digito):
    if digito <= 9:
        print(f"Digito é: {digito}")
    else:
        digito = 0
        print(f"Digito é: {digito}")

def validadorCPF(CPF,digito1,digito2):
    cpf_gerado = str(CPF[:9])+str(digito1)+str(digito2)
    if CPF == cpf_gerado:
        return print(f"CPF {CPF} validado")
    else:
        return print(f"CPF {CPF} inválido")


if __name__ == "__main__":
    CPF = input('Insira o CPF: ')
    validadorInput(CPF)
    CPF = onlynumbers(CPF)
    digito1 = (somaCPF1(CPF)*10) % 11
    validadorDigito(digito1)
    digito2 = (somaCPF2(CPF)*10) % 11
    validadorDigito(digito2)
    validadorCPF(CPF,digito1,digito2)

