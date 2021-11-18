from db import get_connection_db
from datetime import datetime


def insert_shoes(id, model, price, brand, size, image):
     cur = get_connection_db()
     with cur.cursor() as cursor:
        cursor.execute('INSERT INTO shoes (id, model, price, brand, size, image) VALUES(%s, %s,%s,%s,%s, %s)', (id, model, price, brand, size, image))  
     cur.commit()
     cur.close()

 

def delete_an_image( id):
    cur = get_connection_db()
    with cur.cursor() as cursor:
            cursor.execute("SELECT image FROM shoes WHERE id = %s", id)
            fila = cursor.fetchall()
            return fila 

    
def delete_shoe(id):
    cur = get_connection_db()
    with cur.cursor() as cursor:
        cursor.execute("DELETE FROM shoes WHERE id={0}" .format(id))
        cur.commit()


def get_shoe_edit(id):
    connection = get_connection_db()
    data = [] 
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM shoes WHERE id= %s", (id))
        data = cursor.fetchall()
    return data

def format_an_image(image):
    
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    if image.filename != '':
            nuevoNombreImagen =  tiempo + image.filename
            image.save("uploads/" + nuevoNombreImagen)
            return nuevoNombreImagen


def upload_an_image(image, id):
    cur = get_connection_db()
    with cur.cursor() as cursor:
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        if image.filename != '':
            nuevoNombreImagen =  tiempo + image.filename
            image.save("uploads/" + nuevoNombreImagen)
            cursor.execute("SELECT image FROM shoes WHERE id = %s", id)
            fila = cursor.fetchall()
            return fila


def update_shoe(id, model, price, brand, size, image):
    cur = get_connection_db()
    with cur.cursor() as cursor:
        cursor.execute("UPDATE shoes SET model = %s, price = %s, brand = %s, size = %s, image = %s  WHERE id = %s", (model, price, brand, size, image, id))
        
        

        cur.commit()


def get_shoes():
    connection = get_connection_db()
    shoes = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, model, price, brand, size from shoes")
        shoes = cursor.fetchall()
    connection.close()
    return shoes



