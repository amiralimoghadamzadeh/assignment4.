m = int(input('enter the number of rows'))
n = int(input('enter the number of coloumns'))
def f(m,n):
    p = ''
    if (n % 2) == 0:
        p = n * "*#"
    else:
        p = (int((n - 1) / 2) * "*#") + "*"

    for i in range(m):
        print(p)


f(m,n)
