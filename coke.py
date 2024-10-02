ammount_due = 50
coins_accepted = [5,10,25]

while ammount_due > 0:
    print("Amount Due:", ammount_due)

    coin = int(input("Insert coin: "))

    if coin in coins_accepted:
        ammount_due -= coin

print("Change Owed:", ammount_due * -1)
