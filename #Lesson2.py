#Lesson2_SamuelHarris

# Task 1: Code Correction

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# Task 2: Identify the Greatest and Smallest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print(f"The smallest number is {smallest}. The largest number is {largest}.")

# Task 3: Leap Year Checker

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
