name1=input("enter the name:")
name2=input("enter the name:")
combine=name1+name2
lower_case=combine.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('0')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e

true_love=true+love
print(f"you love percentage is{true_love}")

if true_love<10 or true_love>90:
 print("bod is strong")
else:
 print("you bond is not strong")


