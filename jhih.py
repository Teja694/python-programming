date=input("enter date to checked:")
c=date.split("/")
b=list(map(int,c))
input_year=(b[2])
if input_year%4==0 :
    if input_year%100==0 :
        if input_year%400==0:
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")
x=input_year%4
if x!=0:
 print("previous leap leap year:",input_year-x)
else:
 print("next leap year:",input_year+4)
        
