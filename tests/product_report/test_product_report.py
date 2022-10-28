from inventory_report.inventory.product import Product


def test_relatorio_produto():
    teste = Product(
        1,
        "Ebytr",
        "Claudio", "2001-01-01", "2023-01-01", "123456", "em local seco"
    )
    mockString = (
        f'O produto {teste.nome_do_produto} '
        f'fabricado em {teste.data_de_fabricacao} '
        f'por {teste.nome_da_empresa} com validade '
        f'até {teste.data_de_validade} '
        f'precisa ser armazenado {teste.instrucoes_de_armazenamento}.'
    )
    print(mockString)
    assert teste.__repr__() == mockString
