#Author: Nirupama Poojari
# Email: poojarn@miamioh.edu
# Class: CSE 102
# Section: C
# Date: 2/25/2021

'''
  Purpose: Calculate the change in dollars, quarters, dimes, nickels, and pennies
  Input: Price of the item bought and money given to the cashier.
  Output: Change in dollards, quarters, dimes, nickels, and pennies.
'''
# Descriptor of program
print("Change Calculator\n") 

#Requesting input of price from the cashier in dollars and cents
price = 100*float(input("Enter the price of the item bought: " ))

#Requesting input of amount of money given to the cashier in dollars & cents
pay = 100*float(input("Enter the amount of money you gave the cashier: "))

#Calculating the total change in cents
change = int(pay-price)

#Return conversions

print("\nYour change:")

#Calculating dollars 
dollars = int(change/100)
print('   dollars     ', dollars)

# Calculating quarters
remainder = int(change%100)
quarters = int(remainder/25)
print('   quarters    ', quarters)

#Calculating dimes
remainder = int(remainder%25)
dimes = int(remainder/10)
print('   dimes       ', dimes)

#Calculating nickels
remainder = int(remainder%10)
nickels = int(remainder/5)
print('   nickels     ', nickels)

#calculating pennies
pennies = int(remainder%5)
print('   pennies     ', pennies)


# Result message
print("\nThank you for your business!\n")
