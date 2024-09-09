# Task 1: Vehicle Registration System

# Define the Vehicle class
class Vehicle:
    def __init__(self, reg_num, type, owner):
        # Initialize the attributes of the Vehicle class
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        # Method to update the owner of the vehicle
        self.owner = new_owner

# Function to display the vehicle menu
def vehicle_menu():
    vehicles = {}
    while True:
        print("\nVehicle Menu:")
        print("1. Add Vehicle")
        print("2. Update Vehicle Owner")
        print("3. Display Vehicle Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            reg_num = input("Enter registration number: ")
            type = input("Enter vehicle type: ")
            owner = input("Enter owner name: ")
            vehicles[reg_num] = Vehicle(reg_num, type, owner)
            print("Vehicle added successfully!")

        elif choice == "2":
            reg_num = input("Enter registration number: ")
            if reg_num in vehicles:
                new_owner = input("Enter new owner name: ")
                vehicles[reg_num].update_owner(new_owner)
                print("Owner updated successfully!")
            else:
                print("Vehicle not found!")

        elif choice == "3":
            reg_num = input("Enter registration number: ")
            if reg_num in vehicles:
                vehicle = vehicles[reg_num]
                print(f"Vehicle {reg_num} details: Type: {vehicle.type}, Owner: {vehicle.owner}")
            else:
                print("Vehicle not found!")

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")


# Task 2: Event Management System Enhancement

# Define the Event class
class Event:
    def __init__(self, name, date):
        # Initialize the attributes of the Event class
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        # Method to add a participant
        self.participant_count += 1

    def get_participant_count(self):
        # Method to get the current participant count
        return self.participant_count

    @staticmethod
    def add_event(events):
        # Static method to add a new event
        name = input("Enter event name: ")
        date = input("Enter event date (MM/DD/YYYY): ")
        events[name] = Event(name, date)
        print("Event added successfully!")

# Function to display the event menu
def event_menu():
    events = {}
    while True:
        print("\nEvent Menu:")
        print("1. Add Event")
        print("2. Add Participant")
        print("3. Display Participant Count")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Event.add_event(events)

        elif choice == "2":
            event_name = input("Enter event name: ")
            if event_name in events:
                events[event_name].add_participant()
                print("Participant added successfully!")
            else:
                print("Event not found!")

        elif choice == "3":
            event_name = input("Enter event name: ")
            if event_name in events:
                print(f"Current participant count for {event_name}: {events[event_name].get_participant_count()}")
            else:
                print("Event not found!")

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")

# Main menu to choose between vehicle and event management
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Vehicle Management")
        print("2. Event Management")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_menu()

        elif choice == "2":
            event_menu()

        elif choice == "3":
            break

        else:
            print("Invalid choice! Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
