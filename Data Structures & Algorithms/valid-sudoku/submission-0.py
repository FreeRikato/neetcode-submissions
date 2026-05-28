class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsHashmap = defaultdict(list)
        colsHashmap = defaultdict(list)
        boxHashmap = defaultdict(list)

        for row in range(len(board[0])):
            for col in range(len(board)):
                if (board[row][col] in rowsHashmap[row] or board[row][col] in colsHashmap[col] or board[row][col] in boxHashmap[(row//3, col//3)]):
                    return False

                if(board[row][col].isdigit()):
                    rowsHashmap[row].append(board[row][col])
                    colsHashmap[col].append(board[row][col])
                    boxHashmap[(row//3, col//3)].append(board[row][col])
        return True
