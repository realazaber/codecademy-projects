hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Your code

#Initial total
total_price = 0

#Add prices to total
for price in prices:
  total_price = total_price + price

#Create average price
average_price = total_price / len(prices)

#Display average price
print("Average Haircut Price: " + str(average_price))

#5 dollar discount to all prices
new_prices = [price - 5 for price in prices]

#Display new prices
print(new_prices)

#Intitiate total revenue
total_revenue = 0

#Loop over hairstyles
for i in range(len(hairstyles)):
  total_revenue = total_revenue + (prices[i] * last_week[i])

#Output total price
print(total_price)

#Calculate and output average daily revenue
average_daily_revenue = total_revenue / 7

print("Average Revenue: " + str(average_daily_revenue))

#Get all cuts under $30
cuts_under_30 = []
for i in range(len(hairstyles)):
  if prices[i] < 30:
    cuts_under_30.append(hairstyles[i])

#Output cuts under $30
print("\nCuts under 30")
print(cuts_under_30)