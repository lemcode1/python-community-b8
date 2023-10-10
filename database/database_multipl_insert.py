from database_connection import get_db_connection
connection_obj = None
try:
    connection_obj = get_db_connection()
    cursor_obj = connection_obj.cursor()
    # insert_query = "insert into py_students values('Y','Nani', 'nani@gmail.com',1122),('Y','naga', 'nani@gmail.com',1133)," \
    #                "('Y','gopi', 'nani@gmail.com',1144),('Y','durga', 'nani@gmail.com',1155)"
    # cursor_obj.execute(insert_query)
    insert_query = "insert into py_students values(%s, %s, %s, %d)"

    records = [('Y','Nani', 'nani@gmail.com',1122), ('Y','Nani', 'nani@gmail.com',1122),
               ('Y','Nani', 'nani@gmail.com',1122),('Y','Nani', 'nani@gmail.com',1122)]
    cursor_obj.executemany(insert_query, records)
    connection_obj.commit()
    print("Insertions is completed")
except Exception as e:
    connection_obj.rollback()
    print("Error while inserting the students, rolledback the transaction ", e)
finally:
    if connection_obj is not None and connection_obj.is_connected():
        cursor_obj.close()
        connection_obj.close()
