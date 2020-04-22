import random
import matplotlib.pyplot as plt
a=[]
b=[]
def rummy():

    account=0
    for i in range(365):
        a.append(i+1)
        x=random.randint(1,10)
        y=random.randint(1,10)
        if x==y:
            account=account+900-100
        else:
            account=account-100
        b.append(account)
        print(account)
    plt.plot(a,b)
    plt.show()
rummy()
    
