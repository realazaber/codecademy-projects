train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#Farenheit to Calsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#Calsius to Farenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Calculate Force
def get_force(mass, acceleration):
  return mass * acceleration

#Calculate Energy
def get_energy(mass, c = 3*10**8):
  return mass * c**2

#Calculate Work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

#Convert 100 farenheit to celsius
f100_in_celsius = f_to_c(100)

#Convert 0 celsius to farenheit 
c0_in_fahrenheit = c_to_f(0)

#Get the train's force
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Get the bomb's energy
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

#Get the train's work
train_work = get_work(train_mass, train_acceleration, train_distance)


#Print the final string
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")

