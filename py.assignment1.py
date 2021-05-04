
num_of_courses = input("How many courses did you finish?")
num_of_course = int(num_of_courses)
# Testing
print(num_of_course)

course_marks = []

i = 1
while (i <= num_of_course):
    course_marks.append(int(input(f"Enter your mark for course {i}: ")))
    i += 1
print(course_marks)


