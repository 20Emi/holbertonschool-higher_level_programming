#!/usr/bin/python3
"""task 1"""
import sys  # para los argumentos
import MySQLdb

if __name__ == "__main__":

    conex = MySQLdb.connect(host="localhost",
                            user=sys.argv[1],
                            password=sys.argv[2],
                            database=sys.argv[3])
    cursor = conex.cursor()

    sql_query = "SELECT * FROM states ORDER BY id"
    cursor.execute(sql_query)

    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    # cierre del cursor
    conex.close()
