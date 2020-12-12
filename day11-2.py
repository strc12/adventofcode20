seatso=[]
f=open("day11input.txt","r")
row=0
for line in f:
    temp=[]
    for letter in line.strip("\n"):
        temp.append(letter)
    col=len(temp)
    seatso.append(temp)
    row+=1
#print (row,col)

def printseats(s,row,col):
    output=""
    for x in range(row):
        row=""
        for y in range(col):
            row+=s[x][y]
        output=output+row+"\n"
    print(output)
#printseats(seatso)

def sitdown(seats,row,col):
    outputy=[]
    for x in range(row):
        temp=[]
        for y in range(col):
            temp.append("")
        outputy.append(temp)
    changes=[(-1,0),(1,0),(0,1),(0,-1),(-1,1),(-1,-1),(1,1),(1,-1)]
    same=0
    for x in range(0,row):
        for y in range(0,col):
            tot=0
            for k,l in changes:
                newx=x+k
                newy=y+l
                if 0<=newx<row and 0<=newy<col:
                    if seats[newx][newy]=="#":
                        tot+=1
            if seats[x][y]==".":
                outputy[x][y]="."
            elif tot>=4 and seats[x][y]=="#":
                outputy[x][y]="L"
            elif tot==0 and seats[x][y]=="L":
                outputy[x][y]="#"  
            else:
                outputy[x][y]=seats[x][y]

    if outputy==seats:
        return outputy,False
    else:
        return outputy,True
x,r=sitdown(seatso,row,col)
#printseats(x,row,col)
while r==True:
    x,r=sitdown(x,row,col)
    #printseats(x,row,col)
count=0
for i in range(row):
        for j in range(col):
            if x[i][j]=="#":
                count+=1
        
print(count)