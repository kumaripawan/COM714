import datetime


class Trip:
    def __init__(self, name, start_date, duration, coordinator, contact_info):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.coordinator = coordinator
        self.contact_info = contact_info
        self.trip_legs = []
        self.passengers = []

    def add_passenger(self, traveler):
        self.passengers.append(traveler)

    def add_trip_leg(self, trip_leg):
        self.trip_legs.append(trip_leg)

    def display_trip_details(self):
        print("Trip:", self.name)
        print("Start Date:", self.start_date.strftime("%d/%m/%Y"))
        print("Duration:", self.duration, "days")
        print("Coordinator:", self.coordinator)
        print("Contact Info:", self.contact_info)
        print("Passengers:")
        for passenger in self.passengers:
            print("\t", passenger)
        print("Trip Legs:")
        for leg in self.trip_legs:
            print("\t", leg)

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.start_date + datetime.timedelta(days=self.duration)
