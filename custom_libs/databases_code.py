import os
import cx_Oracle
from file_management_code import FileManagement


class Databases(FileManagement):
    def __init__(self):
        super().__init__()

    def connect_to_db(self, database):
        creds = self.get_credentials(database)
        db_prop = self.get_database_properties(database)

        dsn = cxOracle.makedsn(
            db_prop.get("host"),
            db_prop.get("port"),
            service_name=database
        )
        conn = cx_Oracle.connect(
            user=creds.get("username"),
            password=creds.get("password"),
            dsn=dsn
        )
        cursor = conn.cursor()
        connection_properties = {
            "cursor": cursor,
            "connection": conn
        }
        return connection_properties

    @staticmethod
    def close_db_connection(connection):
        connection.close()

    def execute_query(self, query, database):
        connection_properties = self.connect_to_db(database)
        cursor = connection_properties.get("cursor")
        connection = connection_properties.get("connection")

        cursor.execute(query)

        column_names = [c[0] for c in cursor.description]
        data = cursor.fetchall()
        data = [list(i) for i in data]
        data = [column_names] + [list(i) for i in data]
        self.close_db_connection(connection)
        return data
