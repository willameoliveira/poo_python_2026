from conta import Conta
from cliente import Cliente

cliente1 = Cliente(nome="José", telefone="987667", cpf="876545778")
cliente2 = Cliente(nome="Maria", telefone="987667", cpf="876545778")

conta1 = Conta(numero="2345-34", cliente=cliente1)
conta2 = Conta(numero="2444-34", cliente=cliente2)

conta1.depositar(100)
conta1.depositar(50)
conta1.sacar(10)
conta1.transferir(conta2, 50)

print("Extrato conta 1: ")
for movimentacao in conta1.obter_extrato():
    print(movimentacao)

print("\nExtrato conta 2: ")
for movimentacao in conta2.obter_extrato():
    print(movimentacao)