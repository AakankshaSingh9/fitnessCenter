import mysql.connector as sql
from datetime import date

fit = sql.connect(host='localhost', user='root', passwd='rootABC', database='IPProject', port="3307")
if fit.is_connected():
    print('Connected')

def cal_feesperhrs(hrs):
    today = date.today()
    curr_mon = today.month
    if(curr_mon==1 or curr_mon==3 or curr_mon==5 or curr_mon==7 or curr_mon==8 or curr_mon==10 or curr_mon==12):
        fees = hrs * 100 * 31
        return fees
    elif(curr_mon==4 or curr_mon==6 or curr_mon==9 or curr_mon==11):
        fees = hrs * 100 * 30
        return fees
    elif(curr_mon==2):
        fees = hrs * 100 * 28
        return fees
    else:
        print("Month Error")

while(1):
    print("******************************\nChoose from Below\n****************************** \n ")
    print("1. Create a new Account \n2. Signin as a Registered User \n3. Admin Login \n4. Exit")
    ch = int(input("Enter Your Choice here : "))
    if(ch==1):
        print("'''''''''''''''''''''''''''''''''''''''''''")
        print("\n \t\t\tRegistration\t\t\t \n")
        print("'''''''''''''''''''''''''''''''''''''''''''")
        name = input("Enter name (full name) : ")
        email = input("Enter email id         : ")
        pwd = input("Enter password         : ")
        hrs = int(input("Enter hours            : "))
        fees = cal_feesperhrs(hrs)
        print("Calculated Fees            : ",fees)
        print("Pay the fees using GPay : \n UPI ID : powerzonefitness@okaxis \n Phone Number : 78001XXXXX  ")
        c1 = fit.cursor()
        insertrecord = ("insert into users_tb(name,email,pwd,fees) values('" + (name) + "','" + (email) + "','" + (pwd) + "'," + str(fees) + ")")
        c1.execute(insertrecord)
        fit.commit()
        print('Account Created')

    elif(ch==2):
        email = input("\nEnter Emailid          : ")
        passwd = input("Enter Password         : ")

        c1 = fit.cursor()
        c1.execute('select * from users_tb')
        data = c1.fetchall()
        count = c1.rowcount

        for row in data:
            if (email in row) and (passwd in row):
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print('            SUCCESSFULLY LOGIN!!!!!!!!')
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print('Welcome',row[1], 'to Powerzone Fitness Centre')
                print()

                while(True):
                    print("\n***************************************\n")
                    print("Choose from Below Options")
                    print("1. Show Details\n2. Update Details\n3. Exit")
                    print("\n***************************************\n")

                    c1 = fit.cursor()
                    c1.execute('select * from users_tb')
                    data = c1.fetchall()
                    count = c1.rowcount

                    user_ch = int(input("Enter Your Choice here : "))
                    if (user_ch == 1):
                        print("Details                : ")
                        for row_user in data:
                            if (email in row_user):
                                print(row_user)

                    elif (user_ch == 2):
                        name = input("Enter name (full name) : ")
                        email = input("Enter email id         : ")
                        pwd = input("Enter password         : ")
                        hrs = int(input("Enter hours           : "))
                        fees = cal_feesperhrs(hrs)
                        print("Calculated Fees            : ", fees)
                        print("Pay the fees using GPay : \n UPI ID : powerzonefitness@okaxis \n Phone Number : 78001XXXXX  ")
                        c1 = fit.cursor()
                        updaterecord = ("update users_tb set name='" + (name) + "', email='" + (email) + "', pwd='" + (pwd) + "', fees=" + str(fees) + " where id=" + str(row[0]))
                        c1.execute(updaterecord)
                        fit.commit()
                        print('Account Updated')
                    elif(user_ch == 3):
                        print("Exiting...")
                        break
                    else :
                        print("Invalid Choice")
    elif(ch==3):
        username = input("Enter username : ")
        password = input("Enter Password : ")

        if(username=='Admin' and password=='Admin@123'):
            while (True):
                print("\n***************************************\n")
                print("Choose from Below Options")
                print("1. Show Customer Details \n2. Update Details \n3. Exit")
                print("\n***************************************\n")

                c1 = fit.cursor()
                c1.execute('select * from users_tb')
                data = c1.fetchall()
                count = c1.rowcount

                admin_ch = int(input("Enter Your Choice here : "))
                if (admin_ch == 1):
                    print(data)
                elif(admin_ch == 2):
                    id = input("Enter id               : ")
                    name = input("Enter name (full name) : ")
                    email = input("Enter email id         : ")
                    pwd = input("Enter password         : ")
                    hrs = int(input("Enter hours            : "))
                    fees = cal_feesperhrs(hrs)
                    print("Calculated Fees        : ", fees)
                    c1 = fit.cursor()
                    updaterecord = (
                            "update users_tb set name='" + (name) + "', email='" + (email) + "', pwd='" + (pwd) + "', fees=" + str(fees) + " where id=" + str(id))
                    c1.execute(updaterecord)
                    fit.commit()
                    print('Account Updated')

                elif(admin_ch == 3):
                    print("Exiting .....")
                    break

                else:
                    print("Invalid Choice !!!")
                    break

        else:
            print("Incorrect Credentials ! Try Again !!")

    elif(ch==4):
        print("Exiting...")
        print(
            "****************************************\n Thank You ! Visit Again !!! \n****************************************")
        break
    else:
        print("Invalid Choice")
        break







