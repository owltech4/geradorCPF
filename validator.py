from utils import only_numbers
import random

class CPFValidator:
    def __init__(self, cpf):
        self.cpf = only_numbers(cpf)
        self.digito1 = 0
        self.digito2 = 0

    def validar_input(self):
        entrada_e_sequencial = self.cpf == self.cpf[0] * len(self.cpf)
        if entrada_e_sequencial:
            return False, 'Você enviou dados sequenciais'
        return True, ''

    def calcular_soma(self, cpf, length):
        soma = 0
        for i in range(length):
            multiplicador = (length + 1) - i
            soma += int(cpf[i]) * multiplicador
        return soma

    def calcular_digito(self, soma):
        digito = (soma * 10) % 11
        return digito if digito < 10 else 0

    def validar_digitos(self):
        cpf_nove_digitos = self.cpf[:9]
        soma1 = self.calcular_soma(cpf_nove_digitos, 9)
        self.digito1 = self.calcular_digito(soma1)
        cpf_dez_digitos = self.cpf[:9] + str(self.digito1)
        soma2 = self.calcular_soma(cpf_dez_digitos, 10)
        self.digito2 = self.calcular_digito(soma2)

        cpf_gerado = cpf_dez_digitos + str(self.digito2)

        if self.cpf == cpf_gerado:
            return True, f"CPF {self.cpf} validado"
        else:
            return False, f"CPF {self.cpf} inválido"

    def validar(self):
        self.cpf = only_numbers(self.cpf)  # Garantir que o CPF esteja limpo antes de validar
        valido, msg = self.validar_input()
        if not valido:
            return False, msg
        if len(self.cpf) != 11:
            return False, "CPF inválido. Deve conter 11 dígitos numéricos."
        return self.validar_digitos()


class CPFGenerator:
    @staticmethod
    def gerar():
        cpf_gerado = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        validator = CPFValidator(cpf_gerado)
        validator.validar_digitos()
        cpf_gerado += str(validator.digito1) + str(validator.digito2)
        return cpf_gerado
