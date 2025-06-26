#features
#1. Banck account
#2. deposit money
#3. withdraw money
#4. Details panel
#5. update details
#6. Delete accounts
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An exception occured as {err}")


    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k= 3)
        nums = random.choices(string.digits, k = 3)
        spchr = random.choices("!@#4%^&*", k= 1)
        id = alpha + nums + spchr
        random.shuffle(id)
        return "".join(id)
    

    def Createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("tell your age: ")),
            "email": (input("tell your email: ")),
            "pin": int(input("tell your pin: ")),
            "accountNo": Bank.__accountgenerate(),
            "balane": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4: #enhance the validation
            print("Sorry you cannot create your account")
        else:
            print("Account is created successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accountNo = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        # for i in Bank.data:
        #     if(i["accountNo"] == accountNo):
        #         if(pin == i["pin"]):
        #             print(f"""
        #                 Account found successfully
        #                 Welcome {i['name']}
        #             """)
        #             break
        #         else:
        #             print("Incorrect pin entered!")
        #             break
        # else:
        #     print("Bank account not found!")
        userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

        if userdata == []:
            print("sorry no data found")
        
        else:
            amount = int(input("how much you want to depoit "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit above 10000 or below 0")

            else:
                print(userdata)
                userdata[0]['balane'] += amount
                Bank.__update()
                print("Amount deposited successfully ")

    def withdrawmoney(self):
        accountNo = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

        if userdata == []:
            print("sorry no data found")
        
        else:
            amount = int(input("how much you want to withdraw "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can withdraw above 10000 or below 0")

            else:
                print(userdata)
                if(userdata[0]['balane'] < amount):
                    print("insufficeient funds!")
                    return
                userdata[0]['balane'] -= amount
                Bank.__update()
                print("Amount deposited successfully ")

    def showDetails(self):
        accountNo = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

        if userdata == []:
            print("sorry no data found")

        else:
            print("Your Bank Scoount details are as follows: ")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updateDetails(self):
        accountNo = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]
        #uptable field name, email and pin
        if userdata == []:
            print("no such user found")
        
        else:
            print("You cannot change the age, account number, balance")
            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name" : input("please tell new name or press enter: "),
                "email" : input("please tell new email or press enter: "),
                "pin" : input("please tell new pin or press enter: "),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            newdata["age"] = userdata[0]["age"]
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balane"] = userdata[0]["balane"]

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")

    def deleteaccount(self):
        accountNo = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]
        if userdata == []:
            print("no such user found")
        else:
            check = input("press y if you actually want to delete account or press n: ")
            if check == 'n' or check == 'N':
                print("passed!")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully!")
                Bank.__update()
        
    pass





user = Bank()

print("Press 1 for creating an account.")
print("Press 2 for depositing money in bank.")
print("Press 3 for withdrawing money from bank.")
print("Press 4 for details.")
print("Press 5 for updating the details.")
print("Press 6 for deleting an account.")

check = int(input("Tell you response: "))
 
if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.deleteaccount()