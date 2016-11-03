#-*- coding:utf-8 -*-
#author:Dganzh

#找出元素x应该在数组A[p..r]中的位置
def binary_search(A,p,r,x):
    if p<r:
        q=int((p+r)/2)
        if x==A[q]:
            A.insert(q,x)
        elif x>A[q]:
            binary_search(A,q+1,r,x)
        else:
            binary_search(A,p,q-1,x)
    elif x<A[p]:
        A.insert(p,x)
    else:
        A.insert(p+1,x)


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j > 0 and A[j] > key:
            A[j + 1] = A[j]
            i -= 1
        A[i + 1] = key

def binary_insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A.pop(i)
        j = i - 1
        binary_search(A,0,j,key)
        print(A)


#A=[0, 0, 2, 2, 2, 3, 4, 5, 5, 6, 6, 8, 9]

#binary_search(A,0,len(A)-1,10)

A=[5,2,2,6,8,0,4,6,3,2,9,5,0]



binary_insertion_sort(A)


