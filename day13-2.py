f=open("day13input1.txt","r")
routes=(f.readline().split(","))
print(routes)
maxa=1
for k in range(len(routes)):
    if routes[k]!="x":
        routes[k]=int(routes[k])
        maxa=maxa*routes[k]
count=0
bob=maxa
found=False
while found==False:
    x=0
    for count in range(len(routes)):
        for route in routes:
            if route!="x":
                x=x+(bob+count)%route
            
    bob+=1
    if x==0:
        found=True
        print(bob)

count=0

for route in routes:
    if route!="x":
       print((bob+count)%route)
    count+=1