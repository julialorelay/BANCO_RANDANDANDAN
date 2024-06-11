import unittest
from caixinha import Caixinha
from cliente import Cliente

class TesteCaixinha(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.__cliente = Cliente('John Doe', 25, 0)

    def test_get_nome(self):
        nome = 'Moto randandandan'
        caixinha = Caixinha(self.__cliente, nome, 100)

        self.assertTrue(caixinha.get_nome() == nome)

    # Teste sem hardcoded mas com erro
    def test_depositar(self):
        valor = 100
        caixinha = Caixinha(self.__cliente, 'Carro', valor)
        caixinha.depositar(100)
        self.assertTrue(caixinha.get_saldo() == 200)

    # Teste de saque de 200 reais (valor hardcoded)
    def test_sacar(self):
        caixinha = Caixinha(self.__cliente, 'Carro', 100)
        caixinha.sacar(100)
        self.assertTrue(caixinha.get_saldo() == 0)
