import datetime


class SimpleReport:

    @classmethod
    def generate(cls, inventory):
        date = cls.min_date(inventory)
        validate = cls.validate(inventory)
        count_products = cls.count_products(inventory)
        return (
            f"Data de fabricação mais antiga: {date}\n"
            f"Data de validade mais próxima: {validate}\n"
            f"Empresa com mais produtos: {count_products}"
        )

    @classmethod
    def min_date(cls, inventory):
        return min(
            [item["data_de_fabricacao"] for item in inventory]
        )

    @classmethod
    def validate(cls, inventory):
        return min(
            [item["data_de_validade"] for item in inventory if (
                item["data_de_validade"] > str(datetime.datetime.now())
            )]
        )

    @classmethod
    def count_products(cls, inventory):
        count_products = dict()
        for item in inventory:
            if item["nome_da_empresa"] in count_products.keys():
                count_products[item["nome_da_empresa"]] += 1
            else:
                count_products[item["nome_da_empresa"]] = 1
        return max(count_products, key=count_products.get)
