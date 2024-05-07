import unittest
from TravelManagementSystem import TravelManagementSystem, Trip, Traveler

class TestTravelManagementSystem(unittest.TestCase):

    def test_create_trip(self):
        # Arrange
        tms = TravelManagementSystem()
        name = "City Tour"
        start_date = datetime.datetime(2024, 9, 1)
        duration = 4
        coordinator = "David Kim"
        contact_info = "david.kim@email.com"

        # Act
        trip = tms.create_trip(name, start_date, duration, coordinator, contact_info)

        # Assert
        self.assertIsInstance(trip, Trip)  # Check if returned object is a Trip instance
        self.assertEqual(trip.name, name)
        self.assertEqual(trip.start_date, start_date)
        self.assertEqual(trip.duration, duration)
        self.assertEqual(trip.coordinator, coordinator)
        self.assertEqual(trip.contact_info, contact_info)

    def test_add_passenger_to_trip(self):
        # Arrange
        tms = TravelManagementSystem()
        trip = tms.create_trip("Island Getaway", datetime.datetime(2024, 10, 15), 10, "Emily Jones", "emily.jones@email.com")
        traveler_name = "William Miller"
        traveler_address = "456 Elm St"
        # ... (other traveler details)

        # Act
        tms.add_passenger_to_trip(trip, traveler_name, traveler_address, ...)  # Assuming you create a Traveler object

        # Assert (check if traveler is added to the trip.passengers list)
        self.assertIn(traveler_name, [p.name for p in trip.passengers
