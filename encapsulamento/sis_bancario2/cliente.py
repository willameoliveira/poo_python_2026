class Cliente:

    def __init__(self, nome, telefone, cpf):
        self._nome = nome
        self._telefone = telefone
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property
    def cpf(self):
        return self._cpf
