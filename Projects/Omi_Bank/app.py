import datetime
import sqlite3
import secrets
from os import system, name
import requests
import json
import os


# define our clear function 
def clear(): 

        # for windows 
        if name == 'nt': 
                _ = system('cls')

def sendSMS(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
        
    params = {
        # 'authorization' : os.environ.get('FSTSMS_SENDER'),
        'authorization' : 'fihYRsgIu2W7KnVBJ0qPpMNaevlZUOFHSXz9k6mDj5wocC8dTQDIqitKbQS5RoGA8zyewuXhZJ6fprcW',
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : number
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

def header():
    clear()

    time = datetime.datetime.now()
    print( ('\n' * 2) + ('\t' * 3) + str(time.strftime('%A')) + ', ' + str(time.strftime('%Y')) + ('\t' * 7) + 'Time : ' + str(time.strftime('%X')))

    print(('\n' * 2) + ('\t' * 6) + ('*' * 6) + ' OMI Bank for Everyone! ' + ('*' * 6) + ('\n' * 1))
    print(('\t' * 4) + ('--' * 34) + ('\n' * 2))

def ShowDashboard():

    header()
    
    print(('\t' * 3) + '1: Login Your Account!' + (("\t" * 6) + '4: Reset Password') + '\n' + ('\t' * 3) + '2: Create Your Account' + (("\t" * 6) + '5: Info') + '\n' + ('\t' * 3) + '3: Check Balance' + (('\t' * 6) + '6: Exit') + ('\n' * 2))
    
    userChoice = int(input(('\t' * 3) + "Type Your Choice : "))

    # Function to Perform Choices
    BrainOperations(userChoice)

def BrainOperations(choice):
    
    if choice == 1:
        
        clear()
        userAuthenticate('login')

    elif choice == 2:
        
        clear()
        CreateBankAccount()

    elif choice == 3:
        
        clear()
        userAuthenticate('checkBalance')

    elif choice == 4:

        # ShowBankDetails()
        userAuthenticate('resetPassword')
        
    elif choice == 5:
        dropTable()

    elif choice == 6:
        exit()
        
    else:
        header()
        print(('\t' * 3) + "Invalid Input, Type Correct Number" + ('\n' * 2) )
        print(('\t' * 3) + '1: Go to Dashboard' + ('\t' * 6) + '2: Exit' + ('\n' * 2))

        try:
            optional = int(input(('\t' * 3) + 'Type Your Choice : '))
        except ValueError:
            print(('\t' * 3) + "Invalid Input, Do not Use Characters or Special Symbols")
        else:
            if optional == 1:
                ShowDashboard()
            elif optional == 2:
                exit()
            else:
                print("Invalid Input!, Type Correct details")

def checkBalance(accountNo):
    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (accountNo,))
    USER = curr.fetchone()

    header()

    print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
    print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   
    print(('\n' * 2) + ('\t' * 3) + '1: Go to DashBoard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

    try:
        choice = int(input(('\t' * 3) + 'Type Your Choice : '))
    except:
        print(('\t' * 3) + 'Provide Valid Details!!!')

    if choice == 1:
        ShowDashboard()
    elif choice == 2:
        exit()
    else:
        errorSolving(accountNo)

def resetPassword(AccountNo):
    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (AccountNo,))
    USER = curr.fetchone()

    header()

    print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
    print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   
    # print(('\n' * 2) + ('\t' * 3) + '1: Go to DashBoard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

    print(('\t' * 3) + "Your Old Password is Sent you as An SMS!" + ('\n' * 2))
    print(('\t' * 3) + 'Now You Are Changing Your Password by which : \n' + ('\t' * 3) + f'- {USER[2]} You are Going to Login with Your New Password!\n' + ('\t' * 3) + '- New Password SMS will be Sent After Setting up Your Password.\n' + ('\t' * 3) + "Don't Share it With Anybody, Your Account Number and Password!" + ('\n' * 2))

    oldPassword = input(('\t' * 3) + 'Type Your Old Password')
    if oldPassword != USER[3]:
        invalidCredentials(AccountNo)
    else:

        clear()
        header()
        print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   

        newPassword = input(('\t' * 3) + 'Choose Your New Password : ')

        curr.execute("UPDATE BankCredentials SET password = (?)", (newPassword,))
        conn.commit()

        print(('\t' * 3) + 'Your Password has Been Changed Successfully!!!\n' + ('\t' * 3) + 'SMS is Sent, On Resgistered Mobile Number!' + ('\n' * 2))

        print(('\n' * 2) + ('\t' * 3) + '1: Login Account' + ('\t' * 6) + '2: Go to DashBoard\n' + ('\t' * 3) + '3: Exit' + ('\n' * 2))

        try:
            YourChoice = int(input(('\t' * 3) + 'Type Your Choice : '))
        except ValueError:
            print("Type Numbers, String or Any other Special Symbols are Not Allowed")

        if YourChoice == 1:
            userAuthenticate('login')
        elif YourChoice == 2:
            ShowDashboard()
        elif YourChoice == 3:
            exit()
        else:
            errorSolving(AccountNo)

        conn.close()
    
def CreateBankAccount():
    
    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute(""" CREATE TABLE IF NOT EXISTS BankCredentials (
        AccNo integer,
        fullName text,
        AccHolderName text,
        password text,
        phone integer,
        country text,
        state text,
        date_of_birth text,
        secretKey text,
        balance integer
    ) """)

    header()

    print(('\t' * 3) + 'CREATE BANK ACCOUNT' + ('\n'*2))
    
    fullName = input(('\t' * 3) + "Type Your Full Name : ").strip()
    Account_Holder_Name  = input('\n' + ('\t' * 3) + "Choose Username : ").strip()
    password = input(('\t' * 3) + 'Choose Password : ').strip()

    try:
        phoneNum = int(input('\n' + ('\t' * 3) + "Type Your Mobile Number : ").strip())
    except ValueError:
        print('Invalid Input, Type Correct Details!!!')

    nationality  = input('\n' + ('\t' * 3) + "Type Your Country : ").strip()
    state  = input('\n' + ('\t' * 3) + "Type your State : ").strip()

    try:
        print('\n' + ('\t' * 3) + 'Date of Birth\n')
        year = int(input(('\t' * 4) + 'Year : ').strip())
        month = int(input('\n' + ('\t' * 4) + 'Month : ').strip())
        day = int(input('\n' + ('\t' * 4) + 'Day : ').strip())
    except ValueError:
        print('Invalid Input, Type Correct Details!!!')

    birth = str(datetime.datetime(year, month, day))
    AccNo = secrets.randbits(16)
    secretKey = secrets.token_hex(16)
    balance = 500    
    
    curr.execute("INSERT INTO BankCredentials VALUES (:accountNO, :fullname, :accHolder, :pass, :phoneNum, :country, :state, :birthdate, :secretNum, :bal)",{
        'accountNO':AccNo,
        'fullname': fullName,
        'accHolder' : Account_Holder_Name,
        'pass' : password,
        'phoneNum' : phoneNum,
        'country' : nationality,
        'state' : state,
        'birthdate' : birth,
        'secretNum' : secretKey,
        'bal' : balance
    })
    conn.commit()

    message = ('\n' * 2) + ('\t') + f"{fullName} - Your Saving Account is Created Successfully:\n" + ('\t') + f'Your Account Number is {AccNo}\n' + ('\t') + f'Your Account Holder Name - {Account_Holder_Name}\n' + ('\t') + f"DON'T SHARE YOUR ACCOUNT NUMBER AND PASSWORD TO ANYONE!!\n" + ('\t' * 2) + f"Your Full Name - {fullName}\n"

    sendSMS(phoneNum, message)

    curr.execute("SELECT AccHolderName,balance,phone FROM BankCredentials WHERE AccNo = (?)", (AccNo,))
    confirmUser = curr.fetchone()

    clear()
    header()
    print(('\t' * 3) + f"{confirmUser[0]} Account Has Been Created Successfully. \n" + ('\t' * 3) + f"SMS Regarded :Account-no and :Other Credentials has been Sent.\n" + ('\t' * 3) +  f"SMS is Sent on this Registered Number - {confirmUser[2]} ")

    print(('\n' * 2) + ('\t' * 3) + '1: Login Account' + ('\t' * 6) + '2: Go to DashBoard\n' + ('\t' * 3) + '3: Exit' + ('\n' * 2))

    try:
        YourChoice = int(input(('\t' * 3) + 'Type Your Choice : '))
    except ValueError:
        print("Type Numbers, String or Any other Special Symbols are Not Allowed")

    if YourChoice == 1:
        userAuthenticate('login')
    elif YourChoice == 2:
        ShowDashboard()
    elif YourChoice == 3:
        exit()
    else:
        errorSolving(AccNo)


def ShowBankDetails():
    
    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM BankCredentials")
    data = curr.fetchall()

    for item in data:
        print(item)

    temp = input("Ok")

def userAuthenticate(operation):
    header()

    AccountNo = int(input(('\t' * 3) + 'Type Your ACCOUNT Number: ').strip())
    password = input(('\t' * 3) + 'Type Your PASSWORD : ').strip()

    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT AccNo, password  FROM BankCredentials WHERE AccNo = (?)", (AccountNo,))
    userAuth = curr.fetchone()

    if operation == 'login':
        if AccountNo == userAuth[0] and userAuth[1] == password:
            loginUserAccount(userAuth[0])
        else:
            invalidCredentials(AccountNo)
    elif operation == 'resetPassword':
        if AccountNo == userAuth[0] and userAuth[1] == password:
            resetPassword(AccountNo)
        else:
            invalidCredentials(AccountNo)
    elif operation == 'checkBalance':
        if AccountNo == userAuth[0] and userAuth == password:
            checkBalance(AccountNo)
        else:
            invalidCredentials(AccountNo)
    else:
        errorSolving()

def invalidCredentials(AccountNo):
    header()
    print(('\t' * 3) + "Invalid Credentials!!!" + ('\n' * 2))
    print(('\t' * 3) + '1: Retry' + ('\t' * 6) + '2: Go to Dashboard' + ('\n' * 2))

    try:
        optional = int(input(('\t' * 3) + 'Type Your Choice : '))
    except ValueError:
        print(('\t' * 3) + "Invalid Input, Do not Use Characters or Special Symbols")
    else:
        if optional == 1:
            userAuthenticate('login')
        elif optional == 2:
            ShowDashboard()
        else:
            errorSolving(AccountNo)

def loginUserAccount(AccountNum):
    header()

    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (AccountNum,))
    userDetails = curr.fetchone()

    print(('\t' * 7) + f"Welcome {userDetails[2]}" + ('\n' * 2))
    print(('\t' * 3) + '1: Check Balance' + ('\t' * 6) + '2: Add Money\n' + ('\t' * 3) + '3: WithDraw Cash' + ('\t' * 6) + '4: Edit Account Details\n' + ('\t' * 3) + '5: Exit' + ('\n' * 2))

    try:
        choice = int(input(('\t' * 3) + 'Type Your Choice : '))
    except:
        print(('\t' * 3) + 'String not Allowed')

    data = handleUserRequest(choice, AccountNum, userDetails)

    if data[1] == 1:

        oldMoney = userDetails[9]
        newMoney = oldMoney + data[0]
        curr.execute("UPDATE BankCredentials SET balance = (?) WHERE AccNo = (?)", (newMoney, AccountNum,))
        conn.commit()

        header()
        print(('\t' * 7) + f"Welcome {userDetails[2]}" + ('\n' * 2))
        curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (AccountNum,))
        showData = curr.fetchone()

        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(showData[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(showData[4])}' + (('\t' * 6) + str(showData[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {showData[1]}')   
        print(('\n' * 2) + ('\t' * 3) + '1: Go to Dashboard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

        try:
            choice = int(input(('\t' * 3) + 'Type Your Choice : '))
        except:
            print(('\t' * 3) + 'Provide Valid Details!!!')    

        if choice == 1:
            ShowDashboard()
        elif choice == 2:
            exit()
        else:
            errorSolving(AccountNum)
    
        conn.close()

    elif data[1] == 2:

        curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (AccountNum,))
        showData = curr.fetchone()

        oldAmt = showData[9]
        newAmt = oldAmt - data[0]

        if newAmt < 500:
            header()
            print(('\t' * 7) + f"Welcome {userDetails[2]}" + ('\n' * 2))
            print(('\t' * 3) + f"Rs{data[0]} Can't Withdraw, Because Rs500 Should be maintain in your Bank Account!!!\n" + ('\t' * 3) + f'Your Withdrawal Request of Rs{data[0]} has been Cancelled.')

            print(('\t' * 3) + f'ACCOUNT NUMBER - {str(showData[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(showData[4])}' + (('\t' * 6) + str(showData[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {showData[1]}\n' + ('\t' * 3) + f'ACCOUNT HOLDER NAME : {showData[2]}\n' + ('\t' * 3) + f'BIRTHDATE : {showData[7]}')   
            print(('\n' * 2) + ('\t' * 3) + '1: Go to Dashboard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

            try:
                choice = int(input(('\t' * 3) + 'Type Your Choice : '))
            except:
                print(('\t' * 3) + 'Provide Valid Details!!!')    

            if choice == 1:
                ShowDashboard()
            elif choice == 2:
                exit()
            else:
                errorSolving(AccountNum)

        else:
            header()
            updateQuery([newAmt, 'N', 'balance'], AccountNum)

    elif data[1] == 'f':
        header()
        updateQuery(data, AccountNum)
    
    elif data[1] == 'u':
        header()
        updateQuery(data, AccountNum)
    
    elif data[1] == 'b':
        header()
        updateQuery(data, AccountNum)

    elif data[1] == 'p':
        header()
        updateQuery(data, AccountNum)

    elif data[1] == 's':
        header()
        updateQuery(data, AccountNum)
    
    elif data[1] == 'c':
        header()
        updateQuery(data, AccountNum)
    
    else:
        print("Invalid Input")
        
def updateQuery(data, AccountNum):
    header()

    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute(f"UPDATE BankCredentials SET {data[2]} = (?) WHERE AccNo = (?)", (data[0], AccountNum))
    conn.commit()

    curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)", (AccountNum,))
    updated = curr.fetchone()

    print(('\t' * 7) + f"Welcome {updated[2]}" + ('\n' * 2))
    print(('\t' * 3) + f'ACCOUNT NUMBER - {str(updated[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(updated[4])}' + (('\t' * 6) + str(updated[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {updated[1]}\n' + ('\t' * 3) + f'ACCOUNT HOLDER NAME : {updated[2]}\n' + ('\t' * 3) + f'BIRTHDATE : {updated[7]}\n' + ('\t' * 3) + f'STATE : {updated[6]}\n' + ('\t' * 3) + f'COUNTRY : {updated[5]}')   
    print(('\n' * 2) + ('\t' * 3) + '1: Go to Dashboard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

    try:
       choice = int(input(('\t' * 3) + 'Type Your Choice : '))
    except:
        print(('\t' * 3) + 'Provide Valid Details!!!')
        
    if choice == 1:
        ShowDashboard()
    elif choice == 2:
        exit()
    else:
        errorSolving(AccountNum)

    conn.close()

def handleUserRequest(humanChoice, accountNum, USER):
    
    header()

    if humanChoice == 1:
        print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   
        print(('\n' * 2) + ('\t' * 3) + '1: Go to DashBoard' + (('\t' * 6) + '2: Exit') + ('\n' * 2))

        try:
            choice = int(input(('\t' * 3) + 'Type Your Choice : '))
        except:
            print(('\t' * 3) + 'Provide Valid Details!!!')

        if choice == 1:
            ShowDashboard()
        elif choice == 2:
            exit()
        else:
            errorSolving(accountNum)

    elif humanChoice == 2:
        print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   

        addAmt = int(input(('\n' * 2) + ('\t' * 3) + 'Enter Amount : '))
        dataList = [addAmt, 1]

        return dataList

    elif humanChoice == 3:
        
        print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}')   

        withAmt = int(input(('\n' * 2) + ('\t' * 3) + 'Enter Amount : '))
        dataList = [withAmt, 2]        

        return dataList

    elif humanChoice == 4:
        print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
        print(('\t' * 3) + f'ACCOUNT NUMBER - {str(USER[0])}' + (('\t' * 5) + 'CASH BALANCE :\n') + ('\t' * 3) + f'PHONE NUMBER - {str(USER[4])}' + (('\t' * 6) + str(USER[9])) + '\n' + ('\t' * 3) + f'FULL NAME - {USER[1]}\n' + ('\t' * 3) + f'DATE OF BIRTH - {USER[7]}\n' + ('\t' * 3) + f'STATE - {USER[6]}\n' + ('\t' * 3) + f'COUNTRY - {USER[5]}\n' + ('\t' * 3) + f'ACCOUNT HOLDER NAME : {USER[2]}\n' + ('\t' * 3) + f'BIRTHDATE : {USER[7]}')   

        wantToChange = str(input(('\n' * 2) + ('\t' * 3) + 'Want to Change any Bank Details? Type "yes" or "no" : '))
        wantChanges = wantToChange.lower()

        if wantChanges == 'yes':
            print(('\n' * 2) + ('\t' * 3) + '1: FULL NAME' + (('\t' * 6) + '2: ACCOUNT HOLDER NAME\n' + ('\t' * 3) + '3: BIRTH' + ('\t' * 6) + '4: PHONE\n' + ('\t' *  3) + '5: STATE' + ('\t' * 6) + '6: COUNTRY' + ('\n' * 2)))
            changes = int(input(('\t' * 3) + 'Type Your Choice to Make Changes in that Column : '))

            if changes == 1:

                FULLNAME = input(('\n' * 2) + ('\t' * 3) + 'Type Your Full Name : ')
                return [FULLNAME, 'f', 'fullName']

            elif changes == 2:

                USERNAME = input(('\n' * 2) + ('\t' * 3) + 'Choose Your Account Holder Name : ')
                return [USERNAME, 'u', 'AccHolderName']

            elif changes == 3:

                print('\n' + ('\t' * 3) + 'Date of Birth\n')
                year = int(input(('\t' * 4) + 'Year : '))
                month = int(input('\n' + ('\t' * 4) + 'Month : '))
                day = int(input('\n' + ('\t' * 4) + 'Day : '))

                BIRTH = str(datetime.datetime(year, month, day))

                return [BIRTH, 'b', 'date_of_birth']

            elif changes == 4:
                
                PHONE = input(('\n' * 2) + ('\t' * 3) + 'Change your Phone Number : ')
                return [PHONE, 'p', 'phone']

            elif changes == 5:

                STATE = input(('\n' * 2) + ('\t' * 3) + 'Type Your State : ')
                return [STATE, 's', 'state']

            elif changes == 6:

                COUNTRY = input(('\n' * 2) + ('\t' * 3) + 'Type Your Country : ')
                return [COUNTRY, 'c', 'country']
                
            else:
                errorSolving()

        elif wantChanges == 'no':
            loginUserAccount(accountNum)
        
        else:
            errorSolving(accountNum)

    elif humanChoice == 5:
        exit()
    
    elif humanChoice > 5:
        errorSolving(accountNum)

    else:
        errorSolving(accountNum)

def errorSolving(accountNum):

    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("SELECT * FROM BankCredentials WHERE AccNo = (?)",(accountNum,))
    USER = curr.fetchone()

    header()
    print(('\t' * 7) + f"Welcome {USER[2]}" + ('\n' * 2))
    print(('\t' * 3) + "Invalid Input, Type Correct Number" + ('\n' * 2) )
    print(('\t' * 3) + '1: Retry' + ('\t' * 6) + '2: Go to Dashboard' + ('\n' * 2))

    try:
        optional = int(input(('\t' * 3) + 'Type Your Choice : '))
    except ValueError:
        print(('\t' * 3) + "Invalid Input, Do not Use Characters or Special Symbols")
    else:
        if optional == 1:
            loginUserAccount(accountNum)
        elif optional == 2:
            ShowDashboard()
        else:
            print("Invalid Input!, Type Correct details")

def dropTable():
    conn = sqlite3.connect('OmiBank.db')
    curr = conn.cursor()

    curr.execute("DROP TABLE BankCredentials")
    curr.close()

# ----------------------------------------------------------- Main Program ------------------------------------------------------------

if __name__ == '__main__':
    while True:
        ShowDashboard()