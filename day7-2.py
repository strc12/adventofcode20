raw=[]
bags={}
f=open("day7input1.txt","r")
for line in f:
    raw.append(line.strip("\n"))
f.close()
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
    bob={}
    for item in y:
        sp=item.find(" ")
        num=item[:sp]
        desc=item[sp+1:]
        if desc!="her":
            bob[desc.strip()]=int(num)
    z=x[0].strip(" ")
    bags[z]=bob
print(bags)
count=1
found=""

def checkbag(bagstocheck,colour):
    global count
    listofbags=bagstocheck[colour]
    print(listofbags,"lob")

    if "" in listofbags:
        return False
    elif "shiny gold" in listofbags:
        
        return True
    else:
        results=[]
        for bag in listofbags:
            print()
            print(listofbags[bag],"bag")
            count=count+count*listofbags[bag]
            results.append(checkbag(bagstocheck,bag))
            print(count)
        if True in results:
            return True
        else:
            return False

nobags=0
def countbags(baglist,bag):
    global nobags
    if bag=="":
        return 1
    else:
        countbags(baglist,bag)

baglist=[]
baglist.append(bags["shiny gold"])
count=1
print(baglist,count)
for bag in baglist:
    countbags(baglist,bag)
    
    #if checkbag(bags,bag):
    #    nobags+=1
print(nobags)
print(count)