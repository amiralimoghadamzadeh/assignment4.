import math
n = int(input('enter your number'))
l = []
yes = 0
if n == 1 or n == 2:
    yes += 1
elif n == 0:
  yes += 1
else:
    pass

for i in range(1,int( n / 2) + 1):
    if n % i == 0:
        l.append(i)
    else:
        pass

for k in l:
    if math.factorial(k) == n:
        yes += 1
    else:
       pass


if yes > 0:
    print('yes')
else:
    print('no')