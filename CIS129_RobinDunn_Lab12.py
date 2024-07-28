# Module 12 Lab
# CIS 129
# Robin Dunn
# July 25, 2024

# Creates a pet class and then creates your very own pet!

# First we create the class

class Pet:
	"""Your loveable pet."""
	def __init__(self, name = '', type = '', age = 0):
		self.__name = name
		self.__type = type
		self.__age = age
    
    # then we create the methods for the Pet class
    
	def set_name(self, n):
		"""Name your pet."""
		self.__name = n
        
	def set_type(self, t):
		"""Tell us your pet type."""
		self.__type = t
        
	def set_age(self, a):
		"""Tell us your pet's age."""
		self.__age = a
	
	def get_name(self):
		"""Returns the name of your pet."""
		return self.__name 
        
	def get_type(self):
		"""Returns the type of your pet."""
		return self.__type 
        
	def get_age(self):
		"""Returns the age of your pet."""
		return self.__age 

# Now for our main wrapper function 

def main():

    # here is an instance of Pet class
	your_pet = Pet()

    # calls all the methods we need for our pet

	your_pet.set_name(input("What is your pet's name? "))
	your_pet.set_type(input("What kind of pet is it? "))
	your_pet.set_age(input("How old is your pet? "))

	print("\nYour pet's name is", your_pet.get_name())
	print("Your pet is a", your_pet.get_type())
	print("Your pet's age is", your_pet.get_age())
   
    
    
main()
