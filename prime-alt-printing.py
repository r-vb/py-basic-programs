def prime(a,b):
    primenum_list = []
    for i in range(a,b):
        if i == 0 or i == 1:
            continue
    else:
        for j in range(2 , int(i/2)+1):
            if i%j == 0:
                break
        else:
            primenum_list.append(i)
    return primenum_list

starting_num = 2
ending_num = 14
calling = prime(starting_num , ending_num)
if len(calling) == 0:
    print('Prime numbers do not exist in this range!!')
else:
    print('The prime numbers in this range is/are: ', calling)