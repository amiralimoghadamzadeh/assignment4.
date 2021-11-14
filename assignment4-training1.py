import random
n = int(input('how many numbers?'))
l = []
while len(l) < n:
    a = random.randint(0,n)
    if a in l:
        pass
    else:
        l.append(a)

print(l)