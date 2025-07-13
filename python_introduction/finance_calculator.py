monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your monthly expenses: "))

monthlySavings = monthlyIncome - monthlyExpenses

annualSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print(f"Your annual savings, including interest, is: {annualSavings}")
                          