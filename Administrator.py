from TripManager import TripManager


class Administrator(TripManager):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.trip_managers = []

    def add_trip_manager(self, trip_manager):
        self.trip_managers.append(trip_manager)

    def view_payment_receipt(self, trip):
        print(f"Payment receipt for trip '{trip.name}': Payment received

