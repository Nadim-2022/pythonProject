#phase 1
import random
def dice_roll():
    return random.randint(1,6)
num = dice_roll()
while num != 6:
    print(num)
    num = dice_roll()
print(num)

#phase 2

import random
def dice_roll(sides):
    return random.randint(1,sides)

num_sides = int(input("Enter the number of the sides :",))
num = dice_roll(num_sides)
while num != num_sides:
    print(num)
    num = dice_roll(num_sides)
print(num_sides)

#phase 3

def liter(gallon):
    return gallon * 3.78541

vol_gallon = int(input("Enter the volume in gallons to convert it to liter:"))
while vol_gallon >= 0:
    print(f"Volume in liter {liter(vol_gallon)}")
    vol_gallon = int(input("Enter the volume in gallons to convert it to liter:"))
else:
    print("Invalid value")

#phase 4

def list_of_paramiters(suma):
    return sum(suma)

list = [1,2,3,4,5,6,7,8,9,10]

print(list_of_paramiters(list))

#phase 5

def evenumbers (list):
    list_2 = []
    for i in list:
        if i % 2 == 0:
            list_2.append(i)
    return list_2

list_1= [1,2,3,4,5,6,7,8,9,10]
print("Even numbers:", evenumbers(list_1), "Even numbers:", list_1)
print()


#Phase 6
def parameter (size, price):
    cen_meter = size*100
    radius = cen_meter / 2
    sq_meter = radius * radius
    uni_price = sq_meter / price
    print(uni_price)

parameter(100,12)
