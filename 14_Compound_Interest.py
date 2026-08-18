# Compound Interest: Calculate compound interest using arithmetic operators and exponentiation ($A = P(1 + r/n)^{nt}$).

# Compound Interest

P = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
n = int(input("Enter number of times interest is compounded per year: "))
t = float(input("Enter time in years: "))

r = r / 100
A = P * (1 + r / n) ** (n * t)
CI = A - P

print("Compound Interest =", CI)
print("Total Amount =", A)