import datetime


class Traveler:
    def __init__(self, name, address, dob, emergency_contact, government_id):
        self.name = name
        self.address = address
        self.dob = dob
        self.emergency_contact = emergency_contact
        self.government_id = government_id

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, DOB: {self.dob}, Emergency Contact: {self.emergency_contact}, Govt. ID: {self.government_id}"
