Bike Rental Shop Application

Overview

Welcome to the Bike Rental Shop Application! 
This project is a console-based application developed in Python to manage bike rentals for a bike shop.

Objectives
- Initial Setup: Gather input to set up the bike shop and its inventory of different bike types.
- Customer Rentals: Allow customers to rent bikes and process rental returns.
- Continuous Operation: Ensure the application runs continuously throughout the day.
- Navigational Menu: Provide a menu for navigation with options for new customer rentals, rental returns, showing inventory, 		ending the day, and exiting the program.
  
Functional Requirements

1. Application Startup:
   - Collect input to establish the bike shop and inventory.
     
2. Navigational Menu Options:
   
   A. New Customer Rental:
   - Gather customer information (name and ID).
	 - Collect details on the type of bike to rent, rental duration, number of bikes, and discount coupons.
	 - Verify inventory and complete the rental.
     
   B. Rental Return:   
	- Display an invoice with:
	- Customer name.
	- Type and number of bikes rented.
	- Rental duration.
	- Total before discount.
	- Applicable discount.
	- Final total.
   - Return bikes to the inventory.
   	  
   	C. Show Inventory
    - Display available inventory of:
		- Mountain bikes
		- Touring bikes
		- Road bikes

		D. End of Day
		- Show the total number of bikes rented and daily revenue collected.

		E. Exit Program
		- End the application.
      
3. Continuous Operation:
- After completing any transaction (1-4), return to the navigational menu.
- Option 5 ends the program.
