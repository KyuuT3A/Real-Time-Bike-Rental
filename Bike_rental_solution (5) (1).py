import datetime
from datetime import datetime, timedelta

class BikeRental:
    
    def __init__(self, stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock 
        self.revenue = 0
        self.bikes_rented_today = 0
        self.mountain_bikes = stock // 3  
        self.touring_bikes = stock // 3   
        self.road_bikes = stock - self.mountain_bikes - self.touring_bikes


    def display_stock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("Inventory:")
        print("Mountain Bikes:", self.mountain_bikes)
        print("Touring Bikes:", self.touring_bikes)
        print("Road Bikes:", self.road_bikes)
        return self.stock

    def rent_bike_on_hourly_basis(self, n, bike_type):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
       
        elif bike_type == 'Mountain' and n > self.mountain_bikes:
            print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain_bikes))
            return None
        elif bike_type == 'Touring' and n > self.touring_bikes:
            print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring_bikes))
            return None
        elif bike_type == 'Road' and n > self.road_bikes:
            print("Sorry! We have currently {} road bikes available to rent.".format(self.road_bikes))
            return None
        else:
            now = datetime.now()
            print("You have rented {} {} bike(s) on hourly basis today at {} hours.".format(n, bike_type, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.bikes_rented_today += n
            if bike_type == 'Mountain':
                self.mountain_bikes -= n
            elif bike_type == 'Touring':
                self.touring_bikes -= n
            elif bike_type == 'Road':
                self.road_bikes -= n
            return now
     
    def rent_bike_on_daily_basis(self, n, bike_type):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        elif bike_type == 'Mountain' and n > self.mountain_bikes:
            print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain_bikes))
            return None
        elif bike_type == 'Touring' and n > self.touring_bikes:
            print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring_bikes))
            return None
        elif bike_type == 'Road' and n > self.road_bikes:
            print("Sorry! We have currently {} road bikes available to rent.".format(self.road_bikes))
            return None
        else:
            now = datetime.now()                      
            print("You have rented {} {} bike(s) on daily basis today at {} hours.".format(n, bike_type, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.bikes_rented_today += n
            if bike_type == 'Mountain':
                self.mountain_bikes -= n
            elif bike_type == 'Touring':
                self.touring_bikes -= n
            elif bike_type == 'Road':
                self.road_bikes -= n
            return now
        
    def rent_bike_on_weekly_basis(self, n, bike_type):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        elif bike_type == 'Mountain' and n > self.mountain_bikes:
            print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain_bikes))
            return None
        elif bike_type == 'Touring' and n > self.touring_bikes:
            print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring_bikes))
            return None
        elif bike_type == 'Road' and n > self.road_bikes:
            print("Sorry! We have currently {} road bikes available to rent.".format(self.road_bikes))
            return None
        else:
            now = datetime.now()
            print("You have rented {} {} bike(s) on weekly basis today at {} hours.".format(n, bike_type, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.bikes_rented_today += n
            if bike_type == 'Mountain':
                self.mountain_bikes -= n
            elif bike_type == 'Touring':
                self.touring_bikes -= n
            elif bike_type == 'Road':
                self.road_bikes -= n
            return now
    
    def return_bike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replenishes the inventory
        3. Returns a bill
        """
        rental_time, rental_basis, num_of_bikes, bike_type = request
        bill = 0
        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes
        
            self.revenue += bill 
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            if bike_type == 'Mountain':
                self.mountain_bikes += num_of_bikes
            elif bike_type == 'Touring':
                self.touring_bikes += num_of_bikes
            elif bike_type == 'Road':
                self.road_bikes += num_of_bikes
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.name = ""
        self.ID = ""
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = None  
        self.bill = 0
        self.discount_coupon = ""
        self.bike_type = ""

    def provide_info(self):
        """
        Gather information on the customer (name and ID), type of bike to rent,
        length of rental, amount of bikes, and any discount coupons.
        """
        while True:
            self.name = input("Enter your name: ")
            if self.name.isdigit():
                print("Invalid name! Please enter a valid name.")
            else:
                break
        self.ID = input("Enter your ID: ")
        while True:
            try:
                self.rental_basis = int(input("Enter rental basis (1. Hourly, 2. Daily, 3. Weekly): "))
                if self.rental_basis not in [1, 2, 3]:
                    raise ValueError("Invalid rental basis! Please enter 1, 2, or 3.")
                break
            except ValueError as e:
                print(e)
        while True:
            self.bikes = int(input("Enter the number of bikes you want to rent: "))
            if self.bikes > 30:
                print("Sorry, you cannot rent more than 30 bikes at a time.")
            else:
                break
        self.discount_coupon = input("Enter discount coupon code (if any): ")
        while True:
            self.bike_type = input("Enter type of bike (Mountain, Touring, Road): ").capitalize()
            if self.bike_type not in ["Mountain", "Touring", "Road"]:
                print("Invalid bike type! Please enter Mountain, Touring, or Road.")
            else:
                break

    def set_rental_time(self, rental_time):
        """
        Set the rental time when the bike is rented.
        """
        self.rental_time = rental_time

    def return_bike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes, self.bike_type
        else:
            return None, None, None, None

# Function to display invoice
def display_invoice(customer, rental_period, bill, discount):
    """
    Display the invoice for the returned bike.
    """
    print("\n*** Invoice ***")
    print("Name of Customer:", customer.name)
    print("Type and number of bikes rented:", customer.bikes)
    print("Total time of rental:", rental_period)
    print("Total before discount: ${}".format(bill))
    if discount > 0:
        print("Discount: ${}".format(discount))
    final_total = bill - discount
    print("Final total to be collected: ${}".format(final_total))

# Test Logic
def main():
    shop = BikeRental(30)
    customers = []  
    
    while True:
        print("\n*** Welcome to the Bike Rental Shop ***")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")
        print("5. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n*** New Customer Rental ***")
            customer = Customer()
            customer.provide_info()  
            if customer.rental_basis in [1, 2, 3]:
                rental_time = datetime.now()  
                customer.set_rental_time(rental_time)  
                if customer.rental_basis == 1:
                    shop.rent_bike_on_hourly_basis(customer.bikes, customer.bike_type)
                elif customer.rental_basis == 2:
                    shop.rent_bike_on_daily_basis(customer.bikes, customer.bike_type)
                elif customer.rental_basis == 3:
                    shop.rent_bike_on_weekly_basis(customer.bikes, customer.bike_type)
                customers.append((customer, None))  
        
        elif choice == '2':
            print("\n*** Rental Return ***")
            for customer, invoice_details in customers:
                rental_time, rental_basis, bikes, bike_type = customer.return_bike()
                if rental_time:
                    bill = shop.return_bike((rental_time, rental_basis, bikes, bike_type))
                    rental_period = datetime.now() - rental_time
                    discount = 0
                    if customer.bikes >= 3 and customer.bikes <= 5:
                        discount = 0.25 * bill
                    invoice_details = (customer, rental_period, bill, discount) 
                    display_invoice(*invoice_details)  
                    customers.remove((customer, None)) 
        
        elif choice == '3':
            print("\n*** Show Inventory ***")
            shop.display_stock()
        
        elif choice == '4':
            print("\n*** End of Day ***")
            print("End of Day Summary:")
            print("Total bikes rented today:", shop.bikes_rented_today)
            print("Daily Revenue Collected for Day: ${}".format(shop.revenue))
            shop.bikes_rented_today = 0
            shop.revenue = 0
        
        elif choice == '5':
            print("\nExiting the program...")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
