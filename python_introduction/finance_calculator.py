income = int (input("Enter your monthly income: "))
expense = int (input("Enter your total monthly expense: "))

savings = income - expense

anual_savings = savings * 12 + (savings * 12 * 0.05)

print(f"your monthly savings are ${savings}.")
print(f"projected savings after one year, with interest, is: ${anual_savings}.")
