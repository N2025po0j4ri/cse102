# Author: Nirupama Poojari
# Program Description: Asks users for
# the number of eggs in the basket
# 1 May 2022
# poojarn@miamioh.edu

eggNum = int(input("How many eggs are in the basket? "))

if eggNum < 12:
    print("There are ", eggNum, "eggs")
else:
    left_over = eggNum%12
    dozenNum = eggNum // 12
print("There are", dozenNum,"dozen eggs and",left_over ,"eggs left over.")
