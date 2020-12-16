input1=[19,20,14,0,9,1]
input0=[0,3,6]
turn=1
spoken=[19,20,14,0,9,1]
spokpos={19:0,20:1,14:2,0:3,9:4}
for k in range(len(spoken)-1,30000005):
    lastnumber = spoken[len(spoken)-1]
    #print("lastnumber",lastnumber)
    if lastnumber not in spokpos:
        spokpos[lastnumber]=k
        spoken.append(0)
        #print(spoken,"0")
        #print(spokpos,"0")
    else:
        newnum=k-spokpos[lastnumber]
        #print("newnum",newnum)
        spokpos[lastnumber]=k
        spoken.append(newnum)
        #print(spoken)
        
        #print(spokpos)
print(spoken[29999999])

