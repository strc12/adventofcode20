codes=[]
f=open("day8input.txt","r")
for line in f:
    temp=line.split(" ")
    temp[1]=int(temp[1])
    temp.append(False)
    codes.append(temp)  
f.close()
print(codes)
pos=0
acc=0
codes[223][0]="nop"
while codes[pos][2]!=True and pos<len(codes)-1:
    codes[pos][2]=True
    if codes[pos][0]=="nop":
        pos+=1
    elif codes[pos][0]=="acc":
        acc+=codes[pos][1]
        pos+=1
    else:
        pos=pos+(codes[pos][1])
    
    #print(pos)
print(acc)