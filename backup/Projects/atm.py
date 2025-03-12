import mysql.connector
from rich import print

def formatter(cursor,data):
    result = []
    for row in data:
        row_dict = {}
        for idx, column in enumerate (cursor.description):
            row_dict[column[0]]=row[idx]
        result.append(row_dict)
    return result

def create_Connection():
    try:
        db_connection=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="atm")
        #print("Successfully connected")
        return db_connection
    except Exception as err:
        print (str(err))

connection  = create_Connection()   
cursor = connection.cursor()
# cuid=511
query = "select * from customer_table"
cursor.execute(query)
data = cursor.fetchall()
formatted_data = formatter(cursor, data)
#print(formatted_data)

while True:
    print("\n_____________________________________")
    print("AAA Bank .")
    print("Welcomes You")
    print("\n_____________________________________")

    print("Select your qOptions:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Balance Enquiry")
    print("4. Withdrawal")
    print("5. Exit")
    user_input = int(input("Enter Your Option: "))
    if user_input == 1:
        customer_Name = input("Enter Your customer Name: ")
        dob = input("Enter Your DOB: ")
        contact_number=int(input("Enter Contact_number"))

        customer_address = input("Enter Address ")
        account_number=int(input("Enter Acc number"))
        account_type = input("Account type(Savings/Current): ")
        initial_balance = int(input("Enter Initial Balance: "))
        
        cursor.execute("insert into customer_table values (NULL, %s, %s, %s, %s, %s,%s, %s)", 
                       (customer_Name, dob,contact_number , customer_address, account_number, account_type, initial_balance))
        connection.commit()
        
        #formatted_data = formatter(cursor, data)

        # print(query)
        print("Account created successfully!")
        print("\n_____________________________________")
        print("AAA Bank .")
        print("Welcomes You")
        print("\n_____________________________________")
        query = "select * from customer_table"
        cursor.execute(query)
        data = cursor.fetchall()
        formatted_data = formatter(cursor, data)

        print(formatted_data)
        
        # Deposit

    elif user_input == 2:
        account_number = int(input("Enter Your Account Number: "))
        # query="select * from customer_table where account_number = %s" % (account_number)
        query = f"select * from customer_table where account_number = {account_number}"
        cursor.execute(query)
        data = cursor.fetchall()
        #print(type(data)
        formatted_data = formatter(cursor, data)
        #print(type(formatted_data))
        #print(len(formatted_data))
        if len(formatted_data) > 0:
            print("Account Number Matched.so go for Deposite")
            nofoneHundred=int(input("Enter No.of One Hundred "))
            nooftwoHundred=int(input("Enter No.of Two Hundred "))
            nooffiveHundred = int(input("Enter No.of Five Hundred"))
            
            depositeAmount= (nofoneHundred*100) + (nooftwoHundred * 200) + (nooffiveHundred*500)
            confirm_amount = int(input(f"""
                *****************************      
                100 * {nofoneHundred} = {nofoneHundred * 100}    
                200 * {nooftwoHundred} = {nooftwoHundred * 200}  
                500 * {nooffiveHundred} = {nooffiveHundred * 500} 
                Total Amount = {depositeAmount}  

                If the denomation is correct Please Enter 1
                Else Enter 2
                """))
            #print(formatted_data[0].get('BALANCE'))
            if(confirm_amount == 1):
                updatedBalance=formatted_data[0].get("BALANCE") + depositeAmount
                #print(getBalance)
                query=f"update customer_table set BALANCE = {updatedBalance} where ACCOUNT_NUMBER = {account_number}"
                cursor.execute(query)
                connection.commit()
                print("Amount depsitted successfully!")
                print("\n_____________________________________")
                print("AAA Bank .")
                print("Welcomes You")
                print("\n_____________________________________")

                
                print("\n==================================================")
                print("CUSTOMER_NAME",formatted_data[0].get("CUSTOMER_NAME"))
                print("ACCOUNT_NUMBER",formatted_data[0].get("ACCOUNT_NUMBER"))
                print("Deposited ur account successfully",updatedBalance)
                print("\n==================================================")
            else:
                print("Please collect ur cash")
        else:
            print("Your account Number not matched with database")    
        

    elif user_input == 3:
        account_number = int(input("Enter your Account Number : "))
        query = f"select ACCOUNT_NUMBER,ACCOUNT_TYPE,BALANCE from customer_table where Account_number = {account_number}"
        cursor.execute(query)
        data = cursor.fetchall()
        #print(data)
        formatted_data = formatter(cursor, data)
        if len(formatted_data) > 0:
            print("Balance Enquiry")
            print("\n================================")
            print("Your Account_Number : ",formatted_data[0].get("ACCOUNT_NUMBER"))
            print("Your Account_Type : ",formatted_data[0].get("ACCOUNT_TYPE"))
            print("Your Account_Balance : ",formatted_data[0].get("BALANCE"))
        
        else:
            print("Your Account_Number not matched with Database")    

    elif user_input == 4:
        print("Withdrawl")
        print("\n=======================")
        account_number = int(input("Enter the Account Number"))
        query = f"select ACCOUNT_NUMBER,ACCOUNT_TYPE,BALANCE from customer_table where Account_number = {account_number}"
        cursor.execute(query)
        data = cursor.fetchall()
        #print(data)
        formatted_data = formatter(cursor, data)
        if  len(formatted_data) > 0 :
            withdrawlAmount = int(input("Enter the Withdraw Amount"))
            if formatted_data[0].get("BALANCE") >= withdrawlAmount :
                updatedBalance=formatted_data[0].get("BALANCE") - withdrawlAmount
                query=f"update customer_table set BALANCE = {updatedBalance} where ACCOUNT_NUMBER = {account_number}"
                cursor.execute(query)
                connection.commit()
                print("Your Account Number matched for Withdraw")
                print("\n================================")
                print("Your Account_Number : ",formatted_data[0].get("ACCOUNT_NUMBER"))
                print("Your Account_Type : ",formatted_data[0].get("ACCOUNT_TYPE"))
                print("Your Account_Balance : ",formatted_data[0].get("BALANCE"))
            else:
                print("Insufficient Balance")    
        else:
            
            print("Your Account Number not matched with Database")
            
    elif user_input == 5:
        
        print("\n================================")
        print("Your Transaction Successfully completed .Visit again.")    
        print("\n================================")
        