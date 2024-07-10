import pymysql
from bd import conectarmysql

def mostrarcomentario():

    conexion=conectarmysql()
    comentario=[]
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM comentariospy"
        cursor.execute(sql)
        mostrar=cursor.fetchall()
        return mostrar