class TripManagement:
    def __init__(self):
        self.trips = []

    def create_trip(self, name, start_date, duration, coordinator, contact_info):
        trip = Trigip(name, start_date, duration, coordinator, contact_info)
        self.trips.append(trip)
        return trip

    def view_trips(self):
        print("All Trips:")
        for index, trip in enumerate(self.trips, start=1):
            print(f"Trip {index}:")
            trip.display_trip_details()
            print()

    # Implement methods for updating and deleting trips
