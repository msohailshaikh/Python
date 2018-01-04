# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 4-Jan-2018
# Modified: 4-Jan-2018
# Script: Linear_Search4.py
# Functionalaties:  While Loop, def <Function>

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]

resultTag = False

def ls_Search(x):
    cnt = 0
    while (cnt in range(len(myList))):
        if(myList[cnt] == x):
            resultTag = True
            print('%d number found at %d position'%(x,cnt))
            break
        else:
            resultTag = False
        cnt = cnt + 1
        
    if(resultTag==False):
        print('%d number not found in the List'%x)

mySearch = int(input("Please enter your number that you want to search : "))

# Using funciton here
ls_Search(mySearch)
