# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:34:51 2017

@author: nothing


Copy Right ： NG Wang (Qingsong Wang)
Email      : nothing2wang@hotmail.com 
"""

'''
This is the Chapter 4 for the book
codes for book and the excercises
'''

#######################################################################

'P_71 Find_Max_Crossing_Subarray'


def Find_Max_Crossing_Subarray(A,low,mid,high):
    left_sum=float("-inf")
    now_sum=0
    for i in range(mid, low-1, -1):
        now_sum=now_sum+A[i]
        if now_sum>left_sum:
            left_sum=now_sum
            max_left=i
    right_sum=float('-inf')
    now_sum=0
    for j in range(mid+1,high+1):
        now_sum=now_sum+A[j]
        if now_sum>right_sum:
            right_sum=now_sum
            max_right=j
    return max_left,max_right,left_sum+right_sum

########
#example:
    A=[-23,18,20,-7,12,-5,-22]
    Find_Max_Corssing_Subarray(A,0,3,6)

#########################################################################

'P_72 Find_Maximum_Subarray'


def Find_Max_Crossing_Subarray(A,low,mid,high):
    left_sum=float("-inf")
    now_sum=0
    for i in range(mid, low-1, -1):
        now_sum=now_sum+A[i]
        if now_sum>left_sum:
            left_sum=now_sum
            max_left=i
    right_sum=float('-inf')
    now_sum=0
    for j in range(mid+1,high+1):
        now_sum=now_sum+A[j]
        if now_sum>right_sum:
            right_sum=now_sum
            max_right=j
    return max_left,max_right,left_sum+right_sum

def Find_Maximum_Subarray(A,low,high):
    if low==high:
        return (low,high,A[low])
    else:
        mid=int((low+high)/2)
        (left_low,left_high,left_sum)=Find_Maximum_Subarray(A,low,mid)
        (right_low,right_high,right_sum)=Find_Maximum_Subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=Find_Max_Crossing_Subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
#############
#example:
    A=[-23,18,20,-7,12,-5,-22]
    Find_Maximum_Subarray(A,0,6)


######################################################################

'P_74----4.1-1'

def Find_Max_Crossing_Subarray(A,low,mid,high):
    left_sum=float("-inf")
    now_sum=0
    for i in range(mid, low-1, -1):
        now_sum=now_sum+A[i]
        if now_sum>left_sum:
            left_sum=now_sum
            max_left=i
    right_sum=float('-inf')
    now_sum=0
    for j in range(mid+1,high+1):
        now_sum=now_sum+A[j]
        if now_sum>right_sum:
            right_sum=now_sum
            max_right=j
    return max_left,max_right,left_sum+right_sum

def Find_Maximum_Subarray(A,low,high):
    if low==high:
        return (low,high,A[low])
    else:
        mid=int((low+high)/2)
        (left_low,left_high,left_sum)=Find_Maximum_Subarray(A,low,mid)
        (right_low,right_high,right_sum)=Find_Maximum_Subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=Find_Max_Crossing_Subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
            
#############
#example:
    A=[-23,-18,-20,-7,-12,-5,-22]
    Find_Maximum_Subarray(A,0,6)

################################################################

'P_74----4.1-2'


def n_square_time_Find_Maximum_Subarray(A,low,high):
    max_sum=float('-inf')
    for i in range(low,high+1):
        for j in range(i,high+1):
            cur_sum=sum(A[i:j+1])
            if cur_sum>max_sum:
                max_sum=cur_sum
                index_left=i
                index_right=j
    return (index_left,index_right,max_sum)

#########
#example:
    A=[-23,-18,20,7,-12,-5,-22]
    n_square_time_Find_Maximum_Subarray(A,0,6)        

#####################################################

'P_74----4.1-3'
'The crossover point is at around a length 20 array'

#####################################################

'P_75----4.1-5'

def Linear_Time_Maximum_Subarray(A):
    M=float('-inf')
    low_M=''
    high_M=''
    M_r=0
    low_r=0
    for i in range(0,len(A)):
        M_r+=A[i]
        if M_r>M:
            low_M=low_r
            high_M=i
            M=M_r
        if M_r<0:
            M_r=0
            low_r=i+1
    return (low_M,high_M,M)
    
#######
#example:
    A=[-23,-18,20,7,-12,-5,-22]
    Linear_Time_Maximum_Subarray(A)
    
    A=[]
    Linear_Time_Maximum_Subarray(A)

############################################################

'P_75--compute the product of two n-by-n matrix A and B'

def Square_Matrix_Multiply(A,B):
    C=[[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C

##############
#example:
    A=[[1,2],[3,4],[5,6]]
    B=[[1,2,3],[4,5,6]]
    Square_Matrix_Multiply(A,B)

##############################################################

'P_77----the Strassen algorithm'

def matrixproduct(a, b):  
    def matrixproductmask(mat_a, mat_b):  
        if mat_a.row == 1:  
            c11 = [[mat_a.mat_list[mat_a.row_list[0]][mat_a.col_list[0]] *  
                    mat_b.mat_list[mat_b.row_list[0]][mat_b.col_list[0]]]]  
            return Martrix(c11)  
        else:  
            mat_a11 = mat_a.divide('11')  
            mat_a12 = mat_a.divide('12')  
            mat_a21 = mat_a.divide('21')  
            mat_a22 = mat_a.divide('22')  
            mat_b11 = mat_b.divide('11')  
            mat_b12 = mat_b.divide('12')  
            mat_b21 = mat_b.divide('21')  
            mat_b22 = mat_b.divide('22')  
  
            s1 = mat_b12 - mat_b22  
            s2 = mat_a11 + mat_a12  
            s3 = mat_a21 + mat_a22  
            s4 = mat_b21 - mat_b11  
            s5 = mat_a11 + mat_a22  
            s6 = mat_b11 + mat_b22  
            s7 = mat_a12 - mat_a22  
            s8 = mat_b21 + mat_b22  
            s9 = mat_a11 - mat_a21  
            s10 = mat_b11 + mat_b12  
  
            p1 = matrixproductmask(mat_a11, s1)  
            p2 = matrixproductmask(s2, mat_b22)  
            p3 = matrixproductmask(s3, mat_b11)  
            p4 = matrixproductmask(mat_a22, s4)  
            p5 = matrixproductmask(s5, s6)  
            p6 = matrixproductmask(s7, s8)  
            p7 = matrixproductmask(s9, s10)  
  
            c11 = (p5 + p4 - p2 + p6)  
            c12 = (p1 + p2)  
            c21 = (p3 + p4)  
            c22 = (p5 + p1 - p3 - p7)  
  
            return matrixmerge(c11, c12, c21, c22)  
  
    mat_a = Martrix(a)  
    mat_b = Martrix(b)  
    product = matrixproductmask(mat_a, mat_b)  
    return product.mat_list  
  
def matrixmerge(c11, c12, c21, c22):  
    mat_list = []  
    for i in c11.row_list:  
        mat_list.append(c11.mat_list[i]+c12.mat_list[i])  
    for i in c21.row_list:  
        mat_list.append(c21.mat_list[i]+c22.mat_list[i])  
    return Martrix(mat_list)  
  
class Martrix(object):  
    def __init__(self, *args):  
        if len(args) == 1 and isinstance(args[0], list):  
            self.mat_list = args[0]  
            self.row = len(args[0])  
            self.col = len(args[0][0])  
            self.row_list = range(self.row)  
            self.col_list = range(self.col)  
  
    def __add__(self, mat2):  
        mat_list = [[self.mat_list[self.row_list[i]][self.col_list[j]]+mat2.mat_list[mat2.row_list[i]][mat2.col_list[j]]  
                     for j in range(self.col)] for i in range(self.row)]  
        return Martrix(mat_list)  
  
    def __sub__(self, mat2):  
        mat_list = [[self.mat_list[self.row_list[i]][self.col_list[j]]-mat2.mat_list[mat2.row_list[i]][mat2.col_list[j]]  
                     for j in range(self.col)] for i in range(self.row)]  
        return Martrix(mat_list)  
  
    def divide(self, block):  
        result = Martrix()  
        result.mat_list = self.mat_list  
        result.row = int(self.row/2)  
        result.col = int(self.col/2)
        dic = {'11': [self.row_list[:result.row], self.col_list[:result.col]],  
               '12': [self.row_list[:result.row], self.col_list[result.col:]],  
               '21': [self.row_list[result.row:], self.col_list[:result.col]],  
               '22': [self.row_list[result.row:], self.col_list[result.col:]]}  
        result.row_list = dic[block][0]  
        result.col_list = dic[block][1]  
        return result  

######################  
#example:
a = [[1,4,8,7],[5,7,9,13],[3,6,8,11],[-1,-3,5,3]]  
b = [[4,8,-12,5],[2,1,9,4],[12,45,-21,5],[5,-1,4,7]]  
c = matrixproduct(a, b)  
print(c)


#################################################################

'P_82----4.2-1'
S1 = 8 − 2 = 6
S2 = 1 + 3 = 4
S3 = 7 + 5 = 12
S4 = 4 − 6 = −2
S5 = 1 + 5 = 6
S6 = 6 + 2 = 8
S7 = 3 − 5 = −2
S8 = 4 + 2 = 6
S9 = 1 − 7 = −6
S10 = 6 + 8 = 14

P1 = 6
P2 = 8
P3 = 72
P4 = −10
P5 = 48
P6 = −12
P7 = −84

C11 = 48 − 10 − 8 − 12 = 18
C12 = 6 + 8 = 14
C21 = 72 − 10 = 62
C22 = 48 + 6 − 72 + 84 = 66

'So C=[[18,14],[62,66]]'

#########################################################

'P_82----4.2-2'
'The Strassen Algorithm for n-by-n matrix multiply'
import numpy as np
def Strassen(A,B):
    if np.size(A,0)==1:
        return A[0,0]*B[0,0]
    else:
        C=np.mat(np.zeros((np.size(A,0),np.size(A,1))))
            
        A11=A[:int(np.size(A,0)/2),:int(np.size(A,1)/2)]
        A12=A[:int(np.size(A,0)/2),int(np.size(A,1)/2):]
        A21=A[int(np.size(A,0)/2):,:int(np.size(A,1)/2)]
        A22=A[int(np.size(A,0)/2):,int(np.size(A,1)/2):]
        
        B11=B[:int(np.size(B,0)/2),:int(np.size(B,1)/2)]
        B12=B[:int(np.size(B,0)/2),int(np.size(B,1)/2):]
        B21=B[int(np.size(B,0)/2):,:int(np.size(B,1)/2)]
        B22=B[int(np.size(B,0)/2):,int(np.size(B,1)/2):] 
        
        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12
        
        P1 = Strassen(A11, S1)
        P2 = Strassen(S2, B22)
        P3 = Strassen(S3, B11)
        P4 = Strassen(A22, S4)
        P5 = Strassen(S5, S6)
        P6 = Strassen(S7, S8)
        P7 = Strassen(S9, S10)
        
        C[:int(len(C)/2),:int(len(C)/2)]=P5+P4-P2+P6
        C[:int(len(C)/2),int(len(C)/2):]=P1+P2
        C[int(len(C)/2):,:int(len(C)/2)]=P3+P4
        C[int(len(C)/2):,int(len(C)/2):]=P5+P1-P3-P7
    return C

#example:       
A = np.mat([[1,4,8,7],[5,7,9,13],[3,6,8,11],[-1,-3,5,3]])
B = np.mat([[4,8,-12,5],[2,1,9,4],[12,45,-21,5],[5,-1,4,7]])
Strassen(A,B)   

#######################################################################

'P_82----4.2-3'
' this is the strassen algorthm for n-by- matrix , where n not equals the power of 2'     
        
import numpy as np
import math
def Strassen(A,B):
    rows=np.size(A,0)
    clomns=np.size(A,1)
    if rows==1 and clomns==1:
        return A[0,0]*B[0,0]
    elif (math.log(rows,2) - int(math.log(rows,2))) !=0:
        
        n=2**(int(math.log(np.size(A,0),2))+1)
        #m=np.mat(zeros((n,n)))
        A_11=A
        A_12=np.mat(np.zeros((rows,n-clomns)))
        A_21=np.mat(np.zeros((n-rows,clomns)))
        A_22=np.mat(np.zeros((n-rows,n-clomns)))
        A=np.vstack((np.hstack((A_11,A_12)),np.hstack((A_21,A_22))))
        
#        A=np.vstack(np.hstack(A,np.mat(zeros((rows,n-clomns)))),np.hstack(np.mat(np.zeros((n-rows,clomns))),np.mat(np.zeros((n-rows,n-clomns))))
#        B=np.vstack(np.hstack(B,np.mat(zeros((rows,n-clomns)))),np.hstack(np.mat(np.zeros((n-rows,clomns))),np.mat(np.zeros((n-rows,n-clomns))))
        B_11=B
        B_12=np.mat(np.zeros((rows,n-clomns)))
        B_21=np.mat(np.zeros((n-rows,clomns)))
        B_22=np.mat(np.zeros((n-rows,n-clomns)))
        B=np.vstack((np.hstack((B_11,B_12)),np.hstack((B_21,B_22))))
        
        C=np.mat(np.zeros((n,n)))
        #C=np.mat(np.zeros((np.size(A,0),np.size(A,1))))
            
        A11=A[:int(np.size(A,0)/2),:int(np.size(A,1)/2)]
        A12=A[:int(np.size(A,0)/2),int(np.size(A,1)/2):]
        A21=A[int(np.size(A,0)/2):,:int(np.size(A,1)/2)]
        A22=A[int(np.size(A,0)/2):,int(np.size(A,1)/2):]
        
        B11=B[:int(np.size(B,0)/2),:int(np.size(B,1)/2)]
        B12=B[:int(np.size(B,0)/2),int(np.size(B,1)/2):]
        B21=B[int(np.size(B,0)/2):,:int(np.size(B,1)/2)]
        B22=B[int(np.size(B,0)/2):,int(np.size(B,1)/2):] 
        
        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12
        
        P1 = Strassen(A11, S1)
        P2 = Strassen(S2, B22)
        P3 = Strassen(S3, B11)
        P4 = Strassen(A22, S4)
        P5 = Strassen(S5, S6)
        P6 = Strassen(S7, S8)
        P7 = Strassen(S9, S10)
        
        C[:int(len(C)/2),:int(len(C)/2)]=P5+P4-P2+P6
        C[:int(len(C)/2),int(len(C)/2):]=P1+P2
        C[int(len(C)/2):,:int(len(C)/2)]=P3+P4
        C[int(len(C)/2):,int(len(C)/2):]=P5+P1-P3-P7
        

    else:
        C=np.mat(np.zeros((np.size(A,0),np.size(A,1))))
            
        A11=A[:int(np.size(A,0)/2),:int(np.size(A,1)/2)]
        A12=A[:int(np.size(A,0)/2),int(np.size(A,1)/2):]
        A21=A[int(np.size(A,0)/2):,:int(np.size(A,1)/2)]
        A22=A[int(np.size(A,0)/2):,int(np.size(A,1)/2):]
        
        B11=B[:int(np.size(B,0)/2),:int(np.size(B,1)/2)]
        B12=B[:int(np.size(B,0)/2),int(np.size(B,1)/2):]
        B21=B[int(np.size(B,0)/2):,:int(np.size(B,1)/2)]
        B22=B[int(np.size(B,0)/2):,int(np.size(B,1)/2):] 
        
        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12
        
        P1 = Strassen(A11, S1)
        P2 = Strassen(S2, B22)
        P3 = Strassen(S3, B11)
        P4 = Strassen(A22, S4)
        P5 = Strassen(S5, S6)
        P6 = Strassen(S7, S8)
        P7 = Strassen(S9, S10)
        
        C[:int(len(C)/2),:int(len(C)/2)]=P5+P4-P2+P6
        C[:int(len(C)/2),int(len(C)/2):]=P1+P2
        C[int(len(C)/2):,:int(len(C)/2)]=P3+P4
        C[int(len(C)/2):,int(len(C)/2):]=P5+P1-P3-P7
    return C[:rows,:clomns]

################
#example:
A = np.mat([[1,4,8,5,6,7],[1,4,8,5,6,7],[1,4,8,5,6,7],[1,4,8,5,6,7],[1,4,8,5,6,7],[1,4,8,5,6,7]])
B = np.mat([[4,8,-12,3,4,3],[4,8,-12,3,4,3],[4,8,-12,3,4,3],[4,8,-12,3,4,3],[4,8,-12,3,4,3],[4,8,-12,3,4,3]])
Strassen(A,B)  

##############################################################################################################################3

'P_83----4.2-7'

(a+bi)(c+di)=ac-bd+(cb+ad)i

we use:
    P1=(a+b)c=ac+bc
    P2=b(c+d)=bc+bd
    P3=(a-b)d=ad+bd
    
then:
    P1-P2 as the real part
    P2+p3 sa the imaginary part
    
################################################################

