pizza=input("enter the size of the pizza [s/l/m]")
bill=0
if pizza=='s' or pizza=='S':
    bill=100
    print("price is 100")
if pizza=='l' or pizza=='L':
    bill=200
    print("price is 200")
if pizza=='m' or pizza=='M':
    bill=150
    print("price is 150")
pepper=input("you want pepper")
if pepper=='y' or pepper=='Y':
 if pizza=='s' or pizza=='S':
     bill+=30
 else:
     bill+=50
cheese=input("you want cheese")
if cheese=='y' or cheese=='Y':
  bill+=20
  print(f"the total bill is {bill}")
