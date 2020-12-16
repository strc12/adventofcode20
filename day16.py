
class1=[1,2,3,5,6,7]
row1=[6,7,8,9,10,11,33,34,35,36,37,38,39,40,41,42,43,44]
seat1=[]
for k in range(13,41):
    seat1.append(k)
for k in range(45,51):
    seat1.append(k)
myticket=[7,1,14]
nearby=[]
f=open("day16input.txt","r")
data=f.readlines()
rest=data[:20]
tick=data[22].split(",")
tick=[int(i) for i in tick]
nearby=data[25:]
ruler={}
for line in rest:
    field,rule=line.split(": ")
    rule=rule.split(" or ")
    rules=[]
    #print(rule,"rule")
    for r in rule:
        #print("r",r)
        ruled=r.split("-")
        for k in range(len(ruled)):
            ruled[k]=int(ruled[k])
            rules.append(ruled[k])
        #print(rules)
    ruler[field]=rules
#print(ruler)
tickets=[]
for item in nearby:
    tickets.append([item])
nb=[]
for i in tickets:
    for d in i:
        b=d.split(",")
        b=[int(g) for g in b]
        nb.append(b)
odd=[]
for ticket in nb:
    temp=[]
    for k in range(20):
        for rule in ruler:
            if (ticket[k]>=ruler[rule][0] and ticket[k]<=ruler[rule][1]) or (ticket[k]>=ruler[rule][2]  and ticket[k]<=ruler[rule][3]):
                pass
            else:
                temp.append(ticket[k])
    #print(temp)
    if len(temp)==20:
        odd.append(temp[0])
print(sum(odd))