from flask import Flask,jsonify,request
import json
import mysql.connector
import products_dao, uom_dao       
connection = mysql.connector.connect(user='root', password='Aman*2004',
                              host='127.0.0.1',
                              database='grocery_store')

app = Flask(__name__)

@app.route('/getProducts')
def get_products():
    products = products_dao.get_all_products()
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM', methods = ['GET'])
def get_uom():
    uom = uom_dao.get_uom()
    response = jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_into_products(request_payload)
    response = jsonify({'product_id' : product_id})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(request.form['product_id'])
    response = jsonify({
        'return_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response




if __name__ == '__main__':
    print("Server started and running for grocery management system")
    app.run(port = 5000)