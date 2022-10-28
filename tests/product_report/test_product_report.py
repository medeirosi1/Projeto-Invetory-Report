from inventory_report.inventory.product import Product


def test_relatorio_produto():
    teste = Product(1, "Ebytr", "Claudio", "2001-01-01", "2023-01-01", "123456", "em local seco")
    mockString = "O produto Ebytr fabricado em 2001-01-01 por Claudio com validade até 2023-01-01 precisa ser armazenado em local seco."
    assert teste.__repr__() == mockString