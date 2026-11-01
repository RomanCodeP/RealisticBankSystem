import os
import time
def user():
    print("---------- Welcome to the Roman's Bank ----------")
    optionlogin = input("would you like to 'login' or 'register'?")
    try:
        assert optionlogin in ("login", "register")
        if optionlogin == "register":
            register()
        elif optionlogin == "login":
            login()
    except AssertionError:
        os.system("cls")
        print("Error, You have to write 'login' or 'register'")


def login():
    loginuser = input("Enter your username: ")
    with open("usernames.csv", "r") as file:
        found = False
        for line in file:
            account = line.strip().split(",")
            if loginuser == account[0]:
                        found = True
                        userpassword = input("Enter the password: ")
                        if userpassword == account[1]:
                             global userfoundsystem
                             userfoundsystem = f"{loginuser}"
                             banksystem()
                        else:
                             print("the password is incorrect")  
        if not found:
             print("This user does not exist")

userfoundsystem = "notfound"
def banksystem():
     os.system("cls")
     with open("usernames.csv", "r") as file:
          for line in file:
                    account = line.strip().split(",")
                    if userfoundsystem == account[0]:
                         moneysystem = account[2]

     print("------------ Welcome " + userfoundsystem + " ------------")
     print("- You have: " + moneysystem)
     print("-")
     print("1 - Transfer")
     print("-")
     print("")
     print("-")
     option = int(input("Enter the number: "))
     if option == 1:
               try:
                    howmuch = int(input("how much would you like to transfer? "))
                    moneysystemvalid = int(account[2])
                    if 0 < howmuch <= moneysystemvalid:
                         print("valid")
                         transfername = input("How would you like to transfer? Enter the username: ")
                         found = False
                         accounts = []
                         with open("usernames.csv", "r") as file: ############################################
                              for line in file:
                                   transferdestin = line.strip().split(",")
                                   if transfername == transferdestin[0]:
                                        found = True
                                        print("You transfered", int(howmuch), "to", transfername) ##########
                                        numbertrans1 = int(transferdestin[2])
                                        finalnumber = int(numbertrans1) + howmuch
                                        transferdestin[2] = str(finalnumber)
                                   if userfoundsystem == transferdestin[0]:
                                        senderbalance = int(transferdestin[2])
                                        transferdestin[2] = str(senderbalance - howmuch)
                                   accounts.append(transferdestin)
                         if found:
                              with open("usernames.csv", "w") as file:
                                   for account in accounts:
                                        file.write(",".join(account) + "\n")
                                             

                              if not found:
                                   print("Not found")
                    else:
                         print("This amount of money is not permited")   
                         time.sleep(1)
                         banksystem()  
               except ValueError, UnboundLocalError:
                    print("You have to enter an integer")    
     else:
          print("You have to enter 1")
          banksystem()


def register():
    os.system("cls")
    print("Welcome") 
    name = str(input("Enter the username: ").strip().lower())
    with open("usernames.csv", "r") as file:
        users = file.read()
    if name in users:
        print("This User in not Avalible")

    else:
        print("User Avalible!")
        registerpassword = str(input("Enter the password to your new account: "))
        with open("usernames.csv", "a") as file:
            file.write(name + "," + registerpassword + "," + "1000 \n")
            print("account created, please log in")
            time.sleep(1)

user()
