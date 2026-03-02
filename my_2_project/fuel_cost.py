# Fuel Cost - Dynamic

distance = float(input("Enter travel distance (km): "))
consumption_rate = float(input("Enter fuel consumption rate (liters per 100 km): "))
fuel_price = float(input("Enter fuel price per liter: "))

liters_needed = (distance / 100) * consumption_rate
total_cost = liters_needed * fuel_price

print("Total fuel cost:", total_cost)