#Phase 1

import random

number = int(input("How many dice to roll?"))
rolls = []

for i in range(number):
    x = random.randint(1, 6)
    rolls.append(x)

print("sum of all dices is:", sum(rolls))

#phase 2
print("Pleas enter at least 5 numbers")
list_number = []
num = input("Give a number: ", )
while num != "":
    list_number.append(num)
    num = input("Give a number: ", )
list_number.sort(reverse=True)
print("The first 5 greatest number are: ")
for i in range(5):
    print(list_number[i], end=" ")

#phase 3
num = int(input("Enter a integer number"))
divisible = False
if num > 1:
    for i in range(2, num-1):
        if num % i == 0:
            divisible = True
            break

if divisible == False:
    print("This is a prime number")
else:
    print("This is not a prime number")

#phase 4
print("Give the name of 5 cities")
cities = []
for i in range(5):
    name = input("Enter the name:",)
    cities.append(name)
for i in range(5):
    print(cities[i])


