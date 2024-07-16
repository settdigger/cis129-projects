# Module 11 Lab, part 2
# CIS 129
# Robin Dunn
# July 16, 2024

# Part 2 reads our grades.txt file and lists the grades, count, and average

# initialize our variables
counter=0
total=0

# cycle  through the grades

with open('grades.txt', mode='r') as grades:
    print('Grades:')
    print ('')

    # increment the counter and add the grades
    for record in grades:
        counter +=1
        total += int(record)
        print(record)
        
print ('* * * * *')
print ('Total grades:', counter)
print ('Average:', f'{(total / counter):.2f}')
