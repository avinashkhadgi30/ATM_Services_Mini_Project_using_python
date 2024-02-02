print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" \t \t Project Created by Avinash")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t \t \tHello Welcome to My ATM")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    restart =()
    #balance = 25000
    try:
        pin = int(input("Please enterd your 4 digit pin :-"))
        if pin == 1234:
            balance = 25000
            print(" Welcome \n name:-avinash khadgi\n you have enterd correct pin")
        
        elif pin == 2345:
            balance = 30000
            print(" Welcome \n name:-shraddha latkar\n you have enterd correct pin")
    
        elif pin == 3456:
            balance = 40000
            print(" Welcome \n name:-vipul margade\n you have enterd correct pin")
    
        elif pin == 4567:
            balance = 50000
            print(" Welcome \n name:-ruchika shede\n you have enterd correct pin")
    
        elif pin == 5678:
            balance = 60000
            print(" Welcome \n name:-ankush nag\n you have enterd correct pin") 
            
        else:
            print("sorry You have enterd wrong pin! please try again")
            continue
            #break
      
        while True:
            print("\t Please Press 1 for your balance\t")
            print("\t Please Press 2 to make a withdraw\t")
            print("\t Please Press 3 to deposit\t")
            print("\t Please Press 4 to Exit\t")
            try:
                option = int(input("What would you like to choose ? :-"))
                if option == 1:
                    print("Your balace is $",balance)
                    restart = input("Would you like to go back ? ")
                    if restart in ('n','NO','no','N'):
                        print("Thank you!!!")
                        break
                elif option == 2:
                    withdraw = float(input("How much would you like to withdraw ? \n"))
                    if withdraw < balance:
                        balance = balance - withdraw
                        print("\nYour balance is now $", balance)
                        print("\ncollect your cash!!")
                        restart = input("Would you like to go back ? ")
                        if restart in ('n','NO','no','N'):
                            print("Thank you!!!")
                            break        
                    else:
                        print("sorry!! you don't have sufficient balance ")    
                        restart = input("Would you like to go back ? ")
                        if restart in ('n','NO','no','N'):
                            print("Thank you!!!")
                            break
                elif option == 3:
                    deposit = float(input("How much would you like to deposit in ?"))
                    balance = balance + deposit
                    print("you have deposited sucessfully")
                    print("Your balance is now $ \n",balance)
                    restart = input("Would you like to go back ? ")
                    if restart in ('n','NO','no','N'):
                        print("Thank you!!!")
                        break        
                
                elif option == 4:
                    exit(0)
                else:
                    print("Please enterd a correct choice.\n")
                    restart = ('y')
            except ValueError as message:
                print("Please enter correct choice",message)        
        else:
            print("You have enterd wrong pin")
    except ValueError as message:
        print("Please enter correct pin",message)        
        
        
