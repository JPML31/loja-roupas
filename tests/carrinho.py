class Carrinho:
    def __init__(self):
        self._itens = [] # pares (produto, quantidade)
        self._finalizado = False

    def adicionar(self, produto, quantidade=1):
        if self._finalizado:
            raise CarrinhoFinalizadoError("carrinho finalizado não recebe peças")
if not isinstance(produto, Produto):    
    raise TypeError("só é possível adicionar um Produto")
if quantidade <= 0:
    raise ValueError("quantidade deve ser positiva")
self._itens.append((produto, quantidade))
