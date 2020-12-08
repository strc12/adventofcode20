resps=[]
total=0
alphabet="abcdefghijklmnopqrstuvwxyz"
f=open("day6input.txt","r")
temp=""
for line in f:
    
    if line!="\n":
        #print(line)
        temp=temp+line.strip("\n")
    #print(temp)
    else:
        resps.append(temp)
        temp=""
f.close()
#print(resps)
for resp in resps:
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for letter in resp:
        if letter in alphabet:
            alphabet1=alphabet.replace(letter,"")
            #print(alphabet1)
            alphabet=alphabet1
    count=26-len(alphabet)
    total+=count
print(total)