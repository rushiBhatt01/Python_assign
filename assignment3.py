

x=float(input("Enter first value :"))
y=float(input("Enter second value :"))
            
print("1) For Addition press + \n2) For Subtraction press -\n3) For Multiplication press * \n4) For Division press / \n")
num=(input("Enter your choice: "))
if num == "+":
                
            print("Addition is : ",(x+y))
elif num=="-":
            print("Subtraction is : ",(x-y))
elif num=="*" :
            print("Multiplication is : ",(x*y))
elif num=="/":
            print("Division is : ",(x/y))
else:
            print("Wrong choice")
            
            
