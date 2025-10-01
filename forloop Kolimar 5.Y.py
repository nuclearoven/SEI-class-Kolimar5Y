iterable = "Python"
for variable in iterable:
    print(variable)

for i in range(5):
    print("Hello")

iterable = "Learning Python is fun"
for variable in iterable.split():
    print(variable)

iterable = "Computer"
revers = reversed(iterable)
for variable in revers:
    print(variable)

iterable = "Science"
count = 0
for variable in iterable:
    count += 1
    s = str(count)
    print(variable+s)

iterable = "Experience teaches slowly"
count = 0
for variable in iterable:
    if variable == "e" or variable == "E":
        count += 1
print(count)

iterable = "Programming is powerful"
for variable in iterable:
    if variable == "a" or variable == "e" or variable == "i" or variable == "o" or variable == "u":
        print(variable)

iterable = "Artificial Intelligence"
count = 0
list1 = []
for variable in iterable:
    count += 1
    if count % 2 == 0:
        list1.append(variable)
s = "".join(list1)
print(s)