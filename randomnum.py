from time import time
a = time()-float(str(time()).split('.')[0])

def randomnum(x,y):
    return int(a*(y-x)+x)

while True:
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    print(randomnum(m,n))