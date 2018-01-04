# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 4-Jan-2018
# Modified: 4-Jan-2018
# Script: Linear_Search2.py
# Functionalaties:  For Loop, def <Function>

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]

resultTag = False

def ls_answer(x):
    for cnt in range(len(myList)):
        if (myList[cnt] == x):
            resultTag = True
            print('%d number found at %d position' % (x, cnt))
            break
        else:
            resultTag = False
    if (resultTag == False):
        print('%d number not found in the List' % x)


mySearch = int(input("Please enter your number that you want to search : "))

# Funciton ls_asnwer using here
ls_answer(mySearch)


