# Module 11 Lab, part 1
# CIS 129
# Robin Dunn
# July 16, 2024

# Part 1 asks the user to input their grades and saves the results in a simple text file

# initialize our variable
grade=0

# get a list of grades as a series of strings
with open('grades.txt', mode='w') as grades:
    while grade != 'stop':
        grade = (input("Please enter your grades. Type 'stop' to end: "))
        if grade != 'stop':
            grades.write(grade)
            grades.write('\n')
