#!/usr/bin/python3
"""Delete the users that contains "a" in the table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cal = State(name="California")
    san = City(name="San Francisco")
    cal.cities.append(san)
    session.add(cal)
    session.commit()
    session.close()
