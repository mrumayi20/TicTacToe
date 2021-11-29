

board = [
    ["-" , "-" , "-"],
    ["-" , "-" , "-"],
    ["-" , "-" , "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}  " , end="")
        print(end="\n")

print("Welcome To TicTacToe, All the best")
print("MAY THE BEST PLAYER WINS")
print_board(board)

def Quit(user_iput):
    if user_input == "q" or user_input == "Q" : 
        print("ThankYou For Playing, Have a good day!")
        return True
    else: return False

def isBound(user_input):
    if user_input >= 1 and user_input <= 9:
        return True
    else:
        print("Input is not in range 1 to 9")
        return False


def isNumValid(user_input):
    if user_input.isnumeric() : return True
    print("Input is not valid. Please enter valid input")
    return False

def isNum(user_input):
    #to check if input is number
    if not isNumValid(user_input) : return False
    user_input = int(user_input)
    if not isBound(user_input) : return False
    return True


while True:
    user_input = input("Please enter from digit 1 to 9 or enter \"q\" to Quit")
    if Quit(user_input): break
    if not isNum(user_input) : 
        print("Please try again")
        continue 


