raw=[]
bags={}
f=open("day7input1.txt","r")
for line in f:
    raw.append(line.strip("\n"))
f.close()
#
# print(raw)
for entry in raw:
    x=(entry.split("bags "))
    y=x[1].strip (" contain") 
    y=y.replace(" bags.","")
    y=y.replace(" bags, ",",")
    y=y.replace(" bag","")
    y=y.replace(" s.","")
    y=y.replace(", ",",")
    y=y.strip(".")
    y=y.split(",")
    #print(y)
    bob={}
    for item in y:
        sp=item.find(" ")
        num=item[:sp]
        desc=item[sp+1:]
        #print(num,"-")
        #print(desc,"-")
        if desc!="her":
            bob[desc.strip()]=int(num)
    #print(bob)

    z=x[0].strip(" ")
    bags[z]=bob
print(bags)
count=0
found=""

def checkbag(bagstocheck,colour):
    global count
    listofbags=bagstocheck[colour]
    print(listofbags,"lob")

    if "" in listofbags:
        return False
    elif "shinygold" in listofbags:
        return True
    else:
        results=[]
        for bag in listofbags:
            print(bag,"bag")
            results.append(checkbag(bagstocheck,bag))
        #print(results)
        if True in results:
            return True
        else:
            return False
nobags=0
for bag in bags:
    
    if checkbag(bags,bag):
        nobags+=1
print(nobags)