from TripCoordinator import TripCoordinator


class TripManager(TripCoordinator):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.trip_coordinators = []

    def add_trip_coordinator(self, trip_coordinator):
        self.trip_coordinators.append(trip_coordinator)

    def generate_invoice(self, trip):
        total_cost = sum(leg.cost for leg in trip.trip_legs)
        print(f"Invoice for trip '{trip.name}': Total cost = {total_cost}")

    # Additional methods for managing trip coordinators and generating total invoices for trips
