import ducoapi
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
            api.transfer(recipient_username=rc, amount=amt)
      if inp=="bal" or "balance" or "monai":
            print("balance: ",api.balance())







##if api.balance = true:
##    print("
##api.balance()
##print(api.balance())



