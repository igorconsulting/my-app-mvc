from src.controller.user_controller import UserController
from driver.db_connector import DBConnector

class UserView:
    def __init__(self, db_connector: DBConnector):
        self.db_connector = db_connector
        self.user_controller = UserController(db_connector=self.db_connector)

    def handle_register_user(self, body: dict) -> dict:
        try:
            self.__validate_body(body)

            user_infos = body["usuario"]
            user_data = self.__map_user_fields(user_infos=user_infos)
            self.user_controller.register_user(user_data)

            return {
                "success": True,
                "Type": "User",
                "count": 1,
                "attributes": user_data
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
                    }
        
    def __validate_body(self, body: dict) -> None:
        # response = validate_func_to_body(body)
        # if response is False: raise Exception("Body mal formatado!")
        if "usuario" not in body:
            raise ValueError("Campo 'usuario' ausente")
        
        user = body["usuario"]
        if not all(k in user for k in ("nome", "idade", "altura")):
            raise ValueError("Campos obrigatórios: nome, idade, altura")
        
    def __map_user_fields(self, user_infos: dict) -> dict:
        return {
            "name": user_infos["nome"],
            "age": user_infos["idade"],
            "height": user_infos["altura"]
        }
    
    def handle_get_user(self,user_name:str)->dict:
        response = None
        try:
            name = self.__validate_name(user_name)
            response = self.user_controller.get_user(name)
            mapped_response = [
            self.__map_user_output_fields(user) for user in response
            ]

            return {
                "success": True,
                "Type": "User",
                "count": len(response),
                "attributes": mapped_response
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def __validate_name(self,name:str) -> str:
        return name.lower()
    
    def __map_user_output_fields(self, user_data: dict) -> dict:
        return {
            "nome": user_data["name"],
            "idade": user_data["age"],
            "altura": user_data["height"]
        }
