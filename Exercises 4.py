#phase 1
n = 1
while n < 1000:
    if n % 3 == 0:
        print(str(n))
    n = n + 1

#phase 2
n = float(input("Enter the value in inches"))
while n != 0:
    if n < 0:
        break
    print(f"centimeters {n*2.54:0.2f}")
    n = float(input("Enter the value in inches"))
print("Incorrect value")

#phase 3
nums = []
while True:
    num = input("Enter a number: ")
    if num == "":
        break
    nums.append(num)

largest = max(nums)
smallest = min(nums)

print("Largest number is", largest)
print("Smallest number is", smallest)

#phase 4
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input("Guess a number between 1 and 10  : "))
    if guess_num > target_num:
        print("Too high")
    if guess_num < target_num:
        print("Too low")
print("Correct")

#phase 5

count = 0

while count < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password == "Nadim" and username == "Ahmed":
        print("Access granted")
        count = 5
    else:
        print("Access denied. Try again.")
        count += 1


#phase 66

import random

input_num = int(input("Enter numbers"))

n = 0
N = 0

for i in range(input_num**2):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    origin_dist = x ** 2 + y ** 2

    if origin_dist < 1:
        n += 1

    N += 1
    pi = 4 * n / N
print(" Estimation of Pi=", pi)
