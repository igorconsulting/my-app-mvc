"""
Modúlo responsável por inicializar a estrutura do banco de dados.
"""
import sqlite3
from driver.db_connector import DBConnector

create_user_query = """
                    CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    height REAL NOT NULL
                    )
                    """

def create_users_table(db_connector: DBConnector):
    # 1. Instanciar DBConnector
    # 2. Conectar
    # 3. Executar a query de criação da tabela
    # 4. Fechar conexão
    db_connector.connect()
    cursor = db_connector.get_cursor()
    cursor.execute(create_user_query)
    db_connector.close()
