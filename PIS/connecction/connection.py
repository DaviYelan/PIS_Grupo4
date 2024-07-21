import cx_Oracle # type: ignore 

dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe', 'PIS') 

try:
    # Establish connection
    connection = cx_Oracle.connect(user='SYSTEM', password='ROOT123', dsn=dsn_tns, encoding="UTF-8") 
    print("Connected to the database")

    # Create a cursor
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM cuenta")

    # Fetch and print results
    for row in cursor:
        print(row)

    # Close cursor
    cursor.close()

    # Close connection
    connection.close()

except cx_Oracle.DatabaseError as e:
    print(f"Database connection error: {e}")
