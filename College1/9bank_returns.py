interest_rate = 7.1 / 100

monthly_installment = float(input("Enter the monthly installment amount (Rs.): "))
duration_months = int(input("Enter the duration of RD (months): "))

if monthly_installment < 500:
    print("Invalid input: Monthly installment amount should be at least Rs. 500.")
elif duration_months < 6:
    print("Invalid input: RD duration should be at least 6 months.")
else:
    total_returns = 0
    for month in range(duration_months):
        monthly_interest = total_returns * (interest_rate / 12)
        total_returns += monthly_installment + monthly_interest

    print("For an RD of Rs.", monthly_installment, "/- per month for", duration_months,
          "months, the total returns will be Rs.", total_returns, "/-.")
