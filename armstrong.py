num = int(input('Enter number to check: '))
temp = num
length = len(str(num))

sum = 0
while num != 0:
    rem = num % 10
    sum = sum + (rem**length)
    num = num//10
if temp == sum:
    print('The given number', temp, 'is an armstrong.')
else:
    print('The given number', temp, 'is not an armstrong.')