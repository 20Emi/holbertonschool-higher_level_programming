#!/usr/bin/python3
"""task 0"""
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    # cierre del cursor
    conex.close()
