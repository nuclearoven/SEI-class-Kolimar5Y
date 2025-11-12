file = open('Numbers.txt', 'r')
text = file.readlines()
divisor = int(input("Enter divisor"))
i=0
for x in text:
    i=i+1
    if int(text[i-1]) % divisor == 0:
        print(x)
