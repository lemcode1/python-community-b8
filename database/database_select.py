from database.database_connection import get_db_connection
conn_obj = None

def build_select_query(product_name = None, product_price= None,
                           category = None, brand = None, color = None):

    if product_name is None and product_price is None and \
            category is None and brand is None and color is None:  # when there is no filter
        select_query = "select * from mytra_products"

    if product_name is not None or product_price is not None or \
            category is not None or brand is not None or color is not None:
        select_query = "select * from mytra_products where "

    if product_name is not None: # product name filtering
        select_query = select_query + " product_name like '%"+product_name+"%'"
    if product_price is not None:
        select_query = select_query + " product_price = '"+product_price + "'"
    if category is not None:
        select_query = select_query + " category = '"+ category +"'"
    if brand is not None:
        select_query = select_query + " brand = '"+ brand + "'"
    if color is not None:
        select_query = select_query + " color = '"+ color + "'"

    return select_query

def filter_myntra_products(product_name = None, product_price= None,
                           category = None, brand = None, color = None):
    try:
        conn_obj = get_db_connection()
        if conn_obj.is_connected():
            cursor_obj = conn_obj.cursor()
            # select_query = "select * from mytra_products where brand in('Ramraj','AllenSolly')"
            select_query = build_select_query(product_name, product_price, category, brand, color)
            print("select_query ", select_query)
            cursor_obj.execute(select_query)
            result_set = cursor_obj.fetchall()  # list of rows, every row here is tuple of values
            # result_set = cursor_obj.fetchmany(2)
            for row in result_set:
                print(row)
            # cursor_obj.fetchall()
    except Exception as e:
        print("Error while fetching the records, ",e)
    finally:
        if conn_obj is not None and conn_obj.is_connected():
            cursor_obj.close()
            conn_obj.close()

if __name__ == '__main__':
    print("Please select what type of cloths that you need:")
    print("What do you want to filter with:")
    print("1.product_name")
    print("2.product_price")
    print("3.category")
    print("4.brand")
    print("5.color")
    selected_filter = int(input())
    enter_value = input("Enter a value")
    if selected_filter == 1:
        filter_myntra_products(product_name=enter_value)
    if selected_filter == 2:
        filter_myntra_products(product_price=enter_value)
    if selected_filter == 3:
        filter_myntra_products(category=enter_value)
    if selected_filter == 4:
        filter_myntra_products(brand=enter_value)
    if selected_filter == 5:
        filter_myntra_products(color=enter_value)
