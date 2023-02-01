MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input('What sum do you want to add?\n')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Type number greater 0.\n')
        else:
            print('Please enter the number.\n')
    
    return(amount)

def lines():
    while True:
        lines = input('Choose number 1 - ' + str(MAX_LINES) + '.\n')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print('Type number 1 - ' + str(MAX_LINES) + '.\n')
        else:
            print('Please enter the number.\n')
    
    return(lines)

def bet():
    while True:
        amount = input(f'How many do you want to bet? (Choose the number between {MIN_BET} - {MAX_BET})?\n')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Type the number between {MIN_BET} - {MAX_BET}.\n')
        else:
            print('Please enter the number.\n')
    
    return(amount)   

def main():
    balance = deposit()
    lines = lines()
    bet = bet()
    total_bet = bet * lines
    print(f'Your bet is {total_bet}.')

main()