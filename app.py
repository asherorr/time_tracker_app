from models import (Base, session, Tracker, engine)


if __name__ == "__main__":
    Base.metadata.create_all(engine)