# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 3-Jan-2018
# Modified: 3-Jan-2018

myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]
mySearch = int(input("Please enter your number that you want to search : "))
resultTag = False

# using For Loop
for i in range(len(myList)):
    if(myList[i] == mySearch):
        resultTag = True
        print('%d number found at %d position'%(mySearch,i))
        break
if(resultTag==False):
    print('%d number not found in the List'%mySearch)


