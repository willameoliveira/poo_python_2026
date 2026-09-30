from cliente import Cliente
from conta import Conta
from movimentacao import Movimentacao

cliente1 = Cliente(nome="José", telefone="2134234", cpf="98867")
conta1 = Conta(numero="3435-24", cliente=cliente1, saldo=100)

cliente2 = Cliente(nome="Maria", telefone="432435", cpf="56754")
conta2 = Conta(numero="3424-34", cliente=cliente2)

conta1.depositar(50)
conta1.sacar(100)
conta1.transferir(conta2, 40)

print("Extrato da conta1:")
for movimentacao in conta1.obter_extrato():
    print(movimentacao)

print("\nExtrato da conta2:")
for movimentacao in conta2.obter_extrato():
    print(movimentacao)