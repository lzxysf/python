# coding=utf-8
# 记得在if和else语句后边加冒号
a = 5
if a < 10:
    print('a < 10')
elif a > 10 and a < 20:
    print('10<a<20')
else:
    print('other numbers')

# python中没有switch语句，条件判断语句只能用if

a = [1, 2, 3]
b = a if len(a) != 0 else ""
print (b)

c = []
d = c if len(c) != 0 else "空列表"
print(d)

nums = [1, 5, 34, 56, 13, 78]
even = []
odd = []
while len(nums) > 0:
    num = nums.pop()
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)
print(nums)
print(even)
print(odd)


def bubble_sort(arr):
    num = len(arr)
    for j in range(num-1):
        for i in range(num-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [6, 2, 78, 34, 66, 68, 0, 43, 66]
bubble_sort(arr)
print(arr)