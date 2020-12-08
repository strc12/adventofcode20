nums=[]
f=open("nums.txt","r")
for line in f:
    nums.append(int(line))
print(nums)
f.close()
for k in range(0,len(nums)):
    for j in range(0,len(nums)):
        for l in range(0,len(nums)):
            if nums[k]+nums[j]+nums[l]==2020:
                print(nums[k],nums[j],nums[l])
                print(nums[k]*nums[j]*nums[l])
