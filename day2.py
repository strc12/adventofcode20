nums=[]
f=open("day2-1.txt","r")
for line in f:
    temp=line.split()
    nums.append(temp)

f.close()
count=0
for k in nums:
    temp=k[0].split("-")
    let=k[1].strip(":")
    code=k[2]
    numlet=0
    for letter in code:
        if letter==let:
            numlet+=1
            
   # print(numlet,int(temp[0]),int(temp[1]))
    if numlet>=int(temp[0]) and numlet<=int(temp[1]):
        count+=1
print(count)
    
