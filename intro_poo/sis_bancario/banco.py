from cliente import Cliente
from conta import Conta

cliente1 = Cliente("José", "(86)988997766", "887.345.654-87")
cliente2 = Cliente("Maria", "(86)988997767", "665.563.644-54")

print(f"Nome: {cliente1.nome}")
print(f"Telefone: {cliente1.telefone}")
print(f"CPF: {cliente1.cpf}")

conta1 = Conta("003456-8", 100.00, cliente1)
print(f"Número da conta: {conta1.numero}")
print(f"Saldo da conta: {conta1.saldo}")
print(f"Cliente da conta: {conta1.cliente.nome}")

print(f"Saldo da conta1: {conta1.exibir_saldo()}")
conta1.sacar(50)
print(f"Saldo da conta1: {conta1.exibir_saldo()}")
conta1.depositar(100)
print(f"Saldo da conta1: {conta1.exibir_saldo()}")
