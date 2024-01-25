import mysql.connector

def get_all_products():
    cnx = mysql.connector.connect(user='root', password='Aman*2004',
                              host='127.0.0.1',
                              database='grocery_store')
    
    cursor = cnx.cursor()
    query = ("SELECT products.product_id,products.product_name,products.unit_of_measurement_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.unit_of_measurement_id = uom.uom_id")
    response = []
    cursor.execute(query)

    for (product_id, product_name,uom_id, price_per_unit,uom_name) in cursor:
        response.append({
            "product_id": product_id,
            "product_name":product_name,
            "uom_id":uom_id,
            "price_per_unit":price_per_unit,
            "uom_name":uom_name
        })
    cnx.close()
    return response


def insert_into_products(product):
    cnx = mysql.connector.connect(user='root', password='Aman*2004',
                              host='127.0.0.1',
                              database='grocery_store')
    
    cursor = cnx.cursor()
    query = ("INSERT INTO products "
              "(product_name, unit_of_measurement_id,price_per_unit)"
              "VALUES (%s, %s, %s)")
    data = (product['product_name'],product['unit_of_measurement_id'],product['price_per_unit'])
    cursor.execute(query,data)

    cnx.commit()
    cnx.close()
    return cursor.lastrowid

def delete_product(product_id):
    cnx = mysql.connector.connect(user='root', password='Aman*2004',
                              host='127.0.0.1',
                              database='grocery_store')
    
    cursor = cnx.cursor()
    query = ("DElETE from products where product_id=" + str(product_id))
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor.lastrowid


if __name__ == '__main__':
    print(get_all_products())   
    # print(insert_into_products({
    #     'product_name':'brocolli',
    #     'unit_of_measurement_id':'1',
    #     'price_per_unit':'30'
    # }))
    # delete_product(13)
    

