a=[]
b=[]
n1=int(input("enter the number:"))
for i in range(1,n1+1):
    c=int(input("enter the numbers:"))
    a.append(c)
print(a)
n2=int(input("enter the number:"))
for i in range(1,n2+1):
    d=int(input("enter the numbers:"))
    b.append(d)
print(b)
new=a+b
new.sort()
print(new)

