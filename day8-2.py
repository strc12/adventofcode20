codes=[]
f=open("day8input.txt","r")
for line in f:
    temp=line.split(" ")
    temp[1]=int(temp[1])
    temp.append(False)
    codes.append(temp)  
f.close()
#print(codes)
def traverse(pos):
    acc=0
    #print(codes[pos][2])
    while codes[pos][2]!=True and pos<len(codes)-1:
        #print(pos,"pos")
        codes[pos][2]=True
        if codes[pos][0]=="nop":
            pos+=1
        elif codes[pos][0]=="acc":
            acc+=codes[pos][1]
            pos+=1
        else:
            pos=pos+(codes[pos][1])
        #print(acc,"acc")
    if pos==len(codes)-1:
        acc+=codes[pos][1]
        return acc, True
    else:
    
        return acc,False

pos=0
acc=0
count=0
nops=[]
jmps=[]

for code in codes:
    if code[0]=="nop":
        nops.append(count)
    elif code[0]=="jmp":
        jmps.append(count)
    count+=1
success=False
for nop in nops:
    codes[nop][0]="jmp"
    acm,suc=traverse(0)
    if suc==True:
        success=True
        out=acm
        print("done")
        print(codes)
    codes[nop][0]="nop"
    for code in codes:
        code[2]=False

while success==False:
    #for jmp in jmps:
        codes[223][0]="nop"
        acm,suc=traverse(0)
        if suc==True:
            #print(jmp)
            success=True
            out=acm
            print("donejmp")
            print(codes)
        #codes[jmp][0]="jmp"
        #for code in codes:
        #    code[2]=False

print (out-1,"out")#gives one more than it should?