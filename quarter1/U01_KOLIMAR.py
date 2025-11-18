def divisors(divisor, lst):
    """this function determines if a number in a list is divisible by the given divisor

    parameter:
    -lst: list of numbers to check
    -divisor: the integer elements of lst are divided by

    the function:
    -Creates the list - numbers
    -loops through the list lst and checks if the number is divisible by the given divisor
    -if it is, it adds the number to the list of numbers
    it returns the list of numbers"""
    numbers = []
    for i in range(len(lst)):
        if int(lst[i]) % divisor == 0:
            numbers.append(int(lst[i]))
    return numbers
print(divisors(divisor = int(input("Enter divisor")),lst = [2,5,8,1,6,5]))