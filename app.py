from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='flask_garage',
        user='garadm7841',
        password='SP7c3$@uwL84jmSEoP3',
        port=5432,
        cursor_factory=RealDictCursor
    )


@app.route('/')
def index():
    return 'Bienvenue dans mon API Flask test'

@app.route('/cars', methods=['GET'])
def get_car_list():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM car ORDER BY car_id')
    cars = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(cars)

@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    inserted_cars = []

    if isinstance(data, list):
        for car in data:
            brand = car.get("brand")
            model = car.get("model")

            cursor.execute(
                'INSERT INTO car (brand, model) VALUES (%s, %s) RETURNING *',
                (brand, model)
            )

            inserted_cars.append(cursor.fetchone())

    else:
        brand = data.get("brand")
        model = data.get("model")

        cursor.execute(
            'INSERT INTO car (brand, model) VALUES (%s, %s) RETURNING *',
            (brand, model)
        )

        inserted_cars.append(cursor.fetchone())

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify(inserted_cars), 201

# Mise à jour d'une voiture
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.get_json()

    brand = data['brand']
    model = data['model']

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        'UPDATE car SET brand = %s, model = %s WHERE car_id = %s RETURNING *',
        (brand, model, id)
    )

    car = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if car:
        return jsonify(car), 200
    else:
        return 'Voiture non trouvée', 404
    
    # Suppression d'une voiture
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        'DELETE FROM car WHERE car_id = %s RETURNING *',
        (id,)
    )

    car = cursor.fetchone()

    connection.commit()

    cursor.close()
    connection.close()

    if car:
        return 'Voiture supprimée', 200
    else:
        return 'Voiture non trouvée', 404
    
@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM car WHERE car_id = %s', (id,))
    car = cursor.fetchone()

    cursor.close()
    connection.close()

    if car:
        return jsonify(car)
    else:
        return 'Voiture non trouvée', 404   
    
    
@app.route('/cars/brand/<string:brand>', methods=['GET'])
def get_car_by_brand(brand):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM car WHERE brand = %s', (brand,))
    car = cursor.fetchone()

    cursor.close()
    connection.close()

    if car:
        return jsonify(car)
    else:
        return 'Voiture non trouvée', 404   
    