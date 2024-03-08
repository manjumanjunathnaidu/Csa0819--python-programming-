def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150001) * 0.1
    elif income <= 500000:
        return (300000 - 150001) * 0.1 + (income - 300001) * 0.2
    else:
        return (300000 - 150001) * 0.1 + (500000 - 300001) * 0.2 + (income - 500001) * 0.3

# Example usage
income = float(input("Enter your income: "))
tax = calculate_tax(income)
print(f"Your tax is: {tax:.2f}")
