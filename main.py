
def printBoard(board):
    # board is a list of lists
    N = len(board)
    for i in range(N):
        for j in range(N-1):
            print(board[N-i-1][j], end='|')
        print(board[N-i-1][N-1])

def playerWin(board, player):
    N = len(board)
    for x in range(N):
        for y in range(1, N):
            if board[y][x] != board[y-1][x] or board[y][x] != player or board[y-1][x] != player:
                sentinel = sentinel and False
    if sentinel:
        return True

    for y in range(N):
        for x in range(1, N):
            if board[y][x] != board[y][x-1] or board[y][x] != player or board[y][x-1] != player:
                sentinel = sentinel and False
    if sentinel:
        return True

    x, y = 1, 1
    for s in range(N-1):
        if board[y+s][x+s] != board[y-1+s][x-1+s] or board[y+s][x+s] != player or board[y-1+s][x-1+s] != player:
            sentinel = sentinel and False
    if sentinel:
        return True

    x, y = N-2, 1
    for s in range(N-1):
        if board[y+s][x-s] != board[y+1+s][x+1-s] or board[y+s][x-s] != player or board[y+1+s][x+1-s] != player:
            sentinel = sentinel and False
    if sentinel:
        return True

    return False

# Returns true when no more moves are possible. Either a player won or there is a draw (i.e. no empty cells).
def isTerminal(board):
    # empty cells means no more moves are allowed
    emptyCells = sum([1 for row in board for element in row if element == 0])
    if emptyCells == 0:
        return True
    return playerWin(board, 1) or playerWin(board, 2)

def score(board, maximizingPlayer):
    sentinel = True
    N = len(board)
    winPlayer1 = playerWin(board, 1)
    winPlayer2 = playerWin(board, 2)
    if maximizingPlayer == 1:
        if winPlayer1:
            return 1
        elif winPlayer2:
            return -1
        return 0
    else:
        if winPlayer2:
            return 1
        elif winPlayer1:
            return -1
        return 0

def possibleMoves(board, maximizingPlayer):
    # get list for empty cells coordinates
    # iterate over coordinate list:
    #   place a token in coordinate element
    #   store new board as part of the result
    pass

def alpha_beta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isTerminal(board):
        return score(board, maximizingPlayer)
    if maximizingPlayer == 1:
        value = -infinity
        for child in possibleMoves(board, maximizingPlayer):
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            if value >= beta:
                break
            alpha = max(alpha, value)
        return value
    else:
        value = infinity
        for child in possibleMoves(board, maximizingPlayer):
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            if value <= alpha:
                break
            beta = min(beta, value)
        return value

if __name__ == '__main__':
    ## Board assumes 0 == empty, 1 == player 1, 2 == player 2
    print("Tic Tac Toe solver")
    selfPlayer = int(input("Choose player # (1 or 2): "))
    width = int(input("Choose board width and/or height (defaults to 3):"))
    board = [[0 for _ in range(width)] for _ in range(width)]
    #TODO: game flow with 2 players.
