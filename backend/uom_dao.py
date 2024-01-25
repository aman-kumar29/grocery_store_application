import mysql.connector

def get_uom():
    cnx = mysql.connector.connect(user='root', password='Aman*2004',
                              host='127.0.0.1',
                              database='grocery_store')
    
    cursor = cnx.cursor()
    query = ("SELECT * FROM uom")
    response = []
    cursor.execute(query)

    for (uom_id,uom_name) in cursor:
        response.append({
            "uom_id": uom_id,
            "uom_name": uom_name
        })
    cnx.close()
    return response


if __name__ == '__main__':
    print(get_uom())   