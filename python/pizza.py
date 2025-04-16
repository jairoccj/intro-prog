print("Welcome to Python Pizza Deliveries!")
size = str(input("What size pizza do you want? S, M or L: \n"))
wants_pepperoni = str(input("Do you want pepperoni on your pizza? Y or N: \n"))
wants_extra_cheese = str(input("Do you want extra cheese? Y or N: \n"))

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if wants_pepperoni == "Y" and size != "S":
    bill += 3
elif wants_pepperoni == "Y" and size == "S":
    bill +=2

if wants_extra_cheese == "Y":
    bill += 1

print(f"Your bill will be ${bill}")