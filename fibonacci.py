def Fibonacci(n):
    if n<0:
        print("invalid")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
num=int(input("enter the number= "))
for i in range(num):
 print(Fibonacci(i))
