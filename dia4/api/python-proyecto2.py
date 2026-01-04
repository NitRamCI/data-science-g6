import requests
from tabulate import tabulate
import mysql.connector

    

URL = 'https://restcountries.com/v3.1/region/America'

response = requests.get(URL)

if response.status_code == 200:
    print('conexión a api exitosa')
    data = response.json()
    rows = []
    for dic_user in data:
        nombre = dic_user['name']['common']
        capital = dic_user.get('capital', ['N/A'])[0]
        region = dic_user['region']
        population = dic_user['population']
        rows.append([nombre,capital,region,population])
        
    headers = ['Nombre','Capital','Region','Population']
    print(tabulate(rows,headers,tablefmt='grid'))
    
    # CARGAMOS DATA EN LA BASE DE DATOS
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root2025',
        database='db_g6'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuario(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(255) NOT NULL,
            capital VARCHAR(255) NOT NULL,
            region VARCHAR(255),
            population BIGINT
            );
            """
        )
        #INSERTAMOS LOS USUARIOS A LA BD
        for usuario in rows:
            cursor.execute(
                """
                insert into usuario(nombre,capital,region,population)
                values(%s,%s,%s,%s)
                """,
                usuario
            )
        connection.commit()
        connection.close()
        print(f' Registros importados a la base de datos')
    else:
        print('Error al conectarse a la base de datos')
else:
    print(f'error : {response.status_code}')