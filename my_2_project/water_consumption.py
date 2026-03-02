import math

# Water Consumption Calculator

people = int(input("Enter number of people: "))

daily_per_person = float(input("Enter daily water consumption per person (liters): "))
gallon_capacity = float(input("Enter gallon capacity (liters): "))
gallon_price = float(input("Enter price per gallon: "))

weekly_water = people * daily_per_person * 7
gallons_needed = math.ceil(weekly_water / gallon_capacity)
total_budget = gallons_needed * gallon_price

print("Weekly water needed:", weekly_water)
print("Gallons to buy:", gallons_needed)
print("Total budget:", total_budget)