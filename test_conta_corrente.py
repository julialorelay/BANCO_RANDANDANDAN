import unittest
from conta_corrente import ContaCorrente
from cliente import Cliente

class TesteContaCorrent(unittest.TestCase):
    def _init_(self, methodName: str = "runTest"):
        super()._init_(methodName)
        self.__cliente = Cliente('John Doe', 25, 0)
        self._conta_corrente = ContaCorrente(self._cliente, 0)

    def get_saldo(self):
        self.assertTrue(False)

    def test_depositar(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)

    def test_criar_caixinha(self):
        self.assertTrue(False)

    def test_get_caixinhas(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)