#first n sum using loops
n=int(input("Enter upper limit "))
total_sum=0
for i in range (1,n+1):
    total_sum+=i
print('Sum of numbers using loops: ',total_sum)
print('Average using loops ',total_sum/n)
#using formula 
formula_sum=n*(n+1)/2
print('Sum of numbers using formula: ',formula_sum)
print('Average using formula ',formula_sum/n)
#using sum function on the individual numbers of the list 
list_sum=0
list=[1,2,3,4,5,6,7,8,9,10]
for num in list:
    list_sum+=num
print('Sum of list using sum function ',list_sum)
print('Average of list using sum function ',list_sum/len(list))
#using the sum function on the list as a whole
list_function_num=sum(list)
print('Sum of list using sum function directly on the list ',list_function_num)
print('Average of list using sum function directly on the list ',list_function_num/len(list))