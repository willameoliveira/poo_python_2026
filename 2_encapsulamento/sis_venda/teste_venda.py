from produto import Produto
from venda import Venda

produto1 = Produto(descricao="mouse",preco_unitario=100,estoque=2)
produto2 = Produto(descricao="pendrive",preco_unitario=50,estoque=7)
produto3 = Produto(descricao="monitor",preco_unitario=1000,estoque=10)
venda1 = Venda()
venda1.adicionar_item(produto=produto1, quantidade=1)
venda1.adicionar_item(produto=produto2, quantidade=4)
venda1.adicionar_item(produto=produto3, quantidade=3)

print(venda1)

venda1.remover_item(produto=produto2)
print(venda1)