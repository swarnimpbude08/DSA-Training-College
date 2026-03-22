# HackerRank and Python Practice Programs


# 1. Solve Me First (HackerRank)


def solveMeFirst(a, b):
    return a + b


print("Solve Me First")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
res = solveMeFirst(num1, num2)
print("Result:", res)



# 2. Simple Array Sum (HackerRank)


def simpleArraySum(ar):
    return sum(ar)


print("\nSimple Array Sum")
n = int(input("Enter number of elements: "))
ar = list(map(int, input("Enter elements: ").split()))

result = simpleArraySum(ar)
print("Sum of array:", result)



# 3. Find Maximum and Minimum


def maxmin(ar):
    largest = ar[0]
    smallest = ar[0]

    for i in ar:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    print("Largest:", largest)
    print("Smallest:", smallest)


print("\nMaximum and Minimum")
n = int(input("Enter range: "))
ar = []

for i in range(n):
    val = int(input("Enter number: "))
    ar.append(val)

maxmin(ar)



# 4. Types of Taking Input


print("\nDifferent Ways of Taking Input")

# 1. Single integer
# n = int(input())

# 2. Two integers
# a = int(input())
# b = int(input())

# 3. Two integers in one line
# a, b = map(int, input().split())

# 4. List input
# ls = list(map(int, input().split()))

# 5. Using eval
# arr = eval(input())


# 5. Remove Duplicates from List


def remove_duplicates(ar):
    unique = []
    for i in ar:
        if i not in unique:
            unique.append(i)
    return unique


print("\nRemove Duplicates")
n = int(input("Enter range: "))
ar = []

for i in range(n):
    val = int(input("Enter number: "))
    ar.append(val)

print("Array without duplicates:", remove_duplicates(ar))


# 6. Pattern Example


print("\nPattern Example")

i = 1
j = 10

while i < j:
    if i == 3 and j == 8:
        i = i + 1
        j = j - 1
        continue

    print(i, "\t", j)
    i = i + 1
    j = j - 1



# 7. Alternating Positive and Negative Numbers


print("\nAlternating Positive and Negative Numbers")

arr = [1, -2, 3, -4, -1, 4]

pos = []
neg = []

# Separate positive and negative numbers
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []
i = j = 0

# Arrange alternately
while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1

# Add remaining elements
result.extend(pos[i:])
result.extend(neg[j:])

print("Result:", result)
