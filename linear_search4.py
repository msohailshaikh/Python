# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 4-Jan-2018
# Modified: 6-Jan-2018
# Script: Linear_Search4.py
# Functionalaties:  While Loop, def <Function>

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]

resultTag = False
r = range(len(myList))
def ls_Search(myList, mySearchVal):
    cnt = 0
    while (cnt in r):
        if(myList[cnt] == mySearchVal):
            resultTag = True
            print('%d number found at %d position'%(mySearchVal,cnt))
            break
        else:
            resultTag = False
        cnt = cnt + 1
        
    if(resultTag==False):
        print('%d number not found in the List'%mySearchVal)

mySearchVal = int(input("Please enter your number that you want to search : "))

# Using funciton here
ls_Search(myList, mySearchVal)
