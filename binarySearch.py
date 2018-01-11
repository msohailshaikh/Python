# Python Program for Linear Search
# Author: Sohail Shaikh
# Created: 4-Jan-2018
# Modified: 6-Jan-2018
# Script: Linear_Search2.py
# Functionalaties:  For Loop, def <Function>

import random
myList = [25, 1, 50, 57, 2, 3, 4, 5, 6, 7, 10, 8, 9]
myList = sorted(myList)

def binary_search(item_list, item):
    first = 0
    last = len(item_list)
    found = False
    while (first < last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binary_search(myList, 57))
print(binary_search(myList, 101))
print(binary_search(myList, 25))

