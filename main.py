def cloneBoard(board):
    return [row[:] for row in board]

def printBoard(board):
    # board is a list of lists
    N = len(board)
    for i in range(N):
        for j in range(N-1):
            print(board[N-i-1][j], end='|')
        print(board[N-i-1][N-1])

def playerWin(board, player):
    N = len(board)
    idealList = [player for _ in range(N)]
    #Check row
    for columnIndex in range(N):
        helperList = []
        for rowIndex in range(N):
            helperList.append(board[columnIndex][rowIndex])
        
        if player == 1 and helperList == idealList:
            return True
        elif player == 2 and helperList == idealList:
            return True
        else:
            helperList = []
    #Check column
    for columnIndex in range(N):
        helperList = []
        for rowIndex in range(N):
            helperList.append(board[rowIndex][columnIndex])
        
        if player == 1 and helperList == idealList:
            return True
        elif player == 2 and helperList == idealList:
            return True
        else:
            helperList = []
    #Check diagonal. Top to bottom. Left to right
    helperList = []
    indexList = []
    for index in range(N):
        helperList.append(board[index][index])
        indexList.append(index)
    if player == 1 and helperList == idealList:
        return True
    elif player == 2 and helperList == idealList:
        return True
    #Check diagonal. Top to bottom. Right to left
    helperList = []
    indexListInverted = indexList[::-1]
    for _ in indexList:
        helperList.append(board[indexListInverted[_]][indexList[_]])
    if player == 1 and helperList == idealList:
        return True
    elif player == 2 and helperList == idealList:
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
    maximizingPlayer = 1 if maximizingPlayer else 2
    N = len(board)
    list_of_boards = []
    for nothingY in range(N):
        for nothingX in range(N):
            if board[nothingY][nothingX] == 0:
                board2 = cloneBoard(board)
                board2[nothingY][nothingX] = maximizingPlayer
                list_of_boards.append(board2)
    return list_of_boards

def boardDiff(board1, board2):
    N = len(board1)
    for y in range(N):
        for x in range(N):
            if board1[y][x] != board2[y][x]:
                return y, x
    # illegal position. Means boards are identical.
    return -1, -1

def alpha_beta(board, depth, alpha, beta, row, column, maximizingPlayer):
    if depth == 0 or isTerminal(board):
        return score(board, maximizingPlayer), row, column
    if maximizingPlayer == 1:
        value = float('-inf')
        for child in possibleMoves(board, maximizingPlayer):
            moveRow, moveColumn = boardDiff(board, child)
            tmpValue, _, _ = alpha_beta(child, depth-1, alpha, beta, moveRow, moveColumn, False)
            if tmpValue > value:
                value = tmpValue
            if value >= beta:
                break
            if value > alpha:
                alpha = value
                row, column = moveRow, moveColumn
        return value, row, column
    else:
        value = float('inf')
        for child in possibleMoves(board, maximizingPlayer):
            moveRow, moveColumn = boardDiff(board, child)
            tmpValue, _, _ = alpha_beta(child, depth-1, alpha, beta, moveRow, moveColumn, True)
            if tmpValue < value:
                value = tmpValue
            if value <= alpha:
                break
            if value < beta:
                beta = value
                row, column = moveRow, moveColumn
        return value, row, column

def playerPositionQuery():
    row = int(input("Choose row: "))
    column = int(input("Choose column: "))
    return row, column

if __name__ == '__main__':
    board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    print(isTerminal(board))

    ## Board assumes 0 == empty, 1 == human, 2 == AI
    print("Tic Tac Toe solver")
    humanFirst = int(input("Choose who goes first # (1 or 2): "))
    width = int(input("Choose board width and/or height (defaults to 3):"))
    board = [[0 for _ in range(width)] for _ in range(width)]
    printBoard(board)
    humanPlaying = humanFirst
    while True:
        if humanPlaying:
            while True:
                tokenRow, tokenColumn = playerPositionQuery()
                if board[tokenRow][tokenColumn] == 0:
                    break
            board[tokenRow][tokenColumn] = 1
        else:
            # AI plays first
            _, moveRow, moveColumn = alpha_beta(board, 10, float('-inf'), float('inf'), 0, 0, 2)
            board[moveRow][moveColumn] = 2
        humanPlaying = not humanPlaying
        printBoard(board)
        print()
        if isTerminal(board):
            break
