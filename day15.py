input1=[19,20,14,0,9,1]
input0=[0,3,6]
turn=1
spoken=[0,3,6]
spokpos={0:1,3:2,6:3}
for k in range(3,20):
    lastnumber = spoken[len(spoken)-1]
    spokpos[k-spokpos[lastnumber]]=k
    #print(lastnumber)
    prev=spoken[:len(spoken)-1]
    if lastnumber not in spoken[:len(spoken)-1]:
        print(lastnumber)
        spoken.append(0)    
    else:
        print(spokpos[lastnumber],k,k-spokpos[lastnumber],lastnumber)
        spoken.append(k-spokpos[lastnumber])
        
        #spokpos[]
    print(spokpos)
    print(spoken)
    #    nextspoken=0
#print (spoken)
print(spoken[1990:])

