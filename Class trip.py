class Trip:
    def __init__(self, name, start_date, duration, coordinator, contact_info):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.coordinator = coordinator
        self.contact_info = contact_info
        self.trip_legs = []
        self.passengers = []
