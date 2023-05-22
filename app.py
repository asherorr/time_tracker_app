from models import (Base, session, Tracker, engine)
import time
import statistics
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
        \r3) Delete all entries
        ''')
        choice = input("What would you like to do? ")
        if choice in ["1", "2", "3"]:
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
            try:
                list_of_times = []
                for entry in session.query(Tracker).all():
                    entry = entry.time_spent
                    list_of_times.append(entry)
                average_of_times = mean(list_of_times)
            except mean.StatisticsError:
                raise mean.StatisticsError("Oh no! There are no entries in the database.")
            else:
                print(f'This is the average time spent: {average_of_times} minutes')
                time.sleep(2)
        elif choice == "3":
            for entry in session.query(Tracker).all():
                session.delete(entry)
                session.commit()
            print("All the previous entries have been deleted.")
            time.sleep(1.5)
        else:
            print("Goodbye!")
            app_running = False
        

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()