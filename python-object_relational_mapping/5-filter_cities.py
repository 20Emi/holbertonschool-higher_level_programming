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
    sql_query = """SELECT cities.id, cities.name, states.name FROM states
    INNER JOIN cities ON cities.state_id = states.id
    WHERE states.name = '{}'
    ORDER BY id""".format(sys.argv[4])
    cursor.execute(sql_query)

    flag = False
    for row in cursor.fetchall():
        if flag == True:
            print(', ', end='')
        else:
            flag = True
        print('{}'.format(row[1]), end='')
    print()
    # cierre del cursor
    conex.close()
