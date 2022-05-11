weight = 1.5
premium_ground_shipping = 125;

print("Normal shipping")

#less than 3
if (weight <= 2):
  print((weight * 1.5) + 20)

#Between 3 and 6
elif (weight > 2 and weight <= 6):
  print((weight * 3) + 20)

#Between 7 and 10
elif (weight > 6 and weight <= 10):
  print((weight * 4) + 20)

#11 and over
elif (weight > 10):
  print((weight * 4.75) + 20)

print("\nDrone shipping")

#less than 3
if (weight <= 2):
  print((weight * 4.5))

#Between 3 and 6
elif (weight > 2 and weight <= 6):
  print((weight * 9))

#Between 7 and 10
elif (weight > 6 and weight <= 10):
  print((weight * 12))

#11 and over
elif (weight > 10):
  print((weight * 14.25))