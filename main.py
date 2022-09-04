

n = int(input("Enter the numbers"))
while n != 0:
    if n == "":
        break
    print("Input is, " + str(n))
    n = int(input("Enter the numbers"))
else:
    print("ALl is well")