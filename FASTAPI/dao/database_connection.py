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





