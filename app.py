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
            
def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "1":
            # add event
            pass
        elif choice == "2":
            #view times
            pass
        elif choice == "3":
            #search statistics (num attempted and average)
            pass
        else:
            print("Goodbye!")
            app_running = False
        

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()