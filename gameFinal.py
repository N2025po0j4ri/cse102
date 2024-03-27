#Author: Nirupama Poojari
# Email: poojarn@miamioh.edu
# Class: CSE 102
# Section: C
# Date: 3/11/2021

'''
  Purpose: Determine the ticket price for watching a game
  Input: Age
  Output: The ticket price
'''

age = int(input("Enter your age:"))
if age < 10:
    print("You're not eligible to buy a ticket")
elif age > 50  or  age < 20:
    print("The ticket price is $12")
else:
    print("The ticket price is $20")

