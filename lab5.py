#Author: Nirupama Poojari
#Class: CSE 102
#Date: 3/4/2022

firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
if firstnum < secondnum:
    print("This number", firstnum, "is less than", secondnum)
elif firstnum > secondnum:
    print("This number", firstnum, "is greater than", secondnum)
elif firstnum == secondnum:
    print("This number", firstnum, "is equal to ", secondnum)
