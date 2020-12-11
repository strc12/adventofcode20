jolts=[]
f=open("day10input2.txt","r")
for line in f:
    jolts.append(int(line))
f.close()
jolts=sorted(jolts)
print (jolts)
l=len(jolts)
print(l)
opts=[1,2,3]
ones=1
threes=1
for k in range(l-1):
    #print(k)
    if jolts[k+1]==jolts[k]+1:
        ones+=1
    else:
        threes+=1
print(ones*threes)
