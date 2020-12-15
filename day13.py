f=open("day13input.txt","r")
target=int(f.readline())
routes=f.readline().split(",")
print(target)
print(routes)
outs=[]
for route in routes:
    if route!="x":
        a=(target//int(route))+1
        b=target%int(route)
        d=target-(a*int(route))
        outs.append([a*int(route),int(route),abs(d)])
mini=999999999999
for k in outs:
    if k[2]<mini:
        mini=k[2]
        dist=k[0]
        rt=k[1]
print(mini*rt)
