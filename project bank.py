import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
print(mycon)
mycursor=mycon.cursor()
# mycursor.execute("create database Bank_Management")
print("Bank_Management")
account_number= int(input("enter you account number:"))
balance = int(input("enter your account balance:"))
name=input("enter your name:")
def main ():
        admin=input("Enter choose option(deposit/withdraw/delete account):").lower()
        if admin=="deposit":
            deposit_amount=int(input("enter your amount:"))
            total_amount=balance+deposit_amount
            print(total_amount)
            print("done")
            print(main())
        elif admin =="withdraw":
            withdraw_amount=int(input("enter amount:"))
            final_amount=balance-withdraw_amount
            print(final_amount)
        elif admin=="delete account":
            print(account_number)
            print("delete account done")

user=input("Enter a option(create account or existing account):").lower()
if user =="existing account":
    print("welcome")
    main() 
elif user=="create account":
    import random
c = set()

def generated_account_number():
    if len(c) >= 9000:
        raise Exception("All 4-digit numbers are used!")
    
    while True:
        number = random.randint(1000, 9999)
        if number not in c:
            c.add(number)
            return number
for _ in range(1):
    print("Client account number :", generated_account_number())
    main() 

    






