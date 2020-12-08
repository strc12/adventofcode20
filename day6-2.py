resps=[]
total=0
alphabet="abcdefghijklmnopqrstuvwxyz"
f=open("day6input.txt","r")
temp=[]
for line in f:
    
    if line!="\n":
        temp.append(line.strip("\n"))
    else:
        resps.append(temp)
        temp=[]
f.close()
#print(resps)
for resp in resps:
    count=0
    #print(resp)
    #print(len(resp))
    longest=max(resp,key=len)
    
    for letter in longest:
        duplet=True
        #print(entry,"entry")
        for entry in resp:
            if letter not in entry:
                duplet=False
        if duplet==True:
            count+=1
    #print(count)


    total+=count
print(total)