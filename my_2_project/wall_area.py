import math

# Wall Paint Calculator

length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
height = float(input("Enter room height: "))

# Wall area = 2(L×H) + 2(W×H)
wall_area = 2 * (length * height) + 2 * (width * height)

paint_coverage = 10
cans_needed = math.ceil(wall_area / paint_coverage)

print("Total wall area:", wall_area)
print("Paint cans needed:", cans_needed)