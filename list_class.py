#The list data type can be called as a function, list-
#with no arguments it returns an empty list
l=list()
print(l)
#with a list argument it returns a shallow copy of the argument, and 
b=[2,3,4]
l=list(b)
print(l)
#with any other argument it attempts to convert the given object to a list
l1=list("ashok")
print(l1)
days=['monday','tuesday',3,4,5]
print(days)
list=[]
print(list)
print(len(days))
print(type(list))
#with dynamic input
# user_input=eval(input("enter list: "))
# print(user_input)
# print(l)
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
list=["cat","dog","cow",56.6,2826,"First Year"]
print(list)
print(list[2])
print(list[-2])
print(list[-1   ])
n=[1,2,3,4,5,6,7,8,9,10]
list=[]
list.append('a')
list.append('b')
list.append('c')
print(list)
list.insert(1,88)
list.insert(2,99)
print(list)

lis=[]
lim=int(input("Enter how many subjects you want to enter "))
for i in range(lim):
    lis.append(input('Enter subject: ').split())
    print("i=",lim," ",lis)
