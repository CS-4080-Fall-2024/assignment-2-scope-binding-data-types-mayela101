class Solution:
    def SolveSudoku(self, board) -> None:
        empty_cell = "."

        def check_value(i, j, input) -> bool:
            # Row 
            for x in board[i]:
                if x == input:
                    return False
            
            # Column 
            for row in range(9):
                if board[row][j] == input:
                    return False

            # Subgrid 
            start_i = (i // 3) * 3
            start_j = (j // 3) * 3
            
            for temp_i in range(start_i, start_i + 3):
                for temp_j in range(start_j, start_j + 3):
                    if board[temp_i][temp_j] == input:
                        return False       
            return True
        
        def solve() -> bool: 
            for x in range(9):
                for y in range(9):
                    if board[x][y] == empty_cell:
                        for value in range(1, 10):
                            choice = str(value)

                            if check_value(x, y, choice):
                                board[x][y] = choice

                                if solve():
                                    return True
                                
                                board[x][y] = empty_cell
                        return False
            return True

        solve()


solution = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solution.SolveSudoku(board)
print(board)

