class TicketSystem:
    def __init__(self):
        self.tickets_available = 100

    def display_menu(self):
        print("Welcome to the Ticket System")
        print("1. View Available Tickets")
        print("2. Purchase Tickets")
        print("3. Exit")

    def view_available_tickets(self):
        print(f"Tickets Available: {self.tickets_available}")

    def purchase_tickets(self, quantity):
        if self.tickets_available >= quantity:
            self.tickets_available -= quantity
            print(f"Successfully purchased {quantity} tickets.")
        else:
            print("Sorry, insufficient tickets available.")

# Main program loop
ticket_system = TicketSystem()

while True:
    ticket_system.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        ticket_system.view_available_tickets()
    elif choice == '2':
        quantity = int(input("Enter the number of tickets to purchase: "))
        ticket_system.purchase_tickets(quantity)
    elif choice == '3':
        print("Thank you for using the Ticket System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")