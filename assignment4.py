#NUMBER THAT ARE DIVISIBLE BY 3 OR 12 TILL 50

for i in range(1, 50):
    if i %3==0:
        pass
    elif i %12==0:
        break
    else:
        continue
    print(i)
