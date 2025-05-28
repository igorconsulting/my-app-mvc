# Receba os dados validados (nome, idade, altura)
# 
# Use o DBConnector para abrir conexão
# 
# Insira o usuário na tabela usuarios
# 
# Retorne confirmação (ou ID, ou dados inseridos)
from driver.db_connector import DBConnector
from src.model.user import User
from src.model.user import UserRepository

class UserController:
    def __init__(self, db_connector:DBConnector):
        self.db_connector = db_connector

    def __connect_database(self):
        self.db_connector.connect()

    def __insert_user(self,user_infos: dict):
        cursor = self.db_connector.get_cursor()
        user = User(user_infos)
        user_repository = UserRepository(db_connection=self.db_connector)
        user_repository.insert_one(user=user,cursor=cursor)
        cursor.close()

    def register_user(self, user_infos):
        self.__connect_database()
        self.__insert_user(user_infos)
        self.db_connector.commit()
        self.db_connector.close()

    def get_user(self,user_name:str):
        self.__connect_database()
        cursor = self.db_connector.get_cursor()
        user_repository = UserRepository(db_connection=self.db_connector)
        users = user_repository.search_by_name(user_name=user_name,cursor=cursor)
        self.db_connector.close()

        return users
        