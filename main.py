from conta_corrente import ContaCorrente
from cliente import Cliente

# Primeiro elemento de uma lista é representado por 0
menu_funcoes = ['Sair']
clientes = []

def cadastrar_cliente():
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    documento = input('Digite o documento: ')

    novo_cliente = Cliente(nome, idade, documento)
    clientes.append(novo_cliente)

# Adiciona as funções ao menu em ordem
menu_funcoes.append(cadastrar_cliente) # Segundo elemento de uma lista é o número 1

print('''
      Bem vindo ao Sistema de Gestão Banco Randandandan
      Logado como: Caixa Presencial 1
      Operações:
      [0]: Sair
      [1]: Cadastrar clientes
      ''')

opcao = int(input('Digite um operação: '))

while opcao != 0:
    menu_funcoes[opcao]()
    