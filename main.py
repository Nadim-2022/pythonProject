secret_code1 = "NATO"
secret_code2 = "EU"

answer = input("What is the secret code?")

if answer == secret_code1:
    print("Correct")
elif answer == secret_code2:
    print("Also correct")
    secret_number = int(input("What is the secret number"))
    if secret_number == 42:
        print("You re lucky!")
    else:
        print("You are not lucky")
elif answer == "TOPSECRET":
    print("you are Ok")
#else:
#    print("Not Correct")
