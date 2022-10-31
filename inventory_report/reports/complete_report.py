from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        count_products = dict()
        for item in inventory:
            if item["nome_da_empresa"] in count_products.keys():
                count_products[item["nome_da_empresa"]] += 1
            else:
                count_products[item["nome_da_empresa"]] = 1
        stock = ""
        for key, value in count_products.items():
            stock += f"- {key}: {value}\n"
        return (
            f"{super().generate(inventory)}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock}"
        )
