class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in seen and board[i][j] != ".":
                    return False
                seen.append(board[i][j])
            seen = []

            for j in range(len(board[i])):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                seen.append(board[j][i])
            seen = []

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] in seen and board[i][j] != ".":
                            return False
                        seen.append(board[i][j])


        return True
