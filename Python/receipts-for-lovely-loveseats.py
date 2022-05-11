#Create Lovely Loveseat description
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
#Create Lovely Loveseat price
lovely_loveseat_price = 254.00

#Create Stylish Settee description
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
#Create Stylish Settee price
stylish_settee_price = 180.50

#Create Luxurious Lamp description
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
#Create Luxurious Lamp price
luxurious_lamp_price = 52.15

#Define sales tax at 8.8%
sales_tax = 0.088

######################################################

#First cumstomer
customer_one_total = 0
customer_one_itemization = ""

#First customer is buying a Lovey Love Seat
customer_one_total += lovely_loveseat_price
customer_one_itemization += "\n" + lovely_loveseat_description

#First customer is buying a Luxurious Lamp Seat
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" + luxurious_lamp_description

#Add tax to customer total
customer_one_tax = (lovely_loveseat_price * sales_tax) + (luxurious_lamp_price * sales_tax)
customer_one_total += customer_one_tax

#Print receipt
print("Customer One Receipt")
print(customer_one_itemization)
print("\n")
print("Customer One Total: " + str(customer_one_total))
