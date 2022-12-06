from random import choice

class Board:

    def __init__(self, n):
        self._n = n
        self._queen_rows = {i: set() for i in range(1, self._n+1)}
        self._queen_posdiag = {i: set() for i in range(1, 2 * self._n)}
        self._queen_negdiag = {i: set() for i in range(1, 2 * self._n)}

    def set_queen(self, x, y, constraints):

        combined = self._queen_rows[y] | self._queen_posdiag[y+(x-1)] | self._queen_negdiag[y + (self._n - x)]

        for i in combined:
            constraints[i] += 1

        self._queen_rows[y].add(x)
        self._queen_posdiag[y+(x-1)].add(x)
        self._queen_negdiag[y+(self._n - x)].add(x)

        constraints[x] = len(combined)
        return

    def remove_queen(self, x, y, constraints):

        combined = self._queen_rows[y] | self._queen_posdiag[y+(x-1)] | self._queen_negdiag[y + (self._n - x)]

        for i in combined:
            constraints[i] -= 1

        self._queen_rows[y].remove(x)
        self._queen_posdiag[y+(x-1)].remove(x)
        self._queen_negdiag[y+(self._n - x)].remove(x)

        constraints[x] = 0
        return

    def get_num_conflicts(self, x, y):

        combined = self._queen_rows[y] | self._queen_posdiag[y+(x-1)] | self._queen_negdiag[y + (self._n - x)]

        return len(combined)


class CSP:

    def __init__(self, variables , domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints


def min_conflicts(csp, n, board, max_steps=100):

    past_var = {}
    past_queen = None

    x = 50 if n >= 100 else (n//2)

    for i in range(1, max_steps+1):
        conflicted = [i for i, j in csp.constraints.items() if j != 0]

        if conflicted == []:
            print('Steps: {}'.format(i))
            return csp

        if past_queen is not None and past_queen in conflicted:
            conflicted.remove(past_queen)

        var = choice(conflicted)
        past_queen = var
        board.remove_queen(var, csp.domains[var], csp.constraints)

        if var in past_var:
            if csp.domains[var] not in past_var[var]:
                past_var[var].append(csp.domains[var])
        else:
            past_var[var] = [csp.domains[var]]

        value = conflicts(var, csp.domains[var], n, csp, past_var[var], board)
        if len(past_var[var]) >= x: past_var[var].pop(0)

        csp.domains[var] = value
        board.set_queen(var, value, csp.constraints)
    return False


def get_least_conflicts_y(x, n, possible, board):

    conflict_list, min_count = [possible[0]], board.get_num_conflicts(x, possible[0])

    for i in possible[1:]:
        count = board.get_num_conflicts(x, i)
        if min_count > count:
            min_count = count
            conflict_list = [i]
        elif min_count == count:
            conflict_list.append(i)

    return choice(conflict_list)


def conflicts(var, v, n, csp, not_possible, board):

    x, y = var, v
    conflict_list, min_count = [], None

    for i in range(1, n+1):
        if i == y: continue
        count = board.get_num_conflicts(x, i)
        if min_count is not None and min_count > count:
            min_count = count
            conflict_list = [i]
        elif min_count is not None and min_count == count:
            conflict_list.append(i)
        elif min_count is None:
            min_count = count
            conflict_list = [i]

    clist = list(set(conflict_list) - set(not_possible))
    if clist != []:
        return choice(clist)

    return choice(conflict_list)

def create_board(n):
    return [['-']*n for i in range(n)]

def print_board(board):
    for x in board:
        for y in x:
            print(y, end=' ')
        print()
    return

def print_boardtofile(board):
    with open("output.txt", "w") as f:
        for x in board:
            for y in x:
                f.write(y)
        f.write("\n")
    return
