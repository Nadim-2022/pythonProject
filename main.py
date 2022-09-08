while True:
    number = int(input("Enter the number : "))
    if number <= 0:
        break
    factorial = 1
    new = 1
    while new <= number:
        factorial *= new
        new += 1
    print(f"The factorial of the number {number} is {factorial}")
print("Thank you and bye")

