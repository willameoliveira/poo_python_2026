class Conta:

    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    # O print fica por conta de quem chama o método. Isso torna nossa classe reusável para outros frontend (web, android, etc).
    def exibir_saldo(self):
        return self.saldo

    # As mensagens de erro irão aparecer aqui mais tarde com uso de tratamento de exceções
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    # usando referência antecipada para definir o tipo do parâmetro destino
    def transferir(self, destino: "Conta", valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False