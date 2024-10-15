import random
MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 100
MIN_BET = 1

MAX_ROWS = 3
MAX_COLS = 3

symbols = {
    'A': 3,
    'B': 6,
    'C': 6,
    'D': 4
}

symbol_values = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 4
}

def get_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

def get_spin(rows, cols, symbols):
    columns = []
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    for _ in range(cols):
        column = []
        all_symbol_cp = all_symbol[:]
        for _ in range(rows):
            value = random.choice(all_symbol_cp)
            column.append(value)
            all_symbol_cp.remove(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def deposit():
    while True:
        amount = input('How much would you like to deposit?: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 1: 
                break
            else:
                print('Enter a number greater than 1')
        else:
            print('Enter a valid number')
    return amount


def number_of_lines():
    while True:
        lines = input('How many lines would you like to bet on (1-3)?: ')
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print('Enter a number greater than 0 but less than or equal to 3')
        else:
            print('Enter a valid number')
    return lines


def get_bet(balance):
    lines = number_of_lines()
    while True:
        bet = input('\nHow much would you like to bet on each line?: $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                total_bet = bet * lines
                if balance < total_bet:
                    print(f'\nYou can not place this bet, your balance is ${balance} and your total bet is ${total_bet}\n')
                else:
                    balance -= total_bet
                    print("\n--------------------------------------------------------------------------------")
                    print(f'You placed a bet of ${bet} on {lines} lines and your total bet is ${total_bet}\n')
                    print(f'Your balance is ${balance}\n')
                    break
        else:
            print('Enter a valid number')
    return bet, total_bet, lines, balance

def play_game(balance):
    play = input('Would you like to play? press (Enter to play or q to quit): ').lower()
    while True:
        if play == 'q':
            break
        else:
            bet, total_bet, lines, balance = get_bet(balance)
            print(f'Bet of ${total_bet} accepted!')
            slot = get_spin(MAX_ROWS, MAX_COLS, symbols)
            print_slot_machine(slot)
            winnings = get_winnings(slot, lines, bet, symbol_values)
            balance += winnings
            print(f"You won ${winnings} and your new balance is ${balance}")
            if balance <= 0:
                print("your balance is 0. you have to deposit more funds to continue")
                balance = deposit()
            else:
                play = input('Would you like to play again? press (Enter to play or q to quit): ').lower()
        print(f"\nYour final balance is ${balance}")



def main():
    balance = deposit()
    play_game(balance)
    

main()


            
        