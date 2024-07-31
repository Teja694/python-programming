n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
if n1>n2:
    smaller=n2
else:
    smaller=n1
l=[]
for i in range(1,smaller+1):
    if n1%i==0 and n2%i==0:
     g=i
print(g)
if n1>n2:
    greater=n1
else:
    greater=n2
l=[]
while(True):
    if greater%n1==0 and greater%n2==0:
        lcm=greater
        break
    greater+=1
print(lcm)

