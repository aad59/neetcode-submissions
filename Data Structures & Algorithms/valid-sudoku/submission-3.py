class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == ".":
                            continue
                        if board[i+k][j+l] in seen:
                            return False
                        seen.add(board[i+k][j+l])
        
        return True