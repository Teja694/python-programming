name=input("enter the name:")
name1=input("enter the second name:")
str1=name.lower()
str2=name1.lower()
combine_string=str1+str2
t=combine_string.count('t')
r=combine_string.count('r')
u=combine_string.count('u')
e=combine_string.count('e')
true=t+r+u+e
l=combine_string.count('l')
o=combine_string.count('o')
v=combine_string.count('v')
e=combine_string.count('e')
love=l+o+v+e
true_love=int(str(true)+str(love))
print(true_love)
if true_love<80:
    print("love is moderate")
elif true_love>90:
    print("love is strong")
else:
    print('love is weak')
