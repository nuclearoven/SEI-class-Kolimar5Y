#fix code
temperature = 30
if temperature > 25:
    print("It's warm outside!")
else:
    print("It's cool.")
#Task2, determine if a number is positive negative or 0
x = input("enter number")
x=float(x)
if x > 0:
    print("Positive")
if x < 0:
    print("Negative")
if x == 0:
    print("Zero")
#Task3, determine if numbers are even or odd
a = input("a=")
b = input("b=")
a=float(a)
b=float(b)
if a % 2 ==0 and b % 2==0:
    print("Both even")
if a % 2 and b % 2:
    print("Both odd")
if a+b %2:
    print("One even, one odd")
#Task4, pasword
pasword = input("enter password")
if len(pasword)>7 and "python" in pasword:
    print("Valid password")
else:
    print("Invalid password")
#Task 5, traffic light
light = input("enter color")
if light == "red" or light == "yellow" or light == "green":
    if light == "red":
        print("stop")
    if light == "yellow":
        print("slow down")
    if light == "green":
        print("go")
else:
    print("Invalid color")
#Task 6, tickets
age= input(int("enter age"))
ticket = input("do you have a ticket")
if ticket.lower() == "yes" and age >= 12:
    print("you may enter")
else:
    print("Entry denied")
#Task 7
#chained conditional
x = 5
y = 3
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')
#single conditional
if 0 < x and x < 10:
    print('x is a positive single-digit number.')
#simplification
if x >= 0 and x <= 10:
    print('x is a positive single-digit number.')
#Task 8
def triangle(a = 4, b = 5, c = 6):
    if c < a + b:
        print("yes")
    else:
        if a < c+b:
            print("yes")
        else:
            if b < a+c:
                print("yes")
            else:
                print("no")
