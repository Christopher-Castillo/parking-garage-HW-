class ParkingGarage:
    def __init__(self):
        self.tickets = [1, 2, 3]
        self.parkingSpaces = [1, 2, 3]
        self.currentTicket = {"paid":False}

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        print("Ticket taken, please pay for parking.")

    def payForParking(self):
        payment = input("Enter the payment amount: ")
        if payment:
            self.currentTicket["paid"] = True
            print("Your ticket has been paid. You have 15 minutes to leave the garage.")

    def leaveGarage(self):
        if self.currentTicket["paid"] == True:
            print("Thank you, have a nice day!")
            self.parkingSpaces.append(1)
            self.tickets.append(1)
        else:
            payment = input("Please enter the payment amount: ")
            if payment:
                self.currentTicket["paid"] = True
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(1)
                self.tickets.append(1)
#Creating the object of class ParkingGarage
garage = ParkingGarage()
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()