#class: 1-3 or 5-7
#row: 6-11 or 33-44
#seat: 13-40 or 45-50
class1=[1,2,3,5,6,7]
row1=[6,7,8,9,10,11,33,34,35,36,37,38,39,40,41,42,43,44]
seat1=[]
for k in range(13,41):
    seat1.append(k)
for k in range(45,51):
    seat1.append(k)
myticket=[7,1,14]
nearby=[]
f=open("day16input1.txt","r")
for line in f:
    temp=line.split(",")
    for k in range(len(temp)):
        temp[k]=int(temp[k])
    nearby.append(temp)
print(nearby)
odd=0
for k in range(len(temp)):
    for ticket in nearby:
        num=ticket[k]
        print(num)
        if num in seat1:
            print("seat",num)
        if num in row1:
            print("row",num)
        if num in class1:
            print("class",num)
        if num not in class1 and num not in row1 and num not in seat1:
            print("odd",num)
            odd+=num
        
print(odd)