# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:23:55 2016

@author: Vinayak11
"""
import pdb

def merge(A):
    left=0
    right=len(A)-1
    mid=(left+right)/2
    L=A[left:mid+1]
    R=A[mid+1:right+1]
    pl=0
    pr=0
    output=[]
    while len(L)>0 and len(R)>0:
        
        if L[pl]>R[pr]:
            output.append(R[pr])
            R=R[pr+1:]
        else:
            output.append(L[pl])
            L=L[pl+1:]
        
    output=output+L+R
#    pdb.set_trace()
    
    return output

def merge_sort(A,left,right):
 #   pdb.set_trace()
    if left==right:
        return A[left:right+1]
        

    mid=left + ((right-left)/2)
    
    B=merge_sort(A,left,mid)
#    pdb.set_trace()
    C=merge_sort(A,mid+1,right)
    D=B+C
    return merge(D)
#    pdb.set_trace()
    
    


    

            
         
    
