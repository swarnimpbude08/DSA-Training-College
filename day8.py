#1.Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
#2. FizzBuzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a.append("FizzBuzz")
            elif i%3==0:
                a.append("Fizz")
            elif i%5==0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a       

#3.Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=len(nums)
        b=[]
        sum=0
        i=0
        while a>0:
            sum+=nums[i]
            b.append(sum)
            i+=1
            a-=1
        return b

#4. only next larget 
n = int(input("Enter the number of Elements: "))
a = []
for i in range(n):
    v = int(input("Enter the number: "))
    a.append(v)
d=len(a)
c=d
b=[]
i=0
temp=0
while c>0:
    if temp<a[i]:
        temp=a[i]
    b.append(temp)
    c-=1
    i+=1
if c==0:
    b.append(-1)
b.remove(b[0])
print (*b)
                    
