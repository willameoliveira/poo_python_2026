class Conta:

    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def exibir_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor