def deposit():
    while True:
        amount=input("Enter the amount to deposit $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("AMount should be greater than 0")
        else:
            print("Please enter a valid input")

    return amount

deposit()