# Your code below:

#Toppings list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Prices list
prices = [2, 6, 1, 3, 2, 7, 2]

#Number of occurences of 2
num_two_dollar_slices = prices.count(2)

#Number of toppings
num_pizzas = len(toppings)

#We sell pizzas message
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Combine toppings and prices
pizza_and_prices = []
for x in range(len(toppings)):
    tmpArray = [prices[x], toppings[x]]
    pizza_and_prices.append(tmpArray)

#Sort pizzas and prices
pizza_and_prices.sort()

#Save the cheapest pizza
cheapest_pizza = pizza_and_prices[0]

#Save the most expensive pizza
priciest_pizza = pizza_and_prices[-1]

#Remove anchovies pizza
pizza_and_prices.pop()

#Add new topping option and resort the array
new_topping = [2.5, "peppers"]
pizza_and_prices.append(new_topping)
pizza_and_prices.sort()

#Three cheapest pizzas
three_cheapest = pizza_and_prices[:3]

#Display the three cheapest pizzas
print(three_cheapest)
