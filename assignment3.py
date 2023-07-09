class Calculator:
    def calculate():
        n1=1
        while n1 == 1:
            print("\n This is menu driven program")
            print("1) For Addition press a \n2) For Subtraction press s \n3) For Multiplication press m \n4) For Division press d \n")
            num=(input("Enter your choice: "))
            if num == "a":
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Addition is : ",(x+y))
            elif num=="s":
                x=float(input("Enter first num :"))
                y=float(input("Enter second num :"))
                print("Subtraction is : ",(x-y))
            elif num=="m" :
                x=float(input("Enter first num :"))
                y=float(input("Enter second num :"))
                print("Multiplication is : ",(x*y))
            elif num=="d":
                x=float(input("Enter first num:"))
                y=float(input("Enter second num :"))
                print("Division is : ",(x/y))
            else:
                print("Wrong choice")
            n=input("If you want to continue press 1 \n otherwise press any key ")
            if n!="1":
                exit()
            n1=int(n)
            
c=Calculator.calculate()