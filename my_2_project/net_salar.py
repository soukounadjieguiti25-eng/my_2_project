# Net Salary Calculator

base_salary = float(input("Enter base salary: "))
allowance = float(input("Enter allowance: "))

bpjs_rate = float(input("Enter BPJS rate: "))
tax_rate = float(input("Enter tax rate: "))

gross_salary = base_salary + allowance
total_deductions = gross_salary * (bpjs_rate + tax_rate)

net_salary = gross_salary - total_deductions

print("Net salary:", net_salary)