lower = 2000
upper = 3200

for num in range(lower, upper +1):
    if (num%7) == 0 and (num%5 !=0):
        print(num)