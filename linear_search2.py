# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 4-Jan-2018
# Modified: 6-Jan-2018
# Script: Linear_Search2.py
# Functionalaties:  For Loop, def <Function>

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]

resultTag = False
r = range(len(myList))
def linear_search(myList, mySearchVal):
    for cnt in r:
        if (myList[cnt] == mySearchVal):
            resultTag = True
            print('%d number found at %d position' % (mySearchVal, cnt))
            break
        else:
            resultTag = False
    if (resultTag == False):
        print('%d number not found in the List' % mySearchVal)


mySearchVal = int(input("Please enter your number that you want to search : "))

# Funciton ls_asnwer using here
linear_search(myList, mySearchVal)
