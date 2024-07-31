def count(s1, s2):
    c = 0  # counter variable
    j = 0

    for i in s1:
        if s2.find(i) >= 0 and j == s1.index(i):
            c = c + 1
        j = j + 1
    
    print("Matching char:", c)

s1 = "string"
s2 = "watch"

count(s1, s2)
 
