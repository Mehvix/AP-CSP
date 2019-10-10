import math

people = int(input("How many people are going?\n"))

buses = math.ceil(people/25)
cost = buses * 6.25
avg = people/buses

print("You need:\t\t\t\t{} buses\nWhich will cost:\t\t${}\nAvg. Students per Bus:\t{}".format(buses, cost, avg))
