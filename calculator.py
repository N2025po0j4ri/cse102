#Author: Nirupama Poojari
#Date: March 4, 2022
#email: poojarn@miamioh.edu

print("Select operation")
print("     1. Add")
print("     2. Subtract")
print("     3. Multiply")
print("     4. Divide")
choice = int(input("Enter your choice (1/2/3/4): "))
firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))
if choice == 1:
    print(firstnum,"+", secondnum, "=",firstnum+secondnum)
elif choice == 2:
    print(firstnum,"-", secondnum, "=",firstnum-secondnum)
elif choice == 3:
    print(firstnum,"*", secondnum, "=",firstnum*secondnum)
elif choice == 4:
    print(firstnum,"*", secondnum, "=",firstnum//secondnum)
