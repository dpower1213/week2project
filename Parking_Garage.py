global tickets
tickets=[]
global i
i=1
global parkingspaces
parkingspaces=10
currentticket=dict()

class Parking_Garage:
    def __init__(self,tickets,parkingspaces,currentticket):
        self.tickets=tickets
        self.parkingspaces=parkingspaces
        self.currentticket=currentticket
        
    def take_ticket(tickets):
        global i
        global parkingspaces
        print('\n' * 4)
        entry=input("Please press 1 to enter the garage:\n")
        if entry == "1":
            if parkingspaces <1:
                print("Parking Garage is full!!\n")
            else:
                tickets.append(i)
                currentticket[i]=150
                i=i+1
                parkingspaces = parkingspaces - 1
                print('Parking Spaces Left:\n', parkingspaces)
                print('Ticket Number:\n', tickets)
                print('Open Tickets {ticket number : amount} :  \n', currentticket)
                exit=""
                exit=input("Would you like to exit and pay your ticket? 'y' for yes:\n")
                if exit=="y":
                    Parking_Garage.pay_for_parking(currentticket)
        
        Parking_Garage.take_ticket(tickets)

    def pay_for_parking(currentticket):
        payus=input("Enter your ticket number:\n")
        print('Open Tickets:\n',currentticket)
        print('Ticket #:\n')
        print('Number of Tickets:\n',tickets)
        print(i)
        a=0
        a=i-1
        print(a)
        pay=""
        payus=int(payus)
        print("For ticket #: {} you owe us: ${} pay up or we sell you to Putin!!\n".format(payus,currentticket[a]))
        pay=input("How much are you paying?:\n")        
        currentticket[payus] = currentticket[payus]-int(pay)              
        print('Open Tickets:\n',currentticket)
        print('Number of Tickets:\n',tickets)
        print('Your ticket has been paid and you have 15mins to leave\n')
        print("Thank You, have a nice day\n")
    
    def leave_garage(self):
        pass
        
Parking_Garage.take_ticket(tickets)
