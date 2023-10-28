basic_salary = float(input("Enter the basic salary: "))

HRA = 0.2 * basic_salary
TA = 0.05 * basic_salary
DA = 0.1 * basic_salary

gross_salary = basic_salary + HRA + TA + DA

if gross_salary < 300000:
    income_tax = 0
elif 300000 <= gross_salary < 1000000:
    income_tax = 0.1 * gross_salary
elif 1000000 <= gross_salary < 2500000:
    income_tax = 0.2 * gross_salary
else:
    income_tax = 0.3 * gross_salary

print("\nGross Salary:", gross_salary)
print("Income Tax:", income_tax)
