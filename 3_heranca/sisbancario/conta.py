from cliente import Cliente
from movimentacao import Movimentacao

class Conta:

    def __init__(self, numero: str, cliente: Cliente, saldo: float=0):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
        self._movimentacoes: list[Movimentacao] = [Movimentacao(f"Abertura da conta com saldo inicial de R$ {saldo:.2f}")]

    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def saldo(self):
        return self._saldo

    def _validar_saque(self, valor: float):
        if valor > 0 and self.saldo >= valor:
            return True
        return False

    # As mensagens de erro irão aparecer aqui mais tarde com uso de tratamento de exceções
    def sacar(self, valor):
        if self._validar_saque(valor): 
            self._saldo -= valor
            self._movimentacoes.append(Movimentacao(f"Saque de R$ {valor:.2f}"))
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._movimentacoes.append(Movimentacao(f"Depósito de R$ {valor:.2f}"))
            return True
        return False

    # usando referência antecipada para definir o tipo do parâmetro destino
    def transferir(self, destino: "Conta", valor):
        if self._validar_saque(valor):
            self._saldo -= valor
            destino._saldo += valor
            self._movimentacoes.append(Movimentacao(f"Transferência de R$ {valor:.2f} enviada para {destino}"))
            destino._movimentacoes.append(Movimentacao(f"Transferência de R$ {valor:.2f} recebida de {self}"))
            return True
        return False

    def obter_extrato(self):
        return self._movimentacoes

    def __str__(self):
        return f"{self._numero}:{self._cliente.nome}"