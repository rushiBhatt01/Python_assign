#NUMBER THAT ARE DIVISIBLE BY 3 OR 12 TILL 50

print("for numbers which are divisible by 3 or 12 choose:-divisible(by for)")
print("for numbers which are not divisible by 3 or 12 choose:-no_div(by while)")
loop=input("choose divisible or n_div:")
i=1
if(loop=="divisible"or "DIVISIBLE"):
    for i in range(1, 51):
        if i%3==0:
            pass
        elif i%12==0:
            break
        else:
            continue
        print(i)
    
    
elif(loop=="n_div"or"N_DIV"):
    
    while i<=50:
        if i%3==0:
           pass
        elif i%12==0:
            break
        else:
            print(i)
        
        i+=1
  
else:
    print("choose correct option")
