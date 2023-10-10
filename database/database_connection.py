import mysql.connector

def get_db_connection():
    # connection_details = {
    #     "username": "admin",
    #     "password": "admin9986",
    #     "port" : 3306,
    #     "hostname": "pythoncommunity8.cvxbyvevf5y2.us-east-2.rds.amazonaws.com",
    #     "database" : "fitness_tracker_db"
    # }
    connection_details = {
            "username": "root",
            "password": "root",
            "port" : 3306,
            "hostname": "localhost",
            "database" : "python_community8"
        }
    connection_obj = None
    try:
        connection_obj = mysql.connector.connect(host=connection_details['hostname'],
                                port=connection_details['port'],
                                user=connection_details['username'],
                                password=connection_details['password'],
                                database=connection_details['database']
                                )
        return connection_obj
    except Exception as e:
        print("Error while connecting to the database", e)


if __name__ == '__main__':
    try:
        connection_obj = get_db_connection()
        if connection_obj.is_connected():
            cursor_obj = connection_obj.cursor()
            query_str = "create table students(rollno varchar(20), name varchar(30))" # DDL
            cursor_obj.execute(query_str)
            print("Successfully created table")
    except Exception as e:
        print("Error while connecting to the database", e)
    finally:
        if connection_obj is not None and connection_obj.is_connected():
            cursor_obj.close()
            connection_obj.close()



