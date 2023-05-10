import math
print("Welcome to YourBank!")

def signin():
    global name #username
    global pin #password
    global cb #current balance

    name = str(input("Please create your username "))
    pin = str(input("Please create 5 digit pin "))
    if len(pin) == 5:
        pin = pin
    else:
        print("The pin has to be 5 digit")
        newpin = str(input("Please create your 5 digit pin again "))
        if len(newpin) != 5:
            print("The pin has to be 5 digits")
            signin()
        else:
            pin = newpin
    print("Thanks for creating your account!")
   

def forgotpin():
    recoverpin = str(input("Please create your new 5 digit pin "))
    if len(recoverpin) != 5:
        print("The pin has to be 5 digits")
        forgotpin()
    else:
        print("New pin has been stored, please log in")   
        pin = recoverpin 
          

def deposit_interest(p, r, t):
    # A = Pe^(rt) formula to calculate continuously compounded interest
    p = float(p) # Initial deposit
    r = float(r) # Interest rate
    t = float(t) # Time in years
    rt = r * t
    e = math.exp(rt)

    # Calculation

    a = p * e # Future value of investment
    return a

def login():
    # name1 represents username
    # pin1 represents user's pin

    name1 = str(input("Please enter your username "))
    pin1 = str(input("Please enter your pin "))

    #check if username and pin matches with created values

    if name1 == name and pin1 == pin:
        print("Welcome to YourBank"  + " " + name)
        print("Please choose menu down here")
        list_menu = ["1-Deposit", "2-Withdraw", "3-Transfer", "4-Check balance", "5-Deposit interest rate", "6-Calculate compound interest"]
        for h in list_menu:
            print(b)
        choose = int(input("Please enter the number of your choice"))
        d = 0 # deposit
        w = 0 # withdraw
        cb = 0 # current balance
        if choose == 1:
            d = int(input("Enter the amount you want to deposit"))
            cb = d
            print("Your current balance is" + " " + str(cb))
        elif choose ==2:
            w = int(input("Enter amount you want to withdraw"))
            if w > cb:
                print("Balance insufficient")
                login()
            else:
                cb = d - w
                print(str(w) + " " + "has been withdrawn from your account!" + " " + "New available balance is" + " " + str(cb))



    else:
        print("Incorrect username or pin, did you create your account?")
        list = ["1-Yes", "2-No"]
        for i in list:
            print(i)
        inp = int(input("Enter your choice below"))  
        if inp == 1:
            list2 = ["1-Do you want to attempt to log in again?", "2-Forgot pin?"]
            for b in list2:
                print(b)
            the_answer = str(input("Please enter your choice"))
            the_answer = int(the_answer)
            if the_answer == 1:
                login()
            elif the_answer == 2:
                forgotpin()
            else:
                print("Option not available")
                login()
        elif inp == 2:
            print("Please create account")
            signin()
            