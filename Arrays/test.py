def isValidSudoku(board):
        d = {}
        for i in range(9):        
            d = {}
            for j in range(9):
                if(board[i][j] != "."):
                    if(board[i][j] not in d):
                        d[board[i][j]] = 1
                    else:
                        return False
                if(board[j][i] != "."):
                    if(board[j][i] not in d):
                        d[board[j][i]] = 1
                    else:
                        return False
        sqCol = 0
        sqRow = 0
        while(sqCol <= 9 and sqRow <= 6):      
            d = {}
            for i in range(3):
                for j in range(3):
                    if(board[i + sqRow][j + sqCol] != "."):
                        if(board[i + sqRow][j + sqCol] not in d):
                            d[board[i + sqRow][j + sqCol]] = 1
                        else:
                            return False
            sqCol += 3
            if(sqCol == 9):
                sqCol = 0
                sqRow += 3
        return True


board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))


