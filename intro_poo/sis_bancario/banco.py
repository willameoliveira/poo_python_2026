from cliente import Cliente
from conta import Conta

cliente1 = Cliente("José", "(86)988997766", "887.345.654-87")
cliente2 = Cliente("Maria", "(86)988997767", "665.563.644-54")

print(f"Nome: {cliente1.nome}")
print(f"Telefone: {cliente1.telefone}")
print(f"CPF: {cliente1.cpf}")

conta1 = Conta("003456-8", 100.00, cliente1)
print(f"\nNúmero da conta: {conta1.numero}")
print(f"Saldo da conta: {conta1.saldo}")
print(f"Cliente da conta: {conta1.cliente.nome}")

conta1.sacar(50)
print(f"\nSaldo da conta1 depois de sacar 50: {conta1.exibir_saldo()}")
conta1.depositar(100)
print(f"Saldo da conta1 depois de depositar 100: {conta1.exibir_saldo()}")

print(f"\nDados da variável de referência conta1: {conta1}") 

conta2 = Conta("004554-7", 200.00, cliente2)
if conta1.transferir(conta2, 50):
    print("\nTransferência de R$ 50 realizada com sucesso!")
    print(f"Saldo conta 1: {conta1.exibir_saldo()}")
    print(f"Saldo conta 2: {conta2.exibir_saldo()}")
else:
    print("\nTransferência falhou!")