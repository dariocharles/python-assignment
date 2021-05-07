#Python Fundamentals Assignment
print("-------------Python Fundamentals Assignment-------------")

# Part 1: User Input
print("How many courses did you complete?")
courses_input = input("Please enter the number of course complete: ")
num_of_courses = int(courses_input)
#  Testing
"""print(type(num_of_courses))"""

# Declare an empty array and append user input
course_marks = []

i = 1
while (i <= num_of_courses):
    course_marks.append(float(input(f"Enter your mark for course {i}: ")))
    i += 1

# Output the course marks outside the list
for x in course_marks:
    print(x)

# Part 2: Find The Average. 
sum = 0
for i in range(len(course_marks)):
    sum += course_marks[i]
# Testing for the sum
"""print(sum)"""

# Alternative
"""
total = 0
 for mark in course_marks:
     total += mark
"""

average = sum / num_of_courses
print(f"Your average for your {num_of_courses} courses is: {average}")

# Part 3: Output The Letter Grade
if (average >= 90 and average <=100):
    print("Your grade is A+")
elif (average >= 80 and average <=89):
    print("Your grade is B")
elif (average >= 70 and average <=79):
    print("Your grade is C")
elif (average >= 60 and average <=69):
    print("Your grade is D")
elif average < 60:
    print("Your grade is F")
