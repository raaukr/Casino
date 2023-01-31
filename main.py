MAX_LINES = 3

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


def main():
    deposit()
    lines()

main()