import pymysql

def get_connection_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='mysql1',
        db='shoes_db'
    )
