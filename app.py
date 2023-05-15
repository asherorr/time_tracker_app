from models import (Base, session, Tracker, engine)
import time
from statistics import mean

def average(list_obj):
    return mean(list_obj)

def menu():
    while True:
        print('''
        \rOPTIONS
        \r----
        \r1) Add Event
        \r2) See Statistics
        ''')
        choice = input("What would you like to do? ")
        if choice in ["1", "2"]:
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
            time_spent = input("How much time did you spend, in minutes? ")
            entry_added = Tracker(time_spent=time_spent)
            session.add(entry_added)
            session.commit()
            print("Entry added!")
            time.sleep(1.5)
        elif choice == "2":
            #all_times = session.query(Tracker).all
            average_of_times = average(all_times)
            print(average_of_times)
        else:
            print("Goodbye!")
            app_running = False
        

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()