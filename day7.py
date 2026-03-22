# #1. Roy and Profile Picture
# l=int(input())
# n=int(input())
# for i in range(n):
#     w, h = map(int, input().split())
#     if w==l and h==l:
#         print("ACCEPTED")
#     elif w<l or h<l:
#         print("UPLOAD ANOTHER")
#     else:
#         print("CROP IT")

# #2. MONK array shifting
# import sys
# input_data = sys.stdin.read().split()
# if not input_data:
#     exit()
# t = int(input_data[0])
# current = 1
# for _ in range(t):
#     n = int(input_data[current])
#     k = int(input_data[current + 1])
#     current += 2
#     arr = list(map(int, input_data[current : current + n]))
#     current += n
#     if n > 0:
#         k %= n
#         for _ in range(k):
#             last_element = arr[n-1]
#             for i in range(n-1, 0, -1):
#                 arr[i] = arr[i-1]
#             arr[0] = last_element 
        
#     print(*(arr))

# #3.Toggle String
# # cahracter to ascii ord and ascii to character chr 
# a = input()
# b = ""
# for i in a:
#     if i.isupper():     
#         b += i.lower()  
#     else:
#         b += i.upper()  
# print(b)

# # swap case function s.swapcase() just flip samller and upper character

# #4. find majority of element
# n = int(input("Enter the number of Elements: "))
# a = []
# for i in range(n):
#     v = int(input("Enter the number: "))
#     a.append(v)
# for i in range(n):
#     if a.count(a[i])>=(n//2):
#         print(a[i])
#         break
        

#5. use 2 passes one from left to right and one from right to left to calculate product
n = int(input("Enter the number of Elements: "))
a = []
for i in range(n):
    v = int(input("Enter the number: "))
    a.append(v)
for i in range(n):
    b=1
    for j in range(n):
        if a[i]==a[j]:
            continue
        else:
            b*=a[j]
    a[i]=b
print(*a)
        
        
    
