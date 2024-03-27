#Author: Nirupama Poojari
# Email: poojarn@miamioh.edu
# Class: CSE 102
# Section: C
# Date: 3/11/2021

'''
  Purpose: The program reports the number of pounds that is equivalent to and the number of ounces left over
  Input: Number of ounces
  Output: Number of pounds
'''

ounces = int(input("How many ounces?"))
if ounces <0:
   print("The number of ounces cannot be negative.")
elif ounces <= 16:
    print("There are ",ounces, "ounces.")
elif ounces > 16:
    print("There are ", int(ounces/16), "pounds and ", ounces%16, " ounces left over.")


