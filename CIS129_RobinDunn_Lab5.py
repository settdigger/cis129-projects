# Module 5 Lab-5
# Robin Dunn
# June 21, 2024
# This script calculates a store's collected bottles per week and calculates its value in dollars

# Lab 5 The Bottle Return Program

# declare local variables

total_bottles = 0
counter = 1
today_bottles = 0   
total_payout = 0
keep_going = "y"


# This loop checks if the user wants to enter another week's data

while keep_going == "y":
    today_bottles = 0
    total_bottles = 0    
    counter = 1
    
# This loop gathers the data for the next week

    while counter < 8: 
        today_bottles = input ("Enter number of bottles for day #" +str(counter)+ ": ")
        total_bottles = int(today_bottles) + int(total_bottles)
        counter = counter + 1
        total_payout = total_bottles * 0.10
    
# Here we display the week's totals
    print ("The total number of bottles collected is ", (total_bottles))
    print ("Your payout is $", "{0:.2f}".format(total_payout))
    
# Ask if they have more data to enter
    print ("Do you want to enter another week's worth of data?") 
    keep_going = input ("Enter y or n: ")


