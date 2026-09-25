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
# lis=[]
# lim=int(input("Enter how many subjects you want to enter "))
# for i in range(lim):
#     lis.append(input('Enter subject: ').split())
#     print("i=",lim," ",lis)
n.reverse()
print(n)
n.sort()
print(n)
n1=[1,14.25, 14,15.231]
n1.sort()
print(n1)
#1.Write a program to display unique vowels in the given word
vowels=['a','e','i','o','u']
word=input("enter a word to search for vowels ")
found=[]
ca=0;ce=0;ci=0;co=0;cu=0
for letter in word:
 if letter=='a' and ca==0:
        found.append('a')
        ca+=1
 if letter=='e' and ce==0:
       found.append('e')
       ce+=1
 if letter=='i' and ci==0:
       found.append('i')
       ci+=1
 if letter=='o' and co==0:
       found.append('o')
       co+=1
 if letter=='u' and cu==0:
       found.append('u')
       cu+=1
print(found)

