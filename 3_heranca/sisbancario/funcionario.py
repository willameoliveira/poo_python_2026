class Funcionario:

    def __init__(self, nome: str, cpf: str, salario: float):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def get_bonificacao(self):
        return self._salario * 0.10