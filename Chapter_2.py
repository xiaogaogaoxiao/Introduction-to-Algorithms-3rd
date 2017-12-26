# -*- coding: utf-8 -*-
"""
Spyder Editor

copy right: NG wang (Qingsong Wang)
email: 172034046@qq.com // nothing2wang@hotmail.com

This is a temporary script file.

Introduction To Algorithms  3rd Edition

"""


################################################################
'page_18'


'This insertion sort functon is sorted by increasing sort'


def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A
    
########    
#example:
    A=[3,1,2,6,5,4,8,7]
    insertion_sort(A)
    
###############################################################

' P_22---2.1-2'

'This insertion sort function is sorted by decreasing sort'

def insertion_sort_de(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]<key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A
    
#########    
#example:
    A=[3,1,2,6,5,4,8,7]
    insertion_sort_de(A)
    
##############################################################
'P_22-----2.1-3'

def find_element(a,A):
    i='not in list'
    for j in range(1,len(A)):
        if a==A[j]:
            i=j
            return i
    return i
    
########    
#example:
    a=2,A=[2,3,4,7,8]
    find_element(a,A)
    a=9,A=[2,3,4,7,8]
    find_element(a,A)
    
###########################################################
'P_22----2.1-4'
'only work for the same length'

def add_two_n_binary_integer(A,B):
    carry=0
    C=list(range(len(A)+1))
    for i in range(len(A)-1,-1,-1):
        C[i+1]=(A[i]+B[i]+carry) % 2
        if A[i]+B[i]+carry>=2:
            carry=1
        else:
            carry=0
    C[0]=carry
    return C
    
#######
#example:
    A[1,1,1],B=[1,1,1]
    add_two_n_binary_integer(A,B)

##############################################################
'P_29----2.2-2'

def selection_algorithm(A):
    for i in range(0,len(A)):
        min_int=i
        for j in range(i+1,len(A)):
            if A[j]<A[min_int]:
                A[min_int],A[j]=A[j],A[min_int]
    return A
    
########    
#example:
    A=[3,1,2]
    selection_algorithm(A)

####################################################

'P_31----MERGE(A,p,q,r)'


def merge_two_sorted_list(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)

    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    L[n1]=10000
    R[n2]=10000
    #return L,R
    i=0
    j=0

    for k in range(p,r+1):
        if i<=n1 and j<=n2:
            if L[i]<=R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
    return A
    
########
#example:            
    A=[2,4,5,7,1,2,3,6]       
    merge_two_sorted_list(A,0,3,7)  
  
###########################################################
'P_34----MERGE_SORT(A,p,r)'

def merge_two_sorted_list(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)

    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    L[n1]=10000
    R[n2]=10000
    #return L,R
    i=0
    j=0

    for k in range(p,r+1):
        if i<=n1 and j<=n2:
            if L[i]<=R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
                
def Merge_Sort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        merge_two_sorted_list(A,p,q,r)
    return A
    
#######
#example:
    A=[2,4,5,7,1,2,3,6] 
    Merge_Sort(A,0,7)
    
#########################################################
'P_37---2.3-2'

def Merge_two_sorted_method2(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    #return L,R
    i=0
    j=0
    k=p
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    if i==n1:
        for m in range(j,n2):
            A[k]=R[m]
            k+=1
    if j==n2:
        for m in range(i,n1):
            A[k]=L[m]
            k+=1
    return A
    
#######   
#example:
    A=[2,4,5,7,1,2,3,6,8]
    Merge_two_sorted_method2(A,0,3,8)  
    
############################################################# 

'P_39----2.3-5'

def BinSearch_in_sorted_list(A,a,b,v):
    'A is the sorted list,'
    'a,b are index range'
    'v is the element that we should to find out'
    m=int((a+b)/2)
    if v==A[m]:
        return m
    elif v<A[m]:
        return BinSearch_in_sorted_list(A,a,m-1,v)
    else:
        return BinSearch_in_sorted_list(A,m+1,b,v)
        
########
#example:
    A=[1, 2, 3, 4, 5, 6, 7, 8]
    BinSearch_in_sorted_list(A,0,7,3)
 
################################################################

'P_39----2.3-7'

'A is a sorted list in increase, A[i]+A[j]=s exists?'

def def_cost_is_nlogn(A,s):
    i=0
    j=len(A)-1
    while i<j:
        if (A[i]+A[j])==s:
            return True
        if (A[i]+A[j])<s:
            i=i+1
        if (A[i]+A[j])>s:
            j=j-1
    return False

#######
#example:
    A=[1,2,3,4,5]
    def_cost_is_nlogn(A,5) 
    def_cost_is_nlogn(A,10)   

#####################################################################

'P_40----2-2'

def Bubble_Sort(A):
    for i in range(0,len(A)-1):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A

########    
#example:
    A=[5,4,2,1,3]
    Bubble_Sort(A)
 
#########################################################################

'P_42----2-4-d'

def M_Merge(A,p,q,r):
    inv=0
    n1=p-q+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    i=0
    j=0
    k=p
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            inv=inv+j
            j+=1
        k+=1
    if i==n1:
        for m in range(j,n2):
            A[k]=R[m]
            k+=1
    if j==n2:
        for m in range(i,n1):
            A[k]=L[m]
            inv=inv+n2
            k+=1
    return inv

def M_Merge_Sort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        left=M_Merge_Sort(A,p,q)
        right=M_Merge_Sort(A,q+1,r)
        inv=M_Merge(A,p,q,r)+left+right
        return inv
    return 0

###########
#example:
    A=[2,3,8,6,1]
    M_Merge_Sort(A,0,4) 
    
#################################################################3
'P_42----2-4.d'

def count_invserse(A):
    count=0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                count+=1
    return count

###########
#example
A=[2,3,8,6,1]
count_invserse(A)

##############################################################
'''
That is all of the python code for chapter two
Introduction to Algorithms  Third Edition
'''                

'''
copy right: Qingsong Wang (NG Wang)
    
    
    
