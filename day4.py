
codes=[]
validcodes=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
f=open("day4input.txt","r")
count=0
code=[]
for line in f:
    if line!="\n":
        temp=line.split()
        code.extend(temp)
    else:
        codes.append(code)
        count+=1
        code=[]
f.close()

novalid=0
for k in codes:
    valid={}
    for d in k:
        t=d.split(":")
        valid[t[0]]=t[1]
    
    x=0
    for key in valid:
        if key in validcodes:
            x+=1
    numvalid2=0
    if x==7:
        if int(valid["byr"])>=1920 and int(valid["byr"])<=2002:
            numvalid2+=1
        if int(valid["iyr"])>=2010 and int(valid["iyr"])<=2020:
            numvalid2+=1
        if int(valid["eyr"])>=2020 and int(valid["eyr"])<=2030:
            numvalid2+=1
        if valid["hgt"][len(valid["hgt"])-2:]=="in":
            if int(valid["hgt"][:len(valid["hgt"])-2])>=59 and int(valid["hgt"][:len(valid["hgt"])-2])<=76:
                numvalid2+=1
        elif valid["hgt"][len(valid["hgt"])-2:]=="cm":
            if int(valid["hgt"][:len(valid["hgt"])-2])>=150 and int(valid["hgt"][:len(valid["hgt"])-2])<=193:
                numvalid2+=1
        if valid["hcl"][0]>="#" and len(valid["hcl"])==7:
            numvalid2+=1
        if valid["ecl"]in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            numvalid2+=1
        if len(valid["pid"])==9 :
            numvalid2+=1
        if numvalid2==7:
            novalid+=1
        
    
        
print(novalid)

