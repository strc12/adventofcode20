dirs=[]
f=open("day12input.txt","r")
for line in f:
    d=line[0]
    w=int(line[1:])
    dirs.append((d,w))
f.close()
#print(dirs)
pointing=1#east
N=0
E=0
for dir in dirs:
    if dir[0]=="N":
        N+=dir[1]
    elif dir[0]=="S":
        N=N-dir[1]
    elif dir[0]=="E":
        E=E+dir[1]
    elif dir[0]=="W":
        E=E-dir[1]
    elif dir[0]=="L":
        pointing-=dir[1]/90
        if pointing<=0:
            pointing=4+pointing          
    elif dir[0]=="R":
        
        pointing+=dir[1]/90
        if pointing>=5:
            pointing=pointing%4
    elif dir[0]=="F":
        if pointing==1:
            E+=dir[1]
        elif pointing==2:
            N-=dir[1]
        elif pointing==3:
            E-=dir[1]
        elif pointing==4:
            N+=dir[1]
print(abs(N)+abs(E))




