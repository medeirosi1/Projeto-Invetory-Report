from inventory_report.inventory.product import Product


def test_cria_produto():
    newProduct = Product(
        1,
        "Ebytr",
        "Claudio", "2001-01-01", "2023-01-01", "123456", "em local seco"
    )
    assert newProduct.id == 1
    assert newProduct.nome_do_produto == "Ebytr"
    assert newProduct.nome_da_empresa == "Claudio"
    assert newProduct.data_de_fabricacao == "2001-01-01"
    assert newProduct.data_de_validade == "2023-01-01"
    assert newProduct.numero_de_serie == "123456"
    assert newProduct.instrucoes_de_armazenamento == "em local seco"
