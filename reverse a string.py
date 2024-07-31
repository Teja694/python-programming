def reverse(s):
    str= " "
    for i in s:
        str= i + str
        return str
s="ukupirre yaniv"
print("the reversed string is : ",end=" ")
print(reverse(s))
