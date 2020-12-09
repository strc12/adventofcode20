code=[]
numtofind=217430975

f=open("day9input.txt","r")
for line in f:
    code.append(int(line))
f.close()
print(len(code))
def adds(thing,num):
    possibles=[]
    #print(thing,num)
    for a in range(len(thing)):
        sub=0
        for k in range(a,len(thing)):
            sub+=code[k]
            if sub==num:
                if num != thing[k]:
                    start=thing[a]
                    end=thing[k]
                    print(a,thing[a],k,thing[k])
            possibles.append(sub)
    return start,end
st,ed=adds(code,numtofind)
print(st,ed)
p1=code.index(st)
p2=code.index(ed)
max=0
min=9999999999999999999999999999999999999999
for k in range (p1,p2):
    print(code[k])
    if code[k]>max:
        max=code[k]
    if code[k]<min:
        min=code[k]
print (max,min, max+min)
    

