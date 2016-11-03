#-*- coding:utf-8 -*-
#author:Dganzh

def merge(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

def merge1(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1]
    i=j=0
    for k in range(p,r+1):
        print(k,L)
        if k>0 and A[k-1]==L[-1]:

            A[k:]=R[j:]
            print(L)
        elif k>0 and A[k-1]==R[-1]:
            A[k:]=L[i:]
            print(R)
        print('now', L)
def merge_sort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge1(A,p,q,r)




from QuickSort import A

if __name__=="__main__":
    merge_sort(A,0,len(A)-1)
    print(A)



