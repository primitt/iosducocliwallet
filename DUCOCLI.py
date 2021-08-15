import ducoapi
import time
api = ducoapi.api_actions()
print("Welcome to the primitt duco balance viewer, this only has a little"
      " stuff you can do with it, but ill add more later")
un = input("Enter your username: ")
pw = input("Enter your password: ")


api.login(username=un, password=pw)
api.balance()
print("Balance of ", un, ":", api.balance())
while True:
      inp = input(">>> ")

      if inp=="send":
            rc = input("Username to send funds to: ")
            amt = input("Amount to send: ")
            api.transfer(recipient_username=rc, amount=amt, message=hello)
            time.sleep(5)
            print("Sent ",amt,"DUCO to", rc,)
            time.sleep(1)
      elif inp=="bal":
            print("balance of account primitt: ",api.balance())
            time.sleep(1)
      if inp=="help":
            print("Commands: "
                  "help, send, bal")
      if inp=="transactions":
          txam = input("Amount of transactions that you would like to view: ")
          txpm = api.getTransactions(txam)
          print(txpm)
    










##if api.balance = true:
##    print("
##api.balance()
##print(api.balance())





