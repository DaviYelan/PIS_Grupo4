import cx_Oracle #type: ignore
class Connection:
    def __init__(self):
        self.dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='xe')
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(user='PIS', password='Kenichi04', dsn=self.dsn_tns, encoding="UTF-8")
            print("Connected to the database")
            self.cursor = self.connection.cursor()
        except cx_Oracle.DatabaseError as e:
            print(f"Database connection error: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute(self, query, params=None):
        if not self.cursor:
            raise Exception("Cursor is not initialized. Call connect() first.")
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor
