from produto import Produto

class Item_Venda:
    
    def __init__(self, produto:Produto, quantidade: int):
        self._produto = produto
        self._quantidade = quantidade
        self._valor = self._calcular_subtotal()
    
    @property
    def produto(self):
        return self._produto
    
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade
        self._valor = self._calcular_subtotal()

    @property
    def valor(self):
        return self._valor

    def _calcular_subtotal(self):
        return self._produto.preco_unitario * self._quantidade