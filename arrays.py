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
my_array.insert(mid,123343242)
for i in my_array:
    print(i, end=" ")