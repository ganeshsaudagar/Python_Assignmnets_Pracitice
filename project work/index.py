print("------->>WELCOME TO THE FOOD ORDERING APP<<--------")
print("ENTER  1 FOR ADMIN \nENTER 2 FOR USER")

choice=int(input("ENTER YOUR OPTION"))

if choice==1 or choice==2:
    if choice==1:
        print("Welcome to the ADMIN")
    elif choice ==2:
        print("welcome to the USER")
else:  
    print("please enter the valid option")  

