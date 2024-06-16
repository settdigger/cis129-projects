"""Coffee Shop Simulator Script

This script allows the user to print a sample receipt they would get from 
buying breakfast items at their local coffee shop.

Using 4 user prompts, it generates a short receipt.

"""

# Greet the customer

print()
print ("Welcome to our Virtual Coffee Shop!")
print()


#  Ask for purchase amounts

coffees = input("How many coffees would you like? ")
muffins = input("How many muffins would you like? ") 

# Provide 2 more purchase options


burritos = input("How many breakfast burritos would you like? ")
pies = input("How many slices of pecan pie would you like? ") 

#  Make the inputs addable numbers and add them, according to their prices
#  (Coffees are $5, Muffins are $4, breakfast burritos are $6, and slices of pie are $5)


coffeecost=(int(coffees)*5)
muffincost=(int(muffins)*4)
burritocost=(int(burritos)*6)
piecost=(int(pies)*5)

subtotal = coffeecost + muffincost + burritocost + piecost

tax = subtotal * 0.06


# Make tax cents look nice

formatted_tax = "{0:.2f}".format(tax)



# Now we'll print the whole receipt

print ()
print ()
print ("***************************************")
print ("My Coffee and Muffin Shop")
print ("Number of coffees bought?")
print (coffees)
print ("Number of muffins bought?")
print (muffins)
print ("Number of breakfast burritos bought?")
print (burritos)
print ("Number of pecan pie slices bought?")
print (pies)
print ("***************************************")
print ()
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")

#  Ensure the dollar charge on receipt looks nice with no space between dollars and cents.

print ((coffees), " Coffees at $5 each: $ ", (coffeecost), ".00", sep='')
print ((muffins), " Muffins at $4 each: $ ", (muffincost), ".00", sep='')
print ((burritos), " Breakfast Burritos at $6 each: $ ", (burritocost), ".00", sep='')
print ((pies), " Pecan Pie Slices at $5 each: $ ", (piecost), ".00", sep='')
print ("6% tax: $ ",(formatted_tax))
print ("---------")


# Make total cents look nice

total = subtotal + tax
formatted_total = "{0:.2f}".format(total)


print ("Total: $ ",(formatted_total))
print ("***************************************")
print ()
print ("Thank for your visiting our virtual coffee shop!  Have a great day.")
