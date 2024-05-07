from Trip import Trip
from Traveler import Traveler
from TripLeg import TripLeg
from TripCoordinator import TripCoordinator
from TripManager import TripManager
from Administrator import Administrator
from ReportingAndAnalytics import ReportingAndAnalytics


class TravelManagementSystem:
    def __init__(self):
        self.trips = []
        self.trip_coordinators = []
        self.trip_managers = []
        self.administrators = []

    def create_trip(self, name, start_date, duration, coordinator, contact_info):
        trip = Trip(name, start_date, duration, coordinator, contact_info)
        self.trips.append(trip)
        return trip

    def create_traveler(self, name, address, dob, emergency_contact, government_id):
        return Traveler(name, address, dob, emergency_contact, government_id)

    def add_passenger_to_trip(self, trip, traveler):
        trip.add_passenger(traveler)
        print(f"{traveler.name} added to trip {trip.name}")

    def add_trip_leg_to_trip(self, trip, trip_leg):
        trip.add_trip_leg(trip_leg)
        print(f"Trip leg added to trip {trip.name}")

    def create_trip_coordinator(self, name, contact_info):
        coordinator = TripCoordinator(name, contact_info)
        self.trip_coordinators.append(coordinator)
        return coordinator

    def create_trip_manager(self, name, contact_info):
        manager = TripManager(name, contact_info)
        self.trip_managers.append(manager)
        return manager

    def create_administrator(self, name, contact_info):
        admin = Administrator(name, contact_info)
        self.administrators.append(admin)
        return admin

    def display_all_trips(self):
        print("All Trips:")
        for index, trip in enumerate(self.trips, start=1):
            print(f"Trip {index}:")
            trip.display_trip_details()
            print()

    # Implement other functionalities such as updating and deleting trips, travelers, trip coordinators, etc.

