MAX_LINES=3
MAX_BET=100
MIN_BET=1

def deposit():
    while True:
        amount=input("Enter the amount to deposit $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Please enter a valid input")

    return amount


def get_number_of_lines():
        while True:
            lines=input("Enter the number of lines you want to bet on (1- "+str(MAX_LINES) +")? ")
            if lines.isdigit():
                lines=int(lines)
                if 1<=lines<=MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines")
            else:
                print("Please enter a valid input")
                
        return lines
    
def get_bet():
    while True:
        amount=input("How much do you want to bet on each line $ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid input")

    return amount



def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet

        if total_bet > balance:
            print(f"You do not have enough balance to bet. Your current balance is {balance}")
        else:
            break
            
    print(f"You have betted an amount of {bet} on {lines} lines. Your total bet is {total_bet}")
    

main()