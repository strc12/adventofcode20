jolts=[]
f=open("day10input2.txt","r")
for line in f:
    jolts.append(int(line))
f.close()
jolts.append(0)
jolts=sorted(jolts)
print (jolts)
l=len(jolts)
jolts.append(jolts[l-1]+3)

print(jolts)
opts=[1,2,3]
ones=1
threes=1
temp=[]
for k in range(l-1):
    for d in opts:
        if jolts[k]+d in jolts:
            temp.append(str(jolts[k])+str(d))

    #print(k)
    if jolts[k+1]==jolts[k]+1:
        ones+=1
    else:
        threes+=1
print(ones*threes)
print(temp)
