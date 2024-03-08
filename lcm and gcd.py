def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage:
num1 = 12
num2 = 18

result_gcd = gcd(num1, num2)
result_lcm = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {result_gcd}")
print(f"LCM of {num1} and {num2} is: {result_lcm}")
