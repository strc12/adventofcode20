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
    
    #print(temp,code,let,code[int(temp[0])-1],code[int(temp[1])-1])
    if (code[int(temp[0])-1]==let) ^ (code[int(temp[1])-1]==let):
        count+=1
    #print(temp,code,let,code[int(temp[0])-1],code[int(temp[1])-1],count)
print(count)
    
