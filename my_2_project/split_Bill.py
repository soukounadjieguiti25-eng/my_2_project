total_bill = float(input("Enter total bill: "))
number_of_people = int(input("Enter number of people: "))
tax_rate = float(input("Enter tax rate: "))

tota_lafter_taxe = total_bill + (total_bill * tax_rate / 100)
payment_per_person = tota_lafter_taxe / number_of_people

print("Total after tax: ", tota_lafter_taxe)
print("Payment per person: ", payment_per_person)