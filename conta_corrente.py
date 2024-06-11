from utils import Utils
from caixinha import Caixinha

class ContaCorrente:
    def __init__(self, cliente, deposito_inicial = 0):
        self.__cliente = cliente
        self.__saldo = deposito_inicial
        self.__caixinhas = {}

        self.__caixinhas['reserva'] = Caixinha(self.__cliente, 'Reserva de Emergência', 0)
        pass

    def depositar(self, valor_deposito):
        self.__saldo =+ valor_deposito

    def sacar(self, valor_saque):
        self.__saldo = valor_saque

    def get_saldo(self):
        return self.__saldo

    def criar_caixinha(self, nome_caixinha, valor_deposito):
        primeira_palavra = Utils().pegar_primeira_palavra(nome_caixinha)
        chave_caixinha = primeira_palavra.lower()

        self.__caixinhas[chave_caixinha] = Caixinha(self.__cliente, nome_caixinha, valor_deposito)

    def deletar_caixinha(self, chave_caixinha):
        caixinha = self.__caixinhas[chave_caixinha]

        if caixinha.get_saldo() == 0:
            del self.__caixinhas[chave_caixinha]

    def get_caixinhas(self):
        return self.__caixinhas

    def salvar(self, chave_caixinha, valor_deposito):
        if valor_deposito > self.__saldo:
            return 'Saldo insuficiente'
        else:
            self.__caixinhas[chave_caixinha].depositar(valor_deposito)

    def retirar(self, chave_caixinha, valor_retirada):
        caixinha = self.__caixinhas[chave_caixinha]
        if valor_retirada > caixinha.get_saldo():
            return 'Saldo de caixinha insuficiente para retirada'
        else:
            self.__caixinhas[chave_caixinha].depositar(valor_retirada)