class TourGuideSystem:
    def __init__(self, locations):
        self.locations = locations
        self.feedback = {}

    def display_locations(self):
        print("\nAvailable Tourist Locations:")
        for idx, location in enumerate(self.locations, 1):
            print(f"{idx}. {location['name']}")

    def provide_location_info(self, location_number):
        if 1 <= location_number <= len(self.locations):
            location = self.locations[location_number - 1]
            print(f"\nLocation: {location['name']}")
            print(f"Description: {location['description']}")
            print(f"Entry Fee: {location['entry_fee']} USD")
            print(f"Timings: {location['timings']}")
        else:
            print("\nInvalid location number.")

    def collect_feedback(self, location_number, user_feedback):
        if 1 <= location_number <= len(self.locations):
            location_name = self.locations[location_number - 1]['name']
            if location_name not in self.feedback:
                self.feedback[location_name] = []
            self.feedback[location_name].append(user_feedback)
            print(f"\nThank you for your feedback on {location_name}!")
        else:
            print("\nInvalid location number.")

    def show_feedback(self, location_number):
        if 1 <= location_number <= len(self.locations):
            location_name = self.locations[location_number - 1]['name']
            print(f"\nFeedback for {location_name}:")
            if location_name in self.feedback and self.feedback[location_name]:
                for fb in self.feedback[location_name]:
                    print(f"- {fb}")
            else:
                print(f"No feedback available for {location_name} yet.")
        else:
            print("\nInvalid location number.")

class Tourist:
    def give_feedback(self):
        print("\nEnter your feedback: ")
        return input()

if __name__ == "__main__":
    # Predefined tourist locations with details
    locations = [
        {'name': 'Eiffel Tower', 'description': 'An iconic symbol of Paris, the Eiffel Tower offers breathtaking views of the city.', 'entry_fee': 25, 'timings': '9 AM - 12 AM'},
        {'name': 'Great Wall of China', 'description': 'A magnificent structure and one of the wonders of the world, stretching across northern China.', 'entry_fee': 10, 'timings': '8 AM - 6 PM'},
        {'name': 'Taj Mahal', 'description': 'A stunning white marble mausoleum, symbolizing love and beauty in Agra, India.', 'entry_fee': 15, 'timings': '6 AM - 7 PM'}
    ]

    guide_system = TourGuideSystem(locations)
    tourist = Tourist()

    while True:
        print("\n\n==== Tour Guide System Menu ====")
        print("1. Display available locations")
        print("2. Get information about a location")
        print("3. Give feedback for a location")
        print("4. Show feedback for a location")
        print("5. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            guide_system.display_locations()

        elif choice == 2:
            guide_system.display_locations()
            loc_number = int(input("\nEnter the location number to get more information: "))
            guide_system.provide_location_info(loc_number)

        elif choice == 3:
            guide_system.display_locations()
            loc_number = int(input("\nEnter the location number to give feedback: "))
            feedback = tourist.give_feedback()
            guide_system.collect_feedback(loc_number, feedback)

        elif choice == 4:
            guide_system.display_locations()
            loc_number = int(input("\nEnter the location number to view feedback: "))
            guide_system.show_feedback(loc_number)

        elif choice == 5:
            print("\nThank you for using the Tour Guide System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Project Summary: Tour Guide System
# The Tour Guide System is a Python-based application designed to assist users in exploring tourist locations. It provides information about various attractions, allows users to give and view feedback, and manages location details.

# Components:
# TourGuideSystem Class:

# Attributes:
# locations: A list of dictionaries, each containing details about a tourist location (name, description, entry fee, timings).
# feedback: A dictionary to store feedback for each location.
# Methods:
# display_locations(): Lists all available tourist locations with their names.
# provide_location_info(location_number): Provides detailed information about a selected location, such as description, entry fee, and timings.
# collect_feedback(location_number, user_feedback): Collects feedback from users about a location and stores it.
# show_feedback(location_number): Displays feedback left by users for a specific location.
# Tourist Class:

# Methods:
# give_feedback(): Prompts the user to enter their feedback for a location.
# Main Program:

# Menu Options:
# Display available locations: Shows all tourist spots.
# Get information about a location: Provides details for a selected location.
# Give feedback for a location: Allows users to submit feedback.
# Show feedback for a location: Displays feedback for a selected location.
# Exit: Exits the program.
# Example Workflow:
# Display Locations: Users can view a list of all tourist locations.
# Get Location Information: Users select a location to see detailed information, including description, entry fee, and operational timings.
# Give Feedback: Users provide feedback for a location they have visited.
# Show Feedback: Users can view feedback given by others for a specific location.
# This project demonstrates key concepts in object-oriented programming, such as encapsulation (data and methods are bundled into classes), and provides a practical application for managing and interacting with data in a user-friendly manner.










