array = [16, 18, 27, 16, 23, 21, 19]
count = 0
for num in array:
    if num < 4:
        continue
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
print(num)
print("Number of Composite Numbers =", count)
