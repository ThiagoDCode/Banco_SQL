from random import choice
from lib_def import *
import os


class Banco:
    def __init__(self, cliente, cpf, senha, conta, saldo):
        self.__cliente = cliente
        self.__cpf = cpf
        self.__senha = senha
        self.__conta = conta
        self.__saldo = saldo

    def info_cliente(self):
        print(f'\n{"<< DADOS DA CONTA >>":=^30}\n'
              f'CLIENTE: {self.__cliente}   CPF: {self.__cpf}   CONTA: {self.__conta}\n'
              f'SALDO: R${self.__saldo:.2f}')

    def depositar(self):
        try:
            valor_deposito = float(input('Valor do depósito: R$'))
            if valor_deposito > 0:
                self.__saldo += valor_deposito
                print(f'\nDEPÓSITO EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.__saldo:.2f}\n')
            else:
                print(erro_cor('ERRO! Valores negativos não é válido para depósito\n'))
        except ValueError:
            print(erro_cor('ERRO! Valor de depósito inválido\n'))

    def sacar(self):
        try:
            valor_saque = float(input('Valor do saque: R$'))
            if valor_saque <= self.__saldo:
                self.__saldo -= valor_saque if valor_saque > 0 else (-valor_saque)  # TODO: vê melhor forma de converter
                print(f'\nSAQUE EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.__saldo:.2f}\n')
            else:
                print(erro_cor('ERRO! Saldo insuficiente\n'))
        except ValueError:
            print(erro_cor('ERRO! Valor de saque inválido\n'))

    def check_pass(self):
        try:
            senha_entrada = int(input('Digite a senha: '))
            if senha_entrada == self.__senha:
                return True
            else:
                print(erro_cor('Senha incorreta\n'))
        except ValueError:
            print(erro_cor('Senha incorreta\n'))
        os.system('pause')


contas_clientes = {}
while True:
    os.system('cls')
    match menu('ABRIR CONTA', 'ACESSAR CONTA', 'ENCERRAR SESSÃO'):

        case 3:
            print('\nObrigado por escolher o Dalla$$ Bank')
            break

        case 1:
            os.system('cls')

            nome_cliente = verify_name('Nome do Cliente: ')
            cpf_cliente = verify_cpf('CPF do Cliente: ')
            senha_cliente = verify_pass('Senha de 4 dígitos: ')
            num_conta = str(choice(range(1000, 9999)))
            deposito_inicial = verify_num('Valor de Depósito: R$')
            contas_clientes[num_conta] = Banco(nome_cliente, cpf_cliente, senha_cliente, num_conta, deposito_inicial)

            print(f'\n|> CONTA CRIADA COM SUCESSO!\n'
                  f'CLIENTE: {nome_cliente}    CPF: {cpf_cliente}   CONTA: {num_conta}\n'
                  f'DEPÓSITO: R${deposito_inicial:.2f}\n')
            os.system('pause')

        case 2:
            buscar = input('Número da Conta: ')
            os.system('cls')

            try:
                if contas_clientes[buscar].check_pass():
                    while True:
                        contas_clientes[buscar].info_cliente()
                        match menu('SACAR', 'DEPOSITAR', 'SAIR DA CONTA'):
                            case 3:
                                break
                            case 1:
                                os.system('cls')
                                contas_clientes[buscar].sacar()
                                os.system('pause')
                            case 2:
                                os.system('cls')
                                contas_clientes[buscar].depositar()
                                os.system('pause')
            except KeyError:
                print(erro_cor('ERRO! Desculpe, conta não encontrada\n'))
                os.system('pause')
