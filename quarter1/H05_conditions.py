
def EX1(temperature):
    """If the integer temperature is higher than 25 it prints It’s warm outside! else it prints It’s cool
    returns nothing"""
    if temperature > 25:
        print("It's warm outside!")
    else:
        print("It's cool.")
    return
def EX2():
    """Asks the user to input a number x and prints if its positive, negative or zero
    returns nothing"""
    x = input("enter number")
    x=float(x)
    if x > 0:
        print("Positive")
    if x < 0:
        print("Negative")
    if x == 0:
        print("Zero")
    return

def EX3():
    """Asks the user to input two numbers a and b and prints if they are odd or even
    returns nothing"""
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
    return

#Task4, pasword
def EX4():
    """Asks the user to input the string password and determines if it has 8 or more characters and has the word python in it
    if yes, it prints Valid password, if not it prints Invalid password
    returns the password"""
    pasword = input("enter password")
    if len(pasword)>7 and "python" in pasword:
        print("Valid password")
    else:
        print("Invalid password")
    return pasword

def EX5():
    """Asks the user to input a color, if its red it prints stop, if yellow it prints slow down and if green it prints go
    returns nothing"""
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
    return

def EX6():
    """Asks the user to input their age and if they have a ticket
    parameters:
    -age: integer
    -ticket: string

    if the number is 12 or more and the answer is yes it prints You may enter, if not it prints Entry denied
    returns nothing"""
    age= int(input("enter age"))
    ticket = input("do you have a ticket")
    if ticket.lower() == "yes" and age >= 12:
        print("You may enter")
    else:
        print("Entry denied")
    return

def EX7(x,y):
    """Function determines if float x is greater or less than or equal to the float y.
    Then it determines if x a positive or negative single digit number
    returns nothing"""
    #chained conditional
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
    return

def is_triangle(a, b, c):
    """
    The function then determine if the sticks with the lenghts a b c can be made into a triangle using chained conditionals
    and assigns the bul boolean as true if they can and false if they cant.
    parameters:
    -a,b,c: floats representing the lengths of the sticks
    -bul: boolean representing if the triangle can be made or not

    it returns the bool"""
    if c < a + b:
        bul = True
    else:
        if a < c+b:
            bul = True
        else:
            if b < a+c:
                bul = True
            else:
                bul = True
    return bul
EX1(30)
EX2()
EX3()
EX4()
EX5()
EX6()
EX7(5, 7)
print(is_triangle(4, 5,  6))