# 1. Series Program



n = int(input("Enter value of n: "))
x = int(input("Enter value of x: "))

sum_series = 1
for i in range(1, n):
    sum_series = sum_series + (x ** i) / i

print("Series Sum =", sum_series)


# 2. Pattern Program


print("\nPattern 1")
for i in range(1, 5):      # rows
    for j in range(1, 5):  # columns
        print(i, end="")
    print()



# 3. Number Pattern


print("\nPattern 2")
n = 1
for i in range(1, 5):
    for j in range(1, 5):
        print(n, end="\t")
        n = n + 1
    print()



# 4. Alphabet Pattern


print("\nPattern 3")
n = 65   # ASCII value of 'A'

for i in range(1, 5):
    for j in range(1, 5):
        print(chr(n), end="\t")
        n = n + 1
    print()



# 5. Number Triangle Pattern


print("\nPattern 4")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(i, end="")
    print()


# -------------------------------
# 6. Star Pattern

print("\nPattern 5")
for i in range(1, 5):
    for j in range(5 - i):
        print("*", end="\t")
    print()
