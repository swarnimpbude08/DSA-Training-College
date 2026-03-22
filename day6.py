#1. compare triplet
def compareTriplets(a, b):
    alice=0
    bob=0
    a=[]
    while len(a)!=0:
            if a[i]>b[j]:
                alice+=1
            elif a[i]<b[j]:
                bob+=1
            else a[i]==b[j]:
                pass
            i+=1
            j+=1
    return (alice,bob)

#2. sum big
def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            pass
    return alice,bob

#3. sum of diagonal of matrix
def diagonalDifference(arr):
    sum1=0
    for i in range(len(arr)):
        sum1+=arr[i][i]
    x=0
    b=len(arr[0])
    for i in range(len(arr)):
        x+=arr[i][b-1]
        b-=1
    return abs(sum1-x)

#4. plus minus
def plusMinus(arr):
    sum1=0
    diff=0
    zero=0
    for i in range(len(arr)):
        if arr[i]>0:
            sum1+=1
        elif arr[i]<0:
            diff+=1
        else:
            zero+=1
    print(sum1/(len(arr)))
    print(diff/(len(arr)))
    print(zero/(len(arr)))

#5. Shifiting array by n steps
n = int(input("Enter the number of Elements: "))
arr = []
for i in range(n):
    a = int(input("Enter the number: "))
    arr.append(a)
b = int(input("Enter the number of steps: "))
for _ in range(b):
    last_element = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_element
for i in range(n):
    print(arr[i])

    
