from driver.db_connector import DBConnector
from sqlite3 import Cursor

class User:
    def __init__(self,user_infos: dict):
        self.name = user_infos["name"]
        self.age = user_infos["age"]
        self.height = user_infos["height"]


class UserRepository:
    def __init__(self, db_connection: DBConnector):
        self.db_connection = db_connection
        self.insert_query = f"""
                INSERT INTO users (name,age,height) VALUES (?,?,?)
                """

    def insert_one(self, user: User, cursor: Cursor):
        cursor.execute(self.insert_query,
                       (user.name,user.age,user.height))
        
    def insert_many(self, users: list[User], cursor: Cursor):
        users_tuple = self.__get_users_tuple(users)
        cursor.executemany(self.insert_query,users_tuple)

    def __get_users_tuple(self,users:list[User])-> list[tuple]:
        return [(user.name,user.age,user.height) for user in users]
    
    def search_by_name(self,user_name:str, cursor: Cursor) -> list[dict]:
        query = "SELECT * FROM users"

        if user_name is not None:
            query = "SELECT * FROM users WHERE name = ?"
        
        cursor.execute(query, (user_name,))
        # extract rows
        rows = cursor.fetchall()
        #extract columns
        columns = [col[0] for col in cursor.description]
        # cursor.description = 
        # ( name, type_code, 
        #   display_size, internal_size, 
        #   precision, scale, null_ok)

        return [dict(zip(columns,row)) for row in rows]


