import pymysql

def conectarmysql():

    host="localhost"
    user="root"
    clave=""
    db="test"
    return pymysql.connect(host=host,user=user,password=clave,database=db)

def mostrarcomentario():

    conexion=conectarmysql()
    comentario=[]
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM test"
        cursor.execute(sql)
        mostrar=cursor.fetchall()
        return mostrar