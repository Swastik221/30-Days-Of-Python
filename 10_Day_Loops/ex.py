def triangle(n):
    for i in range(1,n+1):
        print("*"*i)

def tables(m):
    for i in range(1,11):
        print(m,"*",i,"=",m*i)


from random import randint
print (randint(0,20))

t="hell no"
p=[i for i in t]
print(p)

from datetime import datetime
t=datetime.now()
print(t)

t="*"

for i in range(1,7):
    print(i*t)