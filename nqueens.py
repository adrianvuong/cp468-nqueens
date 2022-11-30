import random

def randomQueens(board, n):
    randList = random.sample(range(1,n),n)
 
    
    return randList
    
def minConflicts(csp, max_steps, current):

    return None
    
def main():    
    choice = input("Choose value of n:\n1.10\n2.100\n3.1000\n4.10000\n5.100000\n6.10000000\n")
    n = 10;
    board
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
    for i in range(n):
        for j in range(n):
            if(list[i] == i + j):
                board[i][j] = 1
        
    
    #print(list)

main()
class Queen:
    
    def __init__(self, board):
        self.variables = list()
        self.constraints = list()
        return None

