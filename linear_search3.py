# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 3-Jan-2018
# Modified: 4-Jan-2018
# Script: Linear_Search2.py
# Functionalaties:  While Loop

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]
mySearch = int(input("Please enter your number that you want to search : "))
resultTag = False

# using While Loop
cnt = 0
while (cnt in range(len(myList))):
    if(myList[cnt] == mySearch):
        resultTag = True
        print('%d number found at %d position'%(mySearch,cnt))
        break
    cnt = cnt + 1
if(resultTag==False):
    print('%d number not found in the List'%mySearch)


