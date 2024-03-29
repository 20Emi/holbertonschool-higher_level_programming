#!/usr/bin/python3
"""task 2"""
import sys  # para los argumentos
import MySQLdb

if __name__ == "__main__":
    # conexion con la base de datos
    conex = MySQLdb.connect(host="localhost",
                            user=sys.argv[1],
                            password=sys.argv[2],
                            database=sys.argv[3])

    # Creacion del cursor
    cursor = conex.cursor()

    # ejecucion
    sql_query = "SELECT * FROM states ORDER BY id"
    cursor.execute(sql_query)

    for row in cursor.fetchall():
        if row[1] == sys.argv[4]:
            print("{}".format(row))

    # cierre del cursor
    conex.close()
