# 1. Check whether a number is even or odd
a = int(input("Enter number: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")

# 2. Find the largest of three numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y and x > z:
    print(x)
elif y > z:
    print(y)
else:
    print(z)

# 3. Check whether a number is positive, negative, or zero
a = int(input("Enter number: "))
if a > 0:
    print("number is positive")
elif a < 0:
    print("number is negative")
else:
    print("zero")

# 4. Check whether a number is divisible by both 3 and 5
a = int(input("Enter number: "))
if a % 3 == 0 and a % 5 == 0:
    print("Divisible by both")
else:
    print("not divisible")

# 5. Print numbers from 1 to N
n = int(input("Enter the range: "))
for i in range(1, n+1):
    print(i)

# 6. Print all even numbers from 1 to N
n = int(input("Enter range: "))
count = 2
while count <= n:
    print(count)
    count += 2

# 7. Calculate the sum of first N natural numbers
n = int(input("Enter n: "))
s = 0
for i in range(1, n+1):
    s += i
print(s)

# 8. Calculate the factorial of a number
n = int(input("Enter n: "))
f = 1
for i in range(1, n+1):
    f *= i
print(f)

# 9. Print the multiplication table of a number
n = int(input("Enter n: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 10. Count the number of digits in a number
n = int(input("Enter number: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)

# 11. Reverse a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    d = n % 10
    rev = rev*10 + d
    n //= 10
print(rev)

# 12. Check whether a number is palindrome
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    d = n % 10
    rev = rev*10 + d
    n //= 10
if temp == rev:
    print("it is palindrome")
else:
    print("it is not palindrome")

# 13. Find the sum of digits of a number
n = int(input("Enter number: "))
s = 0
while n > 0:
    d = n % 10
    s += d
    n //= 10
print(s)

# 14. Check whether a number is an Armstrong number
n = int(input("Enter number: "))
temp = n
s = 0
while n > 0:
    d = n % 10
    s += d**3
    n //= 10
if temp == s:
    print("it is armstrong")
else:
    print("it is not armstrong")

# 15. Print numbers divisible by 7 between 1 and N
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)
