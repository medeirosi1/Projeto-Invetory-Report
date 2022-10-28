from inventory_report.inventory.product import Product



def test_cria_produto():
    teste = Product(1, "Ebytr", "Claudio", "2001-01-01", "2023-01-01", "123456", "em local seco")
    assert teste.id == 1
    assert teste.nome_do_produto == "Ebytr"
    assert teste.nome_da_empresa == "Claudio"
    assert teste.data_de_fabricacao == "2001-01-01"
    assert teste.data_de_validade == "2023-01-01"
    assert teste.numero_de_serie == "123456"
    assert teste.instrucoes_de_armazenamento == "em local seco"