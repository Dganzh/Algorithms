#-*- coding:utf-8 -*-
#author:Dganzh

def bubble_sort(A):
    n=len(A)-1
    for i in range(n):
        for j in range(n,i,-1):
            print(j)
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
        print(A)

from QuickSort import A

if __name__=='main':
    bubble_sort(A)
