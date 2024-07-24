num=int(input("enter a number"))
temp=num
r=0
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    r=r*10+digit
    temp=temp//10
print(r)
print(sum)
