# coding=utf-8
# 二分查找是一种搜索到算法
# 可以使用二分查找的前提是，序列是有序的
# 下面分别使用了迭代方法和普通方法进行二分查找
# 迭代时，退出的条件是，列表的长度num为0，注意不是为None，因为空列表也不是None的
# 普通方法时，退出的条件是，start > end, 此时退出


def binary_search1(alist, target):
    num = len(alist)
    if num == 0:
        return -1
    mid = num//2
    if alist[mid] == target:
        return True
    elif target < alist[mid]:
        return binary_search1(alist[:mid], target)
    else:
        return binary_search1(alist[mid+1:], target)


def binary_search2(alist, target):
    num = len(alist)
    start = 0
    end = num - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == target:
            return mid
        elif target < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def main():
    alist = [0, 1, 2, 3, 4, 7, 9, 11]
    print(binary_search1(alist, 9))
    print(binary_search2(alist, 9))


if __name__ == '__main__':
    main()
