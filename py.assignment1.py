# Part 1 - Getting user input

num_of_courses = input("How many courses did you finish?")
num_of_course = int(num_of_courses)
# Testing
# print(num_of_course)

course_marks = []

# Appending the values entered into the empty list
i = 1
while (i <= num_of_course):
    course_marks.append(int(input(f"Enter your mark for course {i}: ")))
    i += 1

# For loop here for printing the course marks outside the list
for x in course_marks:
    print(x)



# Part 2 - Find the Average
sum = 0
for i in range(len(course_marks)):
    sum += course_marks[i]
# Testing for the sum
# print(sum)

# 2 - after the loop,  
average = sum / num_of_course
print(f"Your average for your 5 courses is: {average}")


# Part 3 - print the grade using if condition
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
