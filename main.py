import sys, time

from copy import deepcopy
from nqueens import Board, CSP
from nqueens import *
from random import choice

#option = input("Choose value of n:\n1.10\n2.100\n3.1000\n4.10000\n5.100000\n6.10000000\n")
n = int(input("choose value of n\n"))
# match option:
#     case "1":
#         n = 10
#     case "2":
#         n = n*n
#     case "3":
#         n = n*n*n
#     case "4":
#         n = n*n*n*n
#     case "5":
#         n = n*n*n*n*n
#     case "6":
#         n = n*n*n*n*n*n
#     case _:
#         print("Invalid value")

start_time = time.time()
board = Board(n)
variables = [i for i in range(1, n+1)]
_var = deepcopy(variables)
constraints = {i: 0 for i in variables}
y = choice(_var)
domains = {1: y}
_var.remove(y)
board.set_queen(1, y, constraints)


for i in range(2, n+1):
    y = get_least_conflicts_y(i, n, _var, board)
    domains[i] = y
    board.set_queen(i, y, constraints)
    _var.remove(y)

csp = CSP(variables, domains, constraints)

if(n <= 100):
    print('\nInitial Board')
    b = create_board(n)
    for key, value in csp.domains.items():
        if constraints[key] > 0:
            b[value-1][key -1] = 'Q' 
        else:
            b[value - 1][key - 1] = 'Q' 

    print_board(b)

solve_time = time.time()
assignment = min_conflicts(csp, n, board)

if assignment:
    end_time = time.time()
    print('Solve Time: {:0.5f} secs'.format(end_time - solve_time))

    if(n <= 100):
        print('\nSolved')
        b = create_board(n)
        for key, value in assignment.domains.items():
            b[value - 1][key - 1] ='Q' 

        print_board(b)

        #print("Board too big, printing to file")
    with open("output.txt", "w") as f:
        for i in csp.domains:
            print(i,csp.domains[i], file = f, end = "\n")
        
else:
    print('Increase Max Steps to solve.')
