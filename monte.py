#Monte hall problem
#either swap or not
# 3 gates ,2 gates :-goats ,1gate -car
#choose 1 gate 
#host will open a goat gate done 
# left with 1 car and 1 goat gate 
#host will offer us to change our choice 
# either yes or no
#winning chances?

#n = int(input())
#l = []
#for i in range(n):
#    s = input().split()
#    cmd = s[0]
#    args = s[1:]
#    if cmd !="print":
#        cmd += "("+ ",".join(args) +")"
#        eval("l."+cmd)
#    else:
#        print(l)


import random
swap=0
noswap=0
total=0
ch='y'
while ch=='y':
    gates=[0]*3
    goats=[]
    x=random.randint(0,2)
    gates[x]="BMW"
    for i in range(3):
        if i==x:
            continue
        else:
            gates[i]="Goat"
            goats.append(i)
    choice=int(input("Select ur gate from 0,1,2\t"))
    door_open=random.choice(goats)
    while door_open==choice:
        door_open=random.choice(goats) 
    print("Let's open a door for u that is door number "+str(door_open))
    mind=input("Do u want to change ur choice y or n")
    if mind=="y":
       swap=swap+1
       if gates[choice]=="Goat":
          print("U win the BMW")
       else:
           print("U lost")
    else:
       noswap=noswap+1
       if gates[choice]=="Goat":
          print("U lost")
       else:
           print("U win the BMW") 
    total=total+1
    ch=input("Do u want to play again y or n")    
print("winning chances when u swap"+str(swap))
print("winning chances when u don't swap"+str(noswap))
print(total)

