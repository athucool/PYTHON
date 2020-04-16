import random
import string 

u=[1]*10
print(u)
for i in range(100):
    y=random.randint(0,9)
    print(y)
    l=random.choice(string.ascii_letters)
    if u[y]==1:
        u[y]=l
    else:
        continue
    y=random.randint(0,9)
    h=random.randint(1,9)
    if u[y]==1:
        u[y]=str(h)
    else:
        continue
print(u)
random.shuffle(u)
i="".join(u)
print(i.upper())
