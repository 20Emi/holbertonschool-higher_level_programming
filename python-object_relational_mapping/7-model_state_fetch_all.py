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
    la = sqlalchemy.select(State.id, State.name).order_by(State.id)
    ls = conexion.execute(la).fetchall()
    for a in ls:
        print("{}: {}".format(a[0], a[1]))
