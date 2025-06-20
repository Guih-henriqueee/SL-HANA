from typing import Optional
from hdbcli import dbapi

class DbConnection:
    def __init__(self, settings: dict):
        self._DATABASE_USER     = settings["DATABASE_USER"]
        self._DATABASE_PASSWORD = settings["DATABASE_PASSWORD"]
        self._DATABASE_HOST     = settings["DATABASE_HOST"]
        self._DATABASE_PORT     = int(settings["DATABASE_PORT"])    
        self._DATABASE_SCHEMA   = settings["DATABASE_SCHEMA"]

    def get_connection(self) -> Optional[dbapi.Connection]:
        try:
            connection = dbapi.connect(
                address=self._DATABASE_HOST,
                port=self._DATABASE_PORT,
                user=self._DATABASE_USER,
                password=self._DATABASE_PASSWORD,
                database=self._DATABASE_SCHEMA
            )
            print("Conexão com o SAP HANA estabelecida com sucesso!")
            return connection
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def test_connection(self):
        conn = None
        try:
            conn = self.get_connection()
            if conn:
                print("Teste de conexão bem-sucedido.")
            else:
                print("Falha no teste de conexão.")
        finally:
            if conn:
                conn.close()
                print("Conexão encerrada após o teste.")


    def close_connection(self, connection: Optional[dbapi.Connection]) -> None:
        if connection:
            connection.close()
            print("Conexão com o SAP HANA encerrada com sucesso!")
