class TripCoordinator:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.managed_trips = []

    def manage_trip(self, trip):
        self.managed_trips.append(trip)

    # Other methods for managing passengers, updating trip legs, generating trip itineraries, handling payments, and generating receipts
