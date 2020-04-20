from getpass import getpass
import time
import json

f = open('bank.db','w')
bank = { 
        'user' : [ 'ram', 'sam','vijay' ],
        'acc' : [ 1001, 1002, 1003 ],
        'password' : [ 'grras@123', 'something', 'redhat'],
        'balance' : [ 10000.23, 20000.45, 124322.234]
        }
json.dump(bank,f)

f.close()
print("File sucessfully created")

f = open('bank.db')
data = json.load(f)
f.close()

for key,value in data.items() :
    print("{} = {}".format(key,value))
    
f = open('bank.db')
bank = json.load(f)
f.close()
admin = 'root'
admin_password = 'redhat@123'

while True :
    print("\n\n")
    print("*"*50)
    print(time.ctime())
    f = open('log.txt','a')
    s = "Application Run by user at {} \n".format(time.ctime())
    f.write(s)
    f.close()
    print("Welcome to Python Bank")
    print("*"*50)
    print("\n\n1. Login \n2. Signup \n3. Admin \n4. Exit")
    ch = int(input("Your Choice : "))
    
    if ch == 1 :
        print("\n\n")
        uacc = int(input("Acc Number : "))
        if uacc in bank['acc'] :
            upass = getpass("Password : ")
            index = bank['acc'].index(uacc)
            if upass == bank['password'][index]:
                s = "User with acc no {} logged into account at {}\n".format(uacc,time.ctime())
                f = open('log.txt','a')
                f.write(s)
                f.close()
                while True :
                    print("\n\n1. Debit\n2. Credit\n3. Check Balance\n4. Change Password \n5. Logout")
                    ch = int(input("Choice : "))
                    if ch == 1 :
                        bal = float(input("\n\nEnter Amount to Debit : "))
                        if bal > bank['balance'][index] :
                            print("\n\ninsufficient Balance to Withdraw")
                            print("You have  : {} rupeess in your account".format(bank['balance'][index]))
                            print()
                        else :
                            print("\n\nAmount Sucessfully Withdrawn")
                            bank['balance'][index] -= bal
                            f = open('log.txt','a')
                            s = "{} User with acc no {} withdrawn {} \n".format(time.ctime(),uacc,bal)
                            f.close()
                            f = open('bank.db','w')
                            json.dump(bank,f)
                            f.close()
                            print("\n\nYou have left {} rupess in your account".format(bank['balance'][index]))
                        #your code goes here for debit
                    elif ch == 2 :
                        bal = float(input("\n\nEnter Bal to Deposite : "))
                        bank['balance'][index] += bal
                        f = open('bank.db','w')
                        json.dump(bank,f)
                        f.close()
                        print("\nYour Account Sucessfully Updated")
                        print("You have {} rupees in your account".format(bank['balance'][index]))
                        print()
                        #your code goes here for credit
                    elif ch == 3 :
                        #your code goes here for Check Balance
                        print("\n\nName : ",bank['user'][index])
                        print("Account Number : ",bank['acc'][index])
                        print("Balance : ",bank['balance'][index])
                        print()
                    elif ch == 4 : 
                        upass = getpass("New Password : ")
                        upass1 = getpass("Verify Password : ")
                        if upass == upass1 : 
                            bank['password'][index] = upass
                            f = open('bank.db','w')
                            json.dump(bank,f)
                            f.close()
                            print("Password Sucessfully Changed")
                            break
                        else :
                            print("\nPassword Does not Match Try Again")
                    elif ch == 5 :
                        print("\nLogging you out.....\n")
                        break
                    else :
                        print("\n\nInvalid Choice ")
                        print("Try Again")
            else :
                f = open('log.txt','a')
                s = "Invalid Access of acc {} by user at {}\n".format(uacc,time.ctime)
                f.write(s)
                f.close()
                print("\n\nInvalid Password\n\nTry Again")
            
        else :
            f = open('log.txt','a')
            s = "Wrong Try by user {}\n".format(time.ctime())
            f.write(s)
            f.close()
            print("\n\nNo such Account Exists \nYou should signup\n\n")
    elif ch == 2 :
        acc = bank['acc'][-1] + 1
        name = input("Username : ")
        bal = float(input("Initial Blance : "))
        password = getpass("Set Password : ")
        bank['user'].append(name)
        bank['acc'].append(acc)
        bank['password'].append(password)
        bank['balance'].append(bal)
        f = open('bank.db','w')
        json.dump(bank,f)
        f.close()
        print("\nAccount Sucessfully Created")
        print("Note down your account num :  {}".format(acc))
        print("Now you can login\n")
    elif ch == 3 :
        username = input("\nEnter name : ").strip().lower()
        password = getpass()
        if username == admin : 
            if password == admin_password :
                print()
                for key,value in bank.items():
                    print("{}={}".format(key,value))
                print()
            else :
                print("\nInvalid password \nTry Again")
        else :
            print("\nThis user is not an admin.")
    elif ch == 4 :
        ch = input("\n\nDo really want to exit ? (y/n) : ").strip().lower()
        if ch == 'y' or ch == 'yes' :      
            print("\nThanks for useing our services ")
            break
    else :
        print("\nInvalidChoice\nTry again")
