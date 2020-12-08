nums=[]
f=open("day3input.txt","r")
for line in f:
    nums.append(line.strip("\n")*130)

f.close()
print(len(nums))
print(nums[0])

#print(nums)
def traverse(a,b):
    trees=0
    line=0
    k=0
    while line<len(nums):
        #print(nums[line][k])
        if nums[line][k]=="#":
            trees+=1
        line+=b
        k=k+a
    return trees
print(traverse(3,1)*traverse(1,1)*traverse(5,1)*traverse(7,1)*traverse(1,2))
