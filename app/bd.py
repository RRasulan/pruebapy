import pymysql

def conectarmysql():

    host="localhost"
    user="root"
    clave=""
    db="comentariospy"
    return pymysql.connect(host=host,user=user,password=clave,database=db)
