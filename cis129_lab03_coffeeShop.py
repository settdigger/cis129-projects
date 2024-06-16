"""Coffee Shop Simulator Script

This script allows the user to print a sample receipt they would get from 
buying coffees and muffins at their local coffee shop.

Using 2 user prompts, it generates a short receipt.

"""


#  Ask for purchase amounts

coffees = input("How many coffees would you like?")
muffins = input("How many muffins would you like?") 

#  Make the inputs addable numbers and add them, according to their prices
#  (Coffees are $5, Muffins are $4)

coffeecost=(int(coffees)*5)
muffincost=(int(muffins)*4)

subtotal = coffeecost + muffincost

tax = subtotal * 0.06


# Now we'll print the whole receipt


print ("***************************************")
print ("My Coffee and Muffin Shop")
print ("Number of coffees bought?")
print (coffees)
print ("Number of muffins bought?")
print (muffins)
print ("***************************************")
print ()
print ("***************************************")
print ("My Coffee and Muffin Shop Receipt")

#  Ensure the dollar charge on receipt looks nice with no space between dollars and cents.

print ((coffees), " Coffees at $5 each: $", (coffeecost), ".00", sep='')
print ((muffins), " Muffins at $4 each: $", (muffincost), ".00", sep='')
print ("6% tax: $ ",(tax))
print ("---------")
print ("Total: $ ",(subtotal + tax))
print ("***************************************")
