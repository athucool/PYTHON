import random
from PIL import Image

class snake_nladder:

    def __init__(self,p1):
        self.x=x
        self.p1=p1

    def show_img(self):
        img=Image.open('nptel/snake_n_ladder.jpg')
        img.show()
            
    def snakee(self):
        snake=[[46,5],[48,9],[44,19],[52,11],[59,17],[52,11],[69,33],[64,36],[83,19],[95,24],[98,28]]

        for i in snake:
            if i[0]==self.p1:
                print(" ha ha,Snake eat you!")
                self.p1=i[1]
                

            m=False
            return self.p1,m
                   
    def laddder(self):
        ladder=[[8,26],[21,79],[50,91],[43,77],[54,93],[62,96],[80,100],[66,87]]

        for i in ladder:
            if i[0]==self.p1:
                print("congrats, u got laddder")
                self.p1=i[1]
            m=False
            return self.p1,m

    def add(self):
            self.p1=self.p1
            return self.p1
                
             
             

    
l=0
e=0
n=0
c=0
p1=0
name1=input("enter first player name")
name2=input("enter second player name")

while(n!=1):
    m=True
    print("press 1 for ready to role dice")
    o=int(input())
    if o==1:
        x=random.randint(1,6)
        if c%2==0:
            l=l+x
            p1=l
            print("FIRST PLAYER TURN..!")
            print("dice=",x)
            u=snake_nladder(p1)
            po1,m=u.snakee()
            po1,m=u.laddder()
            if m:
                po1=u.add()
                print("hey {} you r on {} step".format(name1,po1))
            else:
                print("hey {} you r on {} step".format(name1,po1))
            l=po1
            if po1==100:
                print("first player win")
                break
                n=1

            print("if u want to show deskboard press 5 else press 1")
            r=int(input())
            if r==5:
                u.show_img()
            c=c+1

        else:
            print("SECOND PLAYER TURN..!")

            e=e+x
            p1=e
            print("dice=",x)
            u=snake_nladder(p1)
            po1,m=u.snakee()
            po1,m=u.laddder()
            if m:
                po1=u.add()
                print("hey {} you r on {} step".format(name2,po1))
            else:
                print("hey {} you r on {} step".format(name2,po1))
            e=po1
            if po1==100:
                print("first player win")
                break
                n=1

            print("if u want to show deskboard press 5 else press 1")
            r=int(input())
            if r==5:
                u.show_img()
            c=c+1

             
