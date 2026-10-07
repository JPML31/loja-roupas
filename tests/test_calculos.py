import pytest

from loja.calculos import frete, total_carrinho

def teste_carrinho_vazio_custa_zero(): 
    assert total_carrinho([]) == 0


def teste_soma_preco_vezes_quantidade():
    #PREPARAR
    itens = [(39.90, 3), (129.90, 1)]
    #AGIR
    total = total_carrinho(itens)
    #CONFERIR
    assert total == 249.6

def test_frete_abaixo_de_200_custa_15():
    assert frete(199.99) == 15.0

def test_frete_a_partir_de_200_e_gratis():
    assert frete(200.00) == 0.0
    assert frete(350.00) == 0.0
