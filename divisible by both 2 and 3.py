def is_divisible_by_2_and_3(number):
    if number % 6 == 0:
        return true
    else:
        return false
try:
    number = int(input("enter a number: "))
    if is_divisible_by_2_and_3(number):
        print(f"{number} is divisible by both 2 and 3.")
    else:
        print(f"{number} is not divisible by both 2 and 3.")
except valueError:
    print("please enter a valid integer.")
