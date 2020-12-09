code=[]
f=open("day9input.txt","r")
for line in f:
    code.append(int(line))
f.close()
#print(code)


def adds(b):
    prev=[]
    for K in range(b-25,b):
        prev.append(code[K])
    #print(prev)
    addlist=[]
    for num in prev:
        for num1 in prev:
            if num1!=num:
                addlist.append(num+num1)
    return addlist


posinlist=25
for k in range(posinlist,len(code)):
    listofadds=adds(k)
    #print(listofadds)
    #print("checking ",code[k])
    if code[k] not in listofadds:
        print (code[k])

    posinlist+=1
    

