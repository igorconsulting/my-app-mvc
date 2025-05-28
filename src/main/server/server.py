from flask import Flask
from src.main.routes.users import user_routes_bp
from driver.db_setup import create_users_table
from driver.db_connector import DBConnector
from driver.paths import DB_PATH

app = Flask(__name__)

# Inicializa conexão com o banco
db_connector = DBConnector(db_path=DB_PATH)

# Garante a estrutura de tabelas
create_users_table(db_connector=db_connector)

# Registra rotas com dependências resolvidas
app.register_blueprint(user_routes_bp)