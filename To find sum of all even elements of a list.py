## Find the sum of all even numbers in a given list

a=[]
b=int(input("Enter the No. of elements you want to put in list:"))
for i in range(b):
    b=int(input("Enter element"))
    a.append(b)

print("List you entered:",a)

c=[]
for i in a:
    if i%2==0:
        c.append(i)
d=sum(c)
print("even elements are:",c)
print("Sum of even elements of the list is:",d)
    
    
