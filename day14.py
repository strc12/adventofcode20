def db(denary):
    binary=""  
    while denary>0:  
    #A left shift in binary means /2  
        binary = str(denary%2) + binary  
        denary = denary//2  
    return(binary)
inst=[]
values={}

f=open("day14input1.txt","r")
for line  in f:
    t=line.split("=")
    #print(t)
    if t[0].strip()=="mask":
        mask=t[1].strip()
     #   print(mask)
    else:
        den=int(t[1])
        temp=t[0].split("[")
        t2=int(temp[1].strip("[")[::-2])
      #  print(den,t2)
        inst.append((den,t2))
        binnum=db(den)
        #print(binnum)
        value="0"*36
        lenbin=len(binnum)
        #print(lenbin)
        value=value[:35-lenbin+1]+binnum
        #print(mask)
        #print(value)
        out=""
        for k in range(len(mask)):
            if mask[k]=="X":
                out=out+value[k]
            elif mask[k]=="1":
                out=out+"1"
            else:
                out=out+"0"
        #print(out)
        values[t2]=int(out,2)
    #print(values)
tot=0
for value in values:
    tot=tot+values[value]
print(tot)
