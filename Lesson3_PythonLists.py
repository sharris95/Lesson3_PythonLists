#Lesson3_PythonLists

# 1. Python List Transformation

# Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades_sorted = sorted(grades, reverse=True)
print("Sorted grades in descending order:", grades_sorted)

# Task 2
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# 2. Advanced List Methods and Identity Operators

# Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and attended the class.")
else:
    print("Alice did not submit the assignment and/or attend the class.")

# 3. Advanced Slicing Techniques

# Task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:", second_week_temperatures)

# Task 2
temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", temperatures_above_100)
