from models.employee_model import EmployeeModel
from dao.database_connection import get_db_connection


def add_employee_dao(emp : EmployeeModel, address):
    conn_obj = None
    try:
        conn_obj = get_db_connection()
        cursor_obj = conn_obj.cursor()
        insert_query = "insert into emp_data(first_name, last_name, mail, mobile_number, address) \
            values(%s,%s,%s,%s, %s)"
        values = (emp.first_name, emp.last_name, emp.mail, emp.mobile_number, address)
        cursor_obj.execute(insert_query, values)
        conn_obj.commit()
    except Exception as e:
        print("Error while adding a new employee ", e)
    finally:
        conn_obj.close()