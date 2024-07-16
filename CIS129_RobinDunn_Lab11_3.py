# Module 11 Lab, part 3
# CIS 129
# Robin Dunn
# July 16, 2024

# Part 3 moves on to CSV format, and asks the user to input student names and grades for 3 exams

import csv

# initialize our variables
firstname=0
lastname=0
exam1=0
exam2=0
exam3=0
check=0

# commence CSV input
with open('grades.csv', mode='w', newline='') as grades:
    while check != 'n':
        writer = csv.writer(grades)

        # requests user to give us the first student's data
        firstname = input("Please enter First Name: ")
        lastname = input("Please enter Last Name: ")
        exam1 = int(input("Please enter Exam 1 grade: "))
        exam2 = int(input("Please enter Exam 2 grade: "))
        exam3 = int(input("Please enter Exam 3 grade: "))

        # writes that data into the CSV file
        writer.writerow([firstname, lastname, exam1, exam2, exam3])

        # ask if there is more to do
        check = input("Enter more student grades? (y/n): ")

