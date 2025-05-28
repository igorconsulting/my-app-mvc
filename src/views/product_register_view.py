class ProductRegisterView:
    def handle_register_product(self, body: dict) -> dict:
        try:
            self.__validate_body(body)

            product_infos = body["produto"]
            name = product_infos["nome"]
            taste = product_infos["taste"]
            price = int(product_infos["preco"])

            # Chamar Controller
            # response = controller.register_product(name, taste, price)

            return {
                "success": True,
                "Type": "product",
                "count": 1,
                "attributes": {
                    #"response": response
                    "product_name": name,
                    "taste": taste,
                    "price": price
                }
            }
        except:
            return {
                "success": False,
                "Erro": "Deu erro"
            }

    def __validate_body(self, body: dict) -> None:
        # response = validate_func_to_body(body)
        # if response is False: raise Exception("Body mal formatado!")
        if "produto" not in body:
            raise Exception("Deu erro")