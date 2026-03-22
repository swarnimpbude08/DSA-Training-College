
1. https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        original = x
        reverse = 0
        
        while x != 0:
            digit=x % 10
            reverse= reverse*10+digit
            x= x//10
        
        return original==reverse


2. https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        sum=0
        
        for i in accounts:
            sum=0
            for j in range(len(i)):
                sum=sum+i[j]
                wealth.append(sum)
        return max(wealth)
        


3. https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
N=int(input())
A=list(map(int,input().split()))
ten=1000000007
sum=1
for x in A:
    sum=(sum*x)%ten
print(sum)


4. https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)

*Magic Square Problem*
def magic_square_3x3():
    n = 3
    magic = [[0]*n for _ in range(n)]
    num = 1
    i, j = 0, n//2 
    while num <= n*n:
        magic[i][j] = num
        num += 1
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic
square = magic_square_3x3()
for row in square:
    print(row)


5. https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total - max_val
    max_sum = total - min_val


6. https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
tallest = max(candles)
    count = candles.count(tallest)
    return count


7. https://www.hackerrank.com/challenges/time-conversion/problem
period = s[-2:]      # AM or PM
    time_part = s[:-2]   # hh:mm:ss
    hour = int(time_part[:2])
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time_part[2:]}"
