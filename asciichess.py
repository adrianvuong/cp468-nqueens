import math
queen = '[♕]'
empty_square = '[ ]'
cnt = 0

boardLength = input("Enter board size (N): ")
boardLength = int(boardLength)

queens = [0 for i in range (boardLength * boardLength)]
queens[4] = 1
queens[9] = 1
queenlocs = []
sq_count = 0
for j in range (1, boardLength+1):
    for i in range (1, boardLength+1):
        if queens[sq_count] == 1:
            print(queen, end="")
            queenlocs.append(sq_count + 1)
        else:
            print (empty_square, end="")
        sq_count += 1
    print()

for i in queenlocs:
    print("Queen " + str(i) + " at row " + str(queenlocs[0] // boardLength) + " and column " + str(queenlocs[0] % boardLength))
