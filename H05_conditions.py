f = open("text.txt","r")
print(type(f))
x= f.readline()
print(x)
f.close()
temperature = 30
if temperature > 25:
    print("It's warm outside!")
else:
    print("It's cool.")
#Task2
x = input()
x=float(x)
if x > 0:
    print("Positive")
if x < 0:
    print("Negative")
if x == 0:
    print("Zero")
#Task3
a = input()
b = input()
a=float(a)
b=float(b)
if a % 2 ==0 and b % 2==0:
    print("Both even")
if a % 2 and b % 2:
    print("Both odd")
if a+b %2:
    print("One even, one odd")