# phase 1
import math
import random

name = input("What is your name ?")
print("Hello, " + name + "!")

# phase 2
radius = float(input("Give the radius ?"))
area = math.pi * radius ** 2
print("Area is " + str(area))
print(f"Area is {math.pi * radius **2:.1f}")

# phase 3

width = float(input("Give the Width ?"))
length = float(input("Give the Length ?"))
perimeter = 2 * (width + length)
area = width * length
print("The perimeter of a rectangle is" + str(perimeter))
print("The Area of a rectangle is" + str(area))

# phase 4
n1 = int(input("Give the first integer number ?"))
n2 = int(input("Give the second integer number ?"))
n3 = int(input("Give the third integer number ?"))
sum1 = n1+n2+n3
pro = n1*n2*n3
avg = int(sum1)/3
print("Sum of three integer number is " + str(sum1))
print("Product of three integer number is " + str(pro))
print("Average  of three number is " + str(avg))

# phase 5
"""One talent is 20 pounds.
One pound is 32 lots.
One lot is 13.3 grams."""


t = float(input( "Enter a mass in talents ?"))
p = float(input("Enter a mass in Pounds ?"))
l = float(input("Enter a mass in lots ?"))
talent = float(t)*20*32*13.3
pound = float(p)*32*13.3
lot = float(l)*13.3
wight = int(talent+pound+lot)//1000
g = float(talent+pound+lot) % 1000
print("The weight in modern units: " + str(wight), f"kilograms and :  {g:0.2f} grams")

# phase 6
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9)))
print(str(random.randint(1, 6))+str(random.randint(1, 6))+str(random.randint(1, 6))+str(random.randint(1, 6)))
