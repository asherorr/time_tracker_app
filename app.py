from models import (Base, session, Tracker, engine)


def menu():
    while True:
        print('''
        \rOPTIONS
        \r----
        \r1) Add Event
        \r2) View Times
        \r3) See Statistics
        ''')
        choice = input("What would you like to do? ")
        if choice in range(1-4):
            return choice
        else:
            input('''
                  \rPlease choose only one of the options above.
                  \rA number from 1-3.
                  \rPress enter to try again. ''')
        

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()