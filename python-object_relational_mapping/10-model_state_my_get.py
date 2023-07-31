#!/usr/bin/python3
"""Start link class to table in database"""


import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    """task 7"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    conexion = engine.connect()
    state = sqlalchemy.select(State.id, State.name).order_by(State.id)
    result = conexion.execute(state).fetchall()
    flag = False

    for iter in result:
        if iter[1] == sys.argv[4]:
            print("{}".format(iter[0]))
            flag = True
    if not flag:
        print('Not found')
