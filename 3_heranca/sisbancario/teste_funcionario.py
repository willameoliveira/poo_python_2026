from funcionario import Funcionario
from gerente import Gerente
from controle_bonificacoes import ControleBonificacoes

funcionario1 = Funcionario(nome="João", cpf="123.456.789-00", salario=3000)
gerente1 = Gerente(nome="Maria", cpf="987.654.321-00", salario=5000, senha="123", qtd_funcionarios=1)

print(f"\nAtributos de funcionario: {vars(funcionario1)}")
print(f"Atributos de gerente: {vars(gerente1)}")

print(f"\nBonificação do funcionario: R$ {funcionario1.get_bonificacao():.2f}")
print(f"Bonificação do gerente: R$ {gerente1.get_bonificacao():.2f}")

controle = ControleBonificacoes()
controle.registra(funcionario1)
controle.registra(gerente1)

print(f"\nTotal de bonificações: R$ {controle.total_bonificacoes:.2f}")