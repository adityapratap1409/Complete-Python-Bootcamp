'''x,y,z=map(int,input('Enter numbers: ').split(','))
print(x+y+z)
name = input("Enter your name: ")
print("Hello: " + name)
name = "Sam"
print("Hello {name}")'''
def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

print("Age: {}".format(20))
name = "Alex"
print("Hi %s" % name)
tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]
tomstotal=calculate_total(tom_exp_list)
joestotal=calculate_total(joe_exp_list)
print(tomstotal)
print(joestotal)