import pymysql
from bd import conectarmysql

def mostrarcomentario():

    conexion=conectarmysql()
    comentario=[]
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM comentariospy"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    
def instertar_comentario():
    conexion=conectarmysql()
    comentario=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT correo, nombre, comentario FROM comentarios.py")
        comentarios=cursor.fetchall()
    conexion.close()
    return comentarios

def eliminar_comentario(comment):
    conexion=conectarmysql()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comentariospy WHERE comentario = %s", (comment,))
    conexion.commit()
    conexion.close()

def obtener_comentario_pmail(mail):
    conexion=conectarmysql()
    correo=None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre, comentario WHERE correo=%s", (mail,))
        correo=cursor.fetchone()
    conexion.close()
    return correo

def editar_comentario(com):
    conexion=conectarmysql()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE comentariospy SET comentario =%s, WHERE correo=%s", (com))
        conexion.commit()
        conexion.close()
        