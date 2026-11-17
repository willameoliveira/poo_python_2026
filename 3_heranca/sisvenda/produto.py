class Produto:
    
    def __init__(self, descricao: str, preco_unitario: float, estoque: int=0):
        self._descricao = descricao
        self._preco_unitario = preco_unitario
        self._estoque = estoque
    
    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        if descricao:
            self._descricao = descricao

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        if preco_unitario > 0:
            self._preco_unitario = preco_unitario

    @property
    def estoque(self):
        return self._estoque

    def incrementar_estoque(self, quantidade: int):
        if quantidade > 0:
            self._estoque += quantidade
    
    def decrementar_estoque(self, quantidade: int):
        if quantidade > 0 and quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        else:
            return False