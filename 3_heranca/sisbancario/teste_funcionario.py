from funcionario import Funcionario
from gerente import Gerente

funcionario1 = Funcionario(nome="João", cpf="123.456.789-00", salario=3000)
gerente1 = Gerente(nome="Maria", cpf="987.654.321-00", salario=5000, senha="123", qtd_funcionarios=1)

print(f"Atributos de funcionario: {vars(funcionario1)}")
print(f"Atributos de gerente: {vars(gerente1)}")

print(f"Bonificação do funcionario: {funcionario1.get_bonificacao()}")
print(f"Bonificação do gerente: {gerente1.get_bonificacao()}")