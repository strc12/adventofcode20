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
WN=1
WE=10
for dir in dirs:
    if dir[0]=="N":
        WN+=dir[1]
    elif dir[0]=="S":
        WN=WN-dir[1]
    elif dir[0]=="E":
        WE=WE+dir[1]
    elif dir[0]=="W":
        WE=WE-dir[1]
    elif dir[0]=="R":
        #rotate waypoint around NE
        if dir[1]/90 ==1:
            t=WE
            WE=WN
            WN=-t
        elif dir[1]/90 ==2:
            WE=-WE
            WN=-WN   
        elif dir[1]/90 ==3:
            t=WE
            WE=-WN
            WN=t        
    elif dir[0]=="L":
        if dir[1]/90 ==1:
            t=WE
            WE=-WN
            WN=t
        elif dir[1]/90 ==2:
            WE=-WE
            WN=-WN   
        elif dir[1]/90 ==3:
            t=WE
            WE=WN
            WN=-t     
    elif dir[0]=="F":
            E=E+(dir[1]*WE)
            N=N+(dir[1]*WN)
    print(N,E,WN,WE)
print(abs(N)+abs(E))


