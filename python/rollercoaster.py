print("Welcome to the rollercoaster!\n")
height = int(input("What's your height in centimeters? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? \n"))
    if age<=12:
        bill = 5
        print("Child tickets are 5$ \n")
    elif age>12 and age<=18:
        bill = 7
        print("Youth tickets are 7$ \n")
    else:
        bill = 12
        print("Adult tickets are 12$ \n")
    wants_photo = input("Do you want a photo? It's 3$. Type Y for yes and N for no ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller to ride the rollercoaster.")
