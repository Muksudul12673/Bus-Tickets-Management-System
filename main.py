

class bustickets:

    def __init__(self, rt='', s=0, r=0, a=200, name='', paddress='', daddress='', phone='', gender='', sno=1):

        print("\n\n*****WELCOME TO Bus Tickets Management System*****\n")

        self.rt = rt
        self.r = r
        self.s = s
        self.a = a
        self.name = name
        self.paddress = paddress
        self.daddress = daddress
        self.phone = phone
        self.gender = gender
        self.sno = sno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.paddress = input("\nEnter your Pickup Address:")
        self.daddress = input("\nEnter your Dropping Address:")
        self.phone = input("\nEnter your Phone NO:")
        self.gender = input("\nEnter your Gender:")
        print("\nYour Seat No is:", self.sno, "\n")

    def seatrent(self):

        print("We have the following seat for you:-")

        print("1.  Sleeping Coach----> 1800/- Tk")

        print("2.  Business Class A/C----> 1500/- Tk.")

        print("3.  Business Class Non-A/C----> 1200/- Tk.")

        print("4.  Economy Class Normal Seat ----> 800/- Tk.")

        x = int(input("Enter Your Choice Please->"))

        n = int(input("How many seat did you want to buy:"))

        if (x == 1):

            print("You have to pay for Sleeping Coach:")

            self.s = 1800 * n

        elif (x == 2):

            print("You have to pay for Business Class A/C:")

            self.s = 1500 * n

        elif (x == 3):

            print("You have to pay for Business Class Non-A/C:")

            self.s = 1200 * n

        elif (x == 4):
            print("You have to pay for Economy Class:")

            self.s = 800 * n

        else:

            print("please choose a seat.")

        print(self.s, "Tk.")

    def foodbill(self):

        print("*****FOOD MENU*****")

        print("\n1.Water bottle (500ml)----->Tk. 20/-", "\n2.Tea (1 cup)----->Tk. 10/-", "\n3.Breakfast--->Tk. 90/-",
              "\n4.Lunch---->Tk.150/-", "\n5.Dinner--->Tk. 220/-", "\n6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("How many do you want to order:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("How many do you want to order:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("How many do you want to order:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("How many do you want to order:"))
                self.r = self.r + 150 * d

            elif (c == 5):
                d = int(input("How many do you want to order:"))
                self.r = self.r + 220 * d

            elif (c == 6):
                break
            else:
                print("Invalid option")

        print("Total food Cost=TK.", self.r, "\n")

    def display(self):
        print("******BILL FOR PURCHASE TICKETS******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer Pickup Address:", self.paddress)
        print("Customer Dropping Address:", self.daddress)
        print("Customer Phone No:", self.phone)
        print("Customer Gender:", self.gender)
        print("Seat No.", self.sno)
        print("Your Tickets Seat Cost is:,", "TK.", self.s)
        print("Your Food bill is:", "TK.", self.r)

        self.rt = self.s + self.r

        print("Your Sub total bill is:", "TK.", self.rt)
        print("Additional Service Charges is", "TK.", self.a)
        print("Your grandtotal bill is:", "TK.", self.rt + self.a, "\n")
        print("\n******Thank you Sir******\n")
        print("\n***Have A Safe Journey.***\n ")
        self.sno += 1


def main():
    a = bustickets()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate Tickets Cost")

        print("3.Calculate Foods Bill")

        print("4.Show Total Cost")

        print("5.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.seatrent()

        if (b == 3):
            a.foodbill()

        if (b == 4):
            a.display()

        if (b == 5):
            quit()


main()

