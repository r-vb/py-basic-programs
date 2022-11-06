def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while( n > 1 ):
            fact *= n
            n -= 1
        return fact

num = int(input("enter your num: "))
print("Factorial of",num,"is",factorial(num))

""" print("Factorial of {0} is {1}" .format(num , factorial(num))) """
# """-->is also commenting.