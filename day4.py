# Functions, Lists and Strings Examples

# 1. Function to Add Two Numbers

def add(x, y):
    res = x + y
    return res



# 2. Arithmetic Operations Function


def arithmetic(x, y):
    res1 = x + y
    res2 = x - y
    res3 = x * y
    res4 = x / y
    return res1, res2, res3, res4


# Main Program


if __name__ == '__main__':

    print("Addition Function")
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    result = add(a, b)
    print("Sum =", result)

    print("\nArithmetic Operations")
    r1, r2, r3, r4 = arithmetic(a, b)
    print("Addition =", r1)
    print("Subtraction =", r2)
    print("Multiplication =", r3)
    print("Division =", r4)


# List 



print("\nList Creation")

ls = []
print(type(ls))

ls = list()
print(type(ls))


print("\nList Traversing")

ls = [11, 22, 33, 44, 55, 66]
print(ls)

# Using index
for i in range(len(ls)):
    print(ls[i])

# Direct iteration
for x in ls:
    print(x)


print("\nAppend Operation")

ls.append(77)
ls.append(88)
print(ls)
print("First element:", ls[0])


print("\nList Indexing")

print("First element:", ls[0])
print("Last element:", ls[-1])

ls[5] = 123
print("Modified list:", ls)


print("\nList Slicing")

ls = [11, 22, 33, 44, 55, 66]

print(ls[2:5])
print(ls[3:6])
print(ls[:6])
print(ls[2:])
print(ls[:])
print(ls[::1])
print(ls[::2])   # alternate elements
print(ls[::-1])  # reverse list



# String Examples


print("\nString Example")

s = "Mohit"

print("Substring:", s[2:4])

rev = s[::-1]
print("Reversed String:", rev)
