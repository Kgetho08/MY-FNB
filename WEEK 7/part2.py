num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")