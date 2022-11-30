import random

def randomQueens(board, n):
    randList = random.sample(range(1,n*n),n)
    
    return randList
    
def minConflicts(csp, max_steps, current):

    return None
    
def main():    
    list = randomQueens(0,10)
    print(list)


main()
