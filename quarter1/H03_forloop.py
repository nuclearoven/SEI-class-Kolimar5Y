#1 prints every letter in the iterable string
iterable = "Python"
for variable in iterable:
    print(variable)

#2 prints "Hello" five times
for i in range(5):
    print("Hello")

#3 prints every word in the iterable string
iterable = "Learning Python is fun"
for variable in iterable.split():
    print(variable)

#4 prints every letter in the iterable string
iterable = "Computer"
revers = reversed(iterable)
for variable in revers:
    print(variable)

#5 prints every letter in the iterable string along with its number in order
iterable = "Science"
count = 0
for variable in iterable:
    count += 1
    s = str(count)
    print(variable+s)

#6 prints how many of the letter E is in the iterable string
iterable = "Experience teaches slowly"
count = 0
for variable in iterable:
    if variable == "e" or variable == "E":
        count += 1
print(count)

#7 prints every vowel in the iterable string
iterable = "Programming is powerful"
for variable in iterable:
    if variable == "a" or variable == "e" or variable == "i" or variable == "o" or variable == "u":
        print(variable)

#8 prints every letter with an even order in the iterable string
iterable = "Artificial Intelligence"
count = 0
list1 = []
for variable in iterable:
    count += 1
    if count % 2 == 0:
        list1.append(variable)
s = "".join(list1)
print(s)
#9 prints a triangle pattern with the word python
s = "Python"
for i in range(1, len(s) + 1):
    print(s[:i])