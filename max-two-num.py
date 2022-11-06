def max( a , b ):

    if a >= b:
        return a
    else:
        return b

a = input("enter 'a' value: ")
b = input("enter 'b' value: ")

print("Maximum of the two is {0}" .format(max( a , b )))