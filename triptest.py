import unittest
from triptest import Trip

class TestTrip(unittest.TestCase):

    def test_create_trip(self):
        # Arrange
        name = "Summer Adventure"
        start_date = datetime.datetime(2024, 7, 15)
        duration = 7
        coordinator = "John Smith"
        contact_info = "john.smith@email.com"

        # Act
        trip = Trip(name, start_date, duration, coordinator, contact_info)

        # Assert
        self.assertEqual(trip.name, name)
        self.assertEqual(trip.start_date, start_date)
        self.assertEqual(trip.duration, duration)
        self.assertEqual(trip.coordinator, coordinator)
        self.assertEqual(trip.contact_info, contact_info)

    def test_add_passenger(self):
        # Arrange
        trip = Trip("Weekend Getaway", datetime.datetime(2024, 5, 10), 2, "Jane Doe", "jane.doe@email.com")
        traveler_name = "Alice Jones"
        traveler_address = "123 Main St"
        # ... (other traveler details)

        # Act
        trip.add_passenger(traveler_name, traveler_address, ...)  # Assuming you create a Traveler object

        # Assert (check if traveler is added to the trip.passengers list)
        self.assertIn(traveler_name, [p.name for p in trip.passengers])  # Example assertion using list comprehension

    def test_get_start_date(self):
        # Arrange
        trip = Trip("Mountain Hike", datetime.datetime(2024, 6, 1), 5, "Mike Brown", "mike.brown@email.com")

        # Act
        start_date = trip.get_start_date()

        # Assert
        self.assertEqual(start_date, datetime.datetime(2024, 6, 1))

    def test_get_end_date(self):
        # Arrange
        trip = Trip("Beach Trip", datetime.datetime(2024, 8, 10), 3, "Sarah Lee", "sarah.lee@email.com")

        # Act
        end_date = trip.get_end_date()

        # Assert
        self.assertEqual(end_date, datetime.datetime(2024, 8, 13))  # Considering duration is 3 days
