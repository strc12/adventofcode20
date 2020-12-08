raw=[]
bags={}
f=open("day7input.txt","r")
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
    y=y.replace(" ","")
    y=y.replace("1","")
    y=y.replace("2","")
    y=y.replace("3","")
    y=y.replace("4","")
    y=y.replace("5","")
    y=y.replace("6","")
    y=y.replace("7","")
    y=y.replace("8","")
    y=y.replace("9","")
    y=y.replace("0","")
    y=y.strip(".")
    y=y.split(",")
    z=x[0].replace(" ","")
    bags[z]=y
#print(bags)


def checkbag(bagstocheck,colour):
    listofbags=bagstocheck[colour]

    if "her" in listofbags:
        return False
    elif "shinygold" in listofbags:
        return True
    else:
        results=[]
        for bag in listofbags:
            #print(bag)
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