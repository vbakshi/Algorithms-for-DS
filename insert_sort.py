# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def insertion_sort(A):
    i=1
    
    while i<len(A):
        j=i-1
        key=A[i]
         
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            A[j]=key
            j=j-1
            
        A[j+1]=key
        
        i=i+1
    
    return A
    