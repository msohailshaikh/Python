# Math Table Generation program
# Take input from the user untill a vowel is entered

# Python:       Program for Math Table Generation
# Author:       Sohail Shaikh
# Created:      01-Jan-2018
# Modified:     01-Jan-2018
# Script:       mathTables.py


tab1 = int(input("Enter table range from :"))
tab2 = int(input("Enter table range to   :"))
print()
print("Tables will generate from {} to {}".format(tab1,tab2))
print()
for i in range(tab2):
    print("<<< Table - {} >>>".format(tab1))
    print()
    for cnt in range(1,11):
        print(str(tab1) + "*" + str(cnt) + "=" + str(tab1*cnt))
        cnt += 1
    print()
    i += 1
    tab1 += 1
    if tab1 > tab2:
        break

