# This program averages the test scores. It asks the user for the number of students and the number of test scores per student
# Get the number of students
num_students = int(input("How many students are there in the class ?"  ))
testscore = int(input("How many test scores per student? "))
# Determine student's average test scores
for student in range(num_students):
# Initialize the accumulators
    total = 0.0
# Get a student's test scores:
    print('Student number', '\t', student + 1)
    print('..............')
    for test in range(testscore):
        print('Test number', '\t', test +1)
        score = float(input('Enter the score: '))
        # Add the score to the accumulator
        total += score
        average = total/testscore
        print('The average for student number is :', student+1, average)
