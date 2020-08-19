import mysql.connector


class MySqlConnect(object):

    def __init__(self, database) -> None:
        self._myDb = mysql.connector.connect(host='localhost', user="root", passwd='Root#123', database=database)
        self._myCursor = self._myDb.cursor()

    def get_records(self, table=None):
        if not self._myDb.is_connected():
            return "Error. Connect not established"

        if table is not None:
            self._myCursor.execute(f'SELECT * FROM {table}')
            records = self._myCursor.fetchall()
            return records
        return None

    def close_connection(self):
        self._myDb.disconnect()

    def execute(self, query: str):
        if query is None or len(query) == 0 or not self._myDb.is_connected():
            return
        self._myCursor.execute(query)
        self._myDb.commit()


if __name__ == "__main__":
    mysql_connect = MySqlConnect(database="profiles")
    print(mysql_connect.get_records(table="sample_app_sessions"))
    mysql_connect.close_connection()
