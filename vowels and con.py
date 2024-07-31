Vcount = 0
Ccount = 0
Str = "saveetha school of Engineering"
str = Str.lower()

for i in range(0,len(Str)):
    if Str[i] in "aeiou":
        Vcount = Vcount + 1
    elif Str[i].isalpha():
        Ccount = Ccount + 1

print("The total no. of vowels:", Vcount)
print("The total no. of consonants:", Ccount)

if Vcount > Ccount:
    print("The vowels are more")
else:
    print("The consonants are more")
