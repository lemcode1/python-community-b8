from database.database_connection import get_db_connection
def filter_products_by_brand_and_color(brand, color):
    conn_obj = None
    try:
        conn_obj = get_db_connection()
        cursor_obj = conn_obj.cursor()
        # str_parameterized_query = "select * from mytra_products where brand=%s and color=%s"
        str_parameterized_query = "select * from mytra_products where brand=%s"
        # tuple_input = (brand, color)
        tuple_input = (brand,)
        cursor_obj.execute(str_parameterized_query, tuple_input)
        result = cursor_obj.fetchall()
        for row in result:
            print(row)

    except Exception as e:
        print("Error while filtering the data", e)
    finally:
        if conn_obj is not None and conn_obj.is_connected():
            cursor_obj.close()
            conn_obj.close()

filter_products_by_brand_and_color('Ramraj', 'white')