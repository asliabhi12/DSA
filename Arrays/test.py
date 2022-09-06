# def isValidSudoku(board):
#         d = {}
#         for i in range(9):        
#             d = {}
#             for j in range(9):
#                 if(board[i][j] != "."):
#                     if(board[i][j] not in d):
#                         d[board[i][j]] = 1
#                     else:
#                         return False
#                 if(board[j][i] != "."):
#                     if(board[j][i] not in d):
#                         d[board[j][i]] = 1
#                     else:
#                         return False
#         sqCol = 0
#         sqRow = 0
#         while(sqCol <= 9 and sqRow <= 6):      
#             d = {}
#             for i in range(3):
#                 for j in range(3):
#                     if(board[i + sqRow][j + sqCol] != "."):
#                         if(board[i + sqRow][j + sqCol] not in d):
#                             d[board[i + sqRow][j + sqCol]] = 1
#                         else:
#                             return False
#             sqCol += 3
#             if(sqCol == 9):
#                 sqCol = 0
#                 sqRow += 3
#         return True


# board=[["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# print(isValidSudoku(board))

# def isValidSudoku(board):
#         d = {}
#         for i in range(9):        
#             d = {}
#             for j in range(9):
#                 if(board[i][j] != "."):
#                     if(board[i][j] not in d):
#                         d[board[i][j]] = 1
#                     else:
#                         return False
#                 if(board[j][i] != "."):
#                     if(board[j][i] not in d):
#                         d[board[j][i]] = 1
#                     else:
#                         return False
#         sqCol = 0
#         sqRow = 0
#         while(sqCol <= 9 and sqRow <= 6):      
#             d = {}
#             for i in range(3):
#                 for j in range(3):
#                     if(board[i + sqRow][j + sqCol] != "."):
#                         if(board[i + sqRow][j + sqCol] not in d):
#                             d[board[i + sqRow][j + sqCol]] = 1
#                         else:
#                             return False
#             sqCol += 3
#             if(sqCol == 9):
#                 sqCol = 0
#                 sqRow += 3
#         return True


# board=[["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
            if not subRoot: return True
            if not root: return False
            
            if self.sameTree(root, subRoot):
                return True
            return (self.isSubTree(root.left, subRoot) or
                    self.isSubTree(root.right, subRoot))
        
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        return False