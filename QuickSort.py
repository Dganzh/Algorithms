#-*- coding:utf-8 -*-
#author:Dganzh

def partion(A,p,r):
    key=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<key:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_sort(A,p,r):
    if r>p:
        q=partion(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

A=[5,2,2,6,8,0,4,6,3,2,9,5,0]
if __name__=='__main__':
    quick_sort(A,0,len(A)-1)
    print(A)  #[0, 0, 2, 2, 2, 3, 4, 5, 5, 6, 6, 8, 9]
