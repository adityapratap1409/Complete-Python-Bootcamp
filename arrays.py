from array import *
lst=[1,'ni',12.32,(1,'232',123.31235)]
print(lst)
arry=array('i',[1,2,3,4,5,6])
print(arry)
for i in arry:
    print(i,end=" ")
print()
arryunis=array('w',['a','b'])
print(arryunis)
for i in arryunis:
    print(i,end=" ")
print()
my_array=array('i',[1,2,3,4,5,6,7,8,9,76,52])
print(my_array)
for i in my_array:
    print(i, end=" ")
print()
# lst_input=[int(x) for x in input("Enter the elements: ").strip().split()]
# print(lst_input)
# arry_to_lst=array('i',lst_input)
# for i in arry_to_lst:
#     print(i,end=" ")
print()
print(len(arry))
print(len(arryunis))
print(len(my_array))
# print(len(lst_input))
# size=len(arry_to_lst)
# print("No of elements: %d" %size)
print(my_array[0])
print(my_array[-1])
print(my_array[:-2])
print(my_array[3: ])
print(my_array[2:5])
print(my_array[:])
print(my_array[::-7])
mid=int((len(my_array))/2)
my_array.insert(mid,12442)
for i in my_array:
    print(i, end=" ")
my_array.extend(arry)
print()
for i in my_array:
    print(i, end=" ")
print()
# new_list=[int(x) for x in input("Enter elements space seperated: ").strip().split()]
# my_array.fromlist(new_list)
# print()
for i in my_array:
    print(i, end=" ")
print()
l=my_array.tolist()
for i in my_array:
    print(i, end=" ")
print()
print(my_array.typecode)
my_array.reverse()
for i in my_array:
    print(i, end=" ")
print()
for i in range(len(my_array)-1,-1,-1):
    print(my_array[i], end=" ")
print()
print("Count is: ",my_array.count(2))
arr=[25,11,7,75,56,77,76,8]
min=arr[0]
for i in range(0, len(arr)):
    if(arr[i]<min):
        min=arr[i]
print(min)
print('Items are: ')
for i in arr:
    print(i, end=" ")