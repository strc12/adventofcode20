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
    changes=[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
    for x in range(0,row):
        for y in range(0,col):
            tot=0
            bob=[]
            #print(x,y,seats[x][y])
            for k,l in changes:
                
                newx=x+k
                newy=y+l
                #print(x,y,k,l,newx,newy,seats[newx][newy])
                #if 0<=newx<row and 0<=newy<col:
                if 0<=newx<row and 0<=newy<col:
                    #print(seats[newx][newy], newx<row,newx>=0,newy<col, newy>=0)
                    #if 0<=newx<row and 0<=newy<col:
                    if newx<row and newx>=0 and newy<col and newy>=0:
                        c=0
                        while newx<row and newx>=0 and newy<col and newy>=0 and seats[newx][newy]==".":
                            #print(seats[newx][newy], newx<row,newx>=0,newy<col, newy>=0)
                            newx=newx+k
                            newy=newy+l
                            c+=1
                            if not(newx<row and newx>=0 and newy<col and newy>=0):
                                break
                    #print(x,y,k,l,newx,newy,seats[newx][newy])
                   # print(c)
                    if 0<=newx<row and 0<=newy<col:
                        bob.append(seats[newx][newy]+str(k)+str(l))
                        if seats[newx][newy]=="#":
                            tot+=1 
                    else:
                        bob.append(""+str(x+1))
                c+=1 
            #print(bob,tot)
            if seats[x][y]==".":
                outputy[x][y]="."
            elif tot>=5 and seats[x][y]=="#":
                outputy[x][y]="L"
            elif tot==0 and seats[x][y]=="L":
                outputy[x][y]="#"  
            else:
                outputy[x][y]=seats[x][y]
            #print(outputy)
        #print ("row",x)
    if outputy==seats:
        return outputy,False
    else:
        return outputy,True
x,r=sitdown(seatso,row,col)
#printseats(x,row,col)
#x,r=sitdown(x,row,col)
#printseats(x,row,col)
while r==True:
#print("df")
    x,r=sitdown(x,row,col)
    #printseats(x,row,col)
count=0
for i in range(row):
        for j in range(col):
            if x[i][j]=="#":
                count+=1
        
print(count)