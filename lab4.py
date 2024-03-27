#Author: Nirupama Poojari
# Email: poojarn@miamioh.edu
# Class: CSE 102
# Section: C
# Date: 2/25/2021

'''
  Purpose: Being able to identify the lab
  Input:...
  Output:...
'''

print("Change Calculator\n") # Descriptor of program

#Requesting input of price from the cashier in dollars and cents
price = 100*float(input("Enter the price of the item bought: " ))

#Requesting input of amount of money given to the cashier in dollars & cents
pay = 100*float(input("Enter the amount of money you gave the cashier: "))

#Calculating the total change in cents
change = int(pay-price)

#Return conversions

print("\nYour change:")

dollars = int(change/100)
print('   dollars     ', dollars)
#Calculating change 

remainder = int(change%100)
quarters = int(remainder/25)
print('   quarters    ', quarters)
# price of quarters

remainder = int(remainder%25)
dimes = int(remainder/10)
print('   dimes       ', dimes)

remainder = int(remainder%10)
nickels = int(remainder/5)
print('   nickels     ', nickels)

pennies = int(remainder%5)
print('   pennies     ', pennies)

print("\nThank you for your business!\n")
