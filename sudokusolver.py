# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:19:13 2020

@author: HP
"""
import sys

sys.setrecursionlimit(100000)


def check(a,nu,b,i1,j1):
    
    for ik in range(9):
        if a[i1][ik]==nu:
            return
    for ik in range(9):
        if a[ik][j1]==nu:
            return
        
    le=i1//3
    lu=j1//3
    for ik in range(int(le*3),int(le*3+3)):
        for ver in range(int(lu*3),int(lu*3+3)):
            if a[ik][ver]==nu:
                return 
                
    b.append(nu)



def check_2(a,i1,j1,nu):
    for ik in range(9):
        if a[i1][ik]==nu:
            return 0
    for ik in range(9):
        if a[ik][j1]==nu:
            return 0
    le=i1//3
    lu=j1//3
    for ik in range(int(le*3),int(le*3+3)):
        for ver in range(int(lu*3),int(lu*3+3)):
            if a[ik][ver]==nu:
                return 0
                
    return 1            
                
            
                     
    
def backtrack(a,arr,k):
    if k==len(arr):
        print("yes")
        print(a)
        sys.exit()
    i5=list1[k]
    j5=list2[k]
   
    
    for iu in arr[k]:
       
            
        z=check_2(a,i5,j5,iu)
        
        
        if z==1:
            a[i5][j5]=iu
            backtrack(a,arr,k+1)
    a[i5][j5]=0
            
    

                
    
def fit(a,c,b,arr):
    for i1 in range(9):
        for j2 in range(9):
            if a[i1][j2]==0:
                list1.append(i1)
                list2.append(j2)
                for num in c:
                    check(a,num,b,i1,j2)
                if len(b)==1:
                    a[i1][j2]=b[0]
                    list1.remove(i1)
                    list2.remove(j2)
                else:
                    arr.append(b)
                b=[]
                    
                                      
m=9
n=9
#a=[[int(input()) for x in range(n)]for x in range(m)]

arr=[]
list1=[]
list2=[]
cc=[]
c=[1,2,3,4,5,6,7,8,9]
a=[
   [5,4,9,0,0,0,0,0,0],
   [0,0,0,0,0,9,0,0,0],
   [0,0,1,0,0,8,2,0,0],
   [7,2,0,3,0,4,6,0,0],
   [0,0,0,0,0,0,0,7,5],
   [9,0,0,0,0,0,8,0,0],
   [3,0,0,0,0,0,0,6,0],
   [0,0,2,0,7,0,0,1,4],
   [0,7,0,0,0,0,0,0,0]]
for u in range(30):
    arr=[]
    b=[]
    list1=[]
    list2=[]
    fit(a,c,b,arr)
#or u in range(5):
  #  box(a)
    
print(a)
print("\n")
backtrack(a,arr,0)

print(a)

#print(len(list1))

