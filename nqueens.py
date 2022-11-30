import random

def randomQueens(board, n):
    randList = random.sample(range(1,n*n),n)
 
    return randList
    
def minConflicts(csp, max_steps, current):
    
    current = None
    for i in range(max_steps):
        
        return None

def __main__():    
    choice = input("Choose value of n:\n1.10\n2.100\n3.1000\n4.10000\n5.100000\n6.10000000\n")
    n = 10;
    match choice:
        case "1":
            n = 10
        case "2":
            n = n*n
        case "3":
            n = n*n*n
        case "4":
            n = n*n*n*n
        case "5":
            n = n*n*n*n*n
        case "6":
            n = n*n*n*n*n*n
        case _:
            print("Invalid value")
    
    board = [[0 for x in range(n)] for y in range(n)]
 
    list = randomQueens(0,n)
    positions = []
    for i in range(1, len(list)):
        board[list[i] // n][list[i]%n] = 1 
        
    

    print(list)
    for i in range(n):
        print(board[i],"\n")
    
    
    
    #print(list)
class Queen:
    
    def __init__(self, board):
        self.variables = list()
        self.constraints = list()
        return None

__main__()