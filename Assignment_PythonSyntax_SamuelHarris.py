#Assignment: Python Syntax (Samuel Harris)

# Q1

# Task 1

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

# Task 2

mood = input("How do you feel today? ")

if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")


# Q2 - Task 1

PI_VALUE = 3.14  # Renamed to adhere to constant naming convention
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

# Q3 - Task 1

variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True

print(type(variable_a))  # <class 'str'>
print(type(variable_b))  # <class 'int'>
print(type(variable_c))  # <class 'float'>
print(type(variable_d))  # <class 'bool'>


# Q4

# Task 1

bread_price = 1.5
peanut_butter_price = 2.75
jelly_price = 3.25

total_cost = bread_price + peanut_butter_price + jelly_price
print("Total cost:", total_cost)  # Total cost: 7.5

# Task 2

initial_amount = 10000
interest_rate = 0.07

amount_after_year = initial_amount * (1 + interest_rate)
print("Amount after a year:", amount_after_year)  # Amount after a year: 10700.0


# Q5 - Task 1

a = 5
b = 10

# Swap variables using tuple unpacking
a, b = b, a

print("a:", a)  # a: 10
print("b:", b)  # b: 5

# Q6

# Task 1

expression1 = 5 + 3 * 2
expression2 = (5 + 3) * 2

print("Without parentheses:", expression1)  # Without parentheses: 11
print("With parentheses:", expression2)     # With parentheses: 16


# Task 2

result = (5 + 3) > 2 or 4 * 2 > 10
print("Result:", result)  # Prediction: True
# Computed: True