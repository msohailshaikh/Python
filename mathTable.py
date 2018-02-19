#

x = int(input("Which table you want ? "))
i = 0
while True:
    if i == 10:
        break
    i += 1
    print(str(x) +" * " + str(i) + "  = " + str(x*i))
print()
print()
for i in range(10):
    i += 1
    print(str(x) + " * " + str(i) + "  = " + str(x*i))
