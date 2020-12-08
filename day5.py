
codes=[]

f=open("day5input.txt","r")

for line in f:
    codes.append(line.strip("\n"))

f.close()


print(codes)
maximum=0
for code in codes:
    row=code[:7]
    col=code[7:]
    #print(row)

    first=0
    last=127
    for k in range(7):
        test=row[k]
        if test=="F":
            mid=(last-first)//2
            last=last-mid-1

        else:
            mid=(last-first)//2
            first=mid+first+1
    rownum=first
    first=0
    last=7
    for k in range(3):
        test=col[k]
        if test=="L":
            mid=(last-first)//2
            last=last-mid-1

        else:
            mid=(last-first)//2
            first=mid+first+1
    colnum=first
    seat=colnum+(rownum*8)
    if seat>maximum:
        maximum=seat

print(maximum)
