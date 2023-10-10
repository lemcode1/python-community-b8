from database_connection import get_db_connection

def insert_student(first_name, last_name, email, mobile_number):
    connection_obj = None
    try:
        connection_obj = get_db_connection()
        cursor_obj = connection_obj.cursor()
        # insert_query = "insert into students values(1234,'Nani')"
        insert_query = "insert into py_students values('"+first_name+"',"+last_name+"','"+email+"','"+mobile_number+"')"
        print('insert query ', insert_query)
        cursor_obj.execute(insert_query)
        connection_obj.commit()
        print("Insertions is completed")
    except Exception as e:
        connection_obj.rollback()
        print("Error while inserting the students, rolledback the transaction ", e)
    finally:
        if connection_obj is not None and connection_obj.is_connected():
            cursor_obj.close()
            connection_obj.close()

if __name__ == '__main__':
    print("Enter student info to create new student")
    first_name= input("Enter first name:")
    last_name = input("Enter last name:")
    mail = input("Enter mail:")
    phone_num = input("Enter phone num:")
    insert_student(first_name, last_name, mail, phone_num)
