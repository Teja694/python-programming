num=input("enter the number by space:")
list1=num.split( )
print(list1)
count=0
for number in list1:
    count+=1
for i in range(count):
    list1[i]=int(list1[i])
max=list1[0]
for i in range(count):
    if max<list1[i]:
        max=list1[i]
print("maximum number is",max)
min=list1[0]
for i in range(count):
    if min>list1[i]:
        min=list1[i]
print("minimum number is",min)
    
        
