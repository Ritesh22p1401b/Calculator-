print("write 'enter' to do calculations \n press 1 for addition \n press 2 for subtraction \n enter 3 for multiply \n Enter 4 for Division \n Enter 5 for solving Expressions \n write exit to exit")
init=input("Write Enter to do calculations:")
init=init.lower()
if init=="enter":
    while True:
        n=input("Enter the above Numbers for calculation:")
        if n=="exit":
            print("Thankyou for using cal(x)")
            break

        if n=="1":
            a=int(input("Enter the first number:"))
            b=int(input("Enter the second number:"))
            c=a+b
            print(f"Addintion:{c}")
        elif n=="2":
            a=int(input("Enter the first number:"))
            b=int(input("Enter the second number:"))
            c=a-b
            print(f"Subtraction:{c}")
        elif n=="3":
            a=int(input("Enter the first number:"))
            b=int(input("Enter the second number:"))
            c=a*b
            print(f"Multiplication:{c}")
        elif n=="4":
            a=int(input("Enter the first number:"))
            b=int(input("Enter the second number:"))
            c=a/b
            print(f"Division:{c}")
        elif n=="5":
            x=eval(input("Enter the expression:"))
            print(f"Result:{x}")
        else:
            print("Enter the above method only")          

