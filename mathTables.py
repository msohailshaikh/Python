# Python:       Program for Math Table Generation
# Author:       Sohail Shaikh
# Created:      01-Jan-2018
# Modified:     01-Jan-2018
# Script:       mathTables.py


# tab1 = int(input("Enter table range from :"))
# tab2 = int(input("Enter table range to   :"))
tab1 = 2;
tab2 = 10
print()
print("<<< Tables will generate from {} to {}".format(tab1, tab2) + " >>>")
for i in range(tab1, tab2 + 1, 9):
    # print("<<< Table - {} >>>".format(tab1))
    print()
    for cnt in range(1, 11):
        print(str(tab1) + " * " + str(cnt) + " = " + str(tab1 * cnt) \
              + "\t\t" + str(tab1 + 1) + "  *  " + str(cnt) + "  =  " + str((tab1 + 1) * cnt) \
              + "\t\t" + str(tab1 + 2) + "  *  " + str(cnt) + "  =  " + str((tab1 + 2) * cnt) \
              + "\t\t" + str(tab1 + 3) + "  *  " + str(cnt) + "  =  " + str((tab1 + 3) * cnt) \
              + "\t\t" + str(tab1 + 4) + "  *  " + str(cnt) + "  =  " + str((tab1 + 4) * cnt) \
              + "\t\t" + str(tab1 + 5) + "  *  " + str(cnt) + "  =  " + str((tab1 + 5) * cnt) \
              + "\t\t" + str(tab1 + 6) + "  *  " + str(cnt) + "  =  " + str((tab1 + 6) * cnt) \
              + "\t\t" + str(tab1 + 7) + "  *  " + str(cnt) + "  =  " + str((tab1 + 7) * cnt) \
              + "\t\t" + str(tab1 + 8) + "  *  " + str(cnt) + "  =  " + str((tab1 + 8) * cnt)
              )
        cnt += 1
    # print()
    i += 1
    tab1 += 9
    if tab1 > tab2 + 1:
        break
