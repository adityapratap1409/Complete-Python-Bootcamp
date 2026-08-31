'''for i in range (1,6):
    print(i)
else:
    print('the number greater than 6')   
for i in range(1,4):
    for j in range(4,7):
        print(i*j)'''
n=eval(input("enter a "))
for i in range(1,n,1):
    if(i%5==0 and i%10!=0):
        print(i)
