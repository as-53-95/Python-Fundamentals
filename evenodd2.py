num1 = int(input("Enter Number:"))
last_digit = num1 % 10

if last_digit == 0 or 2 or 4 or 6 or 8:
    print(num1, "is even")

