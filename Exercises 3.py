# phase 1
zander = float(input("Please give the length of zander in centimeters"))
min_l = 42
if zander >= 42:
    print("OK")
if zander < 42:
    print(f"Release the zander back into the lack, because zander shor by  {42-zander}")

# phase 2
answer = input("Enter the cabin class of a cruise ship:")

if answer == "LUX":
    print("Upper-deck cabin with a balcony.")
elif answer == "A":
    print("Above the car deck, equipped with a window.")
elif answer == "B":
    print("Windowless cabin above the car deck.")
elif answer == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#phase 3
gender = ("Male", "Female")

q1 = input("What is your biological gender ?")

if q1 == "Male":
    q2 = int(input("What is your hemoglobin value (g/l)"))
    if q2 > 167:
        print("High")
    elif q2 < 134:
             print("Low")
    else:
        print("Normal")
elif q1 == "Female":
    q2 = int(input("What is your hemoglobin value (g/l)"))
    if q2 > 155:
        print("High")
    elif q2 < 117:
        print("Low")
    else:
        print("Normal")

#phase 4
year = int(input("Enter a Year"))

if (year % 4 == 0) and (year % 100 != 0):
    print("This is leap year")
elif (year % 400 == 0) and (year % 100 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
