def si(p,t,r):
    siamt = (p*t*r)/100

    print('The Simple-Interest is: ', siamt)
    return siamt

p = int(input('Enter principal amount: '))
r = float(input('Enter rate of interest: '))
t = float(input('Enter time period on P: '))

si(p, t, r)
