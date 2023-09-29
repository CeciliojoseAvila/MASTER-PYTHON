import mysql.connector
# conexion
def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="8629",
        database="master_python",
        port=3306

    )
#print(database) probar la conexion, debe mostrar algo asi:<mysql.connector.connection_cext.CMySQLConnection object at 0x000001BCB7FF7E50>

    cursor = database.cursor(buffered=True)

    return [database, cursor]