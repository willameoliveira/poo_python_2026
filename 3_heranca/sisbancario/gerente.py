from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, salario: float, senha: str, qtd_funcionarios: int):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios
    
    def get_bonificacao(self):
        return self._salario * 0.15