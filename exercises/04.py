# We have 100 cars
cars = 100
# Each car has 4 sits
space_in_a_car = 4.0
# There are 30 available drivers
drivers = 30
# There are 90 passengers
passengers = 90
# The number of not driven cars can be calculated by subtracting the number of drivers from
# the existing cars
cars_not_driven = cars - drivers
# The number of driven cars is equal to the number of existing drivers
cars_driven = drivers
# The carpool capacity is equal to the number of driven cars multiplied by the available sits
# in each car
carpool_capacity = cars_driven * space_in_a_car
# The average number of passengers per car equals the number of drivers divided by the driven cars
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Extra credit error
# average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined

# Explanation:
# The variable car_pool_capacity has not be initialised in the scope of this script
# so the script does not know how to calculate it

