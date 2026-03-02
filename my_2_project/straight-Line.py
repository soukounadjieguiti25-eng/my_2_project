# Straight-Line Depreciation

initial_price = float(input("Enter initial price: "))
salvage_value = float(input("Enter salvage value: "))
economic_life = int(input("Enter economic life (years): "))

annual_depreciation = (initial_price - salvage_value) / economic_life

value_after_2_years = initial_price - (annual_depreciation * 2)

print("Annual depreciation:", annual_depreciation)
print("Value after 2 years:", value_after_2_years)