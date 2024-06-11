class Caixinha():
    def __init__(self, cliente, nome_caixinha, saldo_inicial):
        self.__cliente = cliente
        self.__nome = nome_caixinha
        self.__saldo = saldo_inicial

    def depositar(self, valor_deposito):
        self.__saldo = self.__saldo + valor_deposito

    def sacar(self, valor_saque):
        self.__saldo = self.__saldo - valor_saque

    def get_saldo(self):
        return self.__saldo
    
    def get_nome(self):
        return self.__nome
    