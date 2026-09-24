import numpy as np
from array import *
new_arr=np.array(['a','s','k','p','y','t','y','o','n'])
rev_arr=np.flip(new_arr)
for i in new_arr:
    print(i, end=" ")
print()
for i in rev_arr:
    print(i, end=" ")
print()
rev2_arr=np.flipud(rev_arr)
for i in rev2_arr:
    print(i, end=" ")
in_arr=np.array([0,1,1,2,3,4,5,6,5,7,8,9,4,6,7,8,9,10])
n=len(in_arr)
print(n)
if n==0 or n==1:
   print(n)
temp=in_arr.tolist()
print(temp)
j=0
for i in range (0,n-1):
   if in_arr[i]!=in_arr[i+1]:
      temp[j]=in_arr[i+1]
      j+=1
temp[j]=in_arr[n-1]
j+=1
n=j
for i in range (n):
   print("%d"%(temp[i]),end=" ")
in_arr1=np.sort(in_arr)
unique_ele=[]
if in_arr1.size>0:
    print('\n''Array size',in_arr1.size)
    unique_ele.append(in_arr1[0])
    for i in range(1, in_arr1.size):
     if in_arr1[i]!=unique_ele[-1]:
        unique_ele.append(in_arr1[i])
arr=np.array(unique_ele)
print(arr)
def kthSmallest (arr,n,k):
 l=arr.tolist()
 l.sort()
 arr=array('i',l)
 return arr[k-1]
my_arr=array('i',12,3,5,7,19,19,8,10,4,11)
length=len(my_arr)
kthelement=4
print('Kth smallest element is',kthsmallest(my_arr,length, kthelement))