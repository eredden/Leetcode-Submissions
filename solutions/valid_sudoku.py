# https://leetcode.com/submissions/detail/1210236000/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check rows
        for row in board:
            row_numbers = set()

            for num in row:
                if num == ".":
                    continue
                elif num in row_numbers:
                    return False
                else:
                    row_numbers.add(num)

        # check columns
        for column in range(0, 9):
            col_numbers = set()

            for row in board:
                num = row[column]

                if num == ".":
                    continue
                elif num in col_numbers:
                    return False
                else:
                    col_numbers.add(num)

        # check squares
        for c in range(0, 3):
            for r in range(0, 3):
                sqr_numbers = set()
                col_index = c * 3
                row_index = r * 3
            
                for col in range(col_index, col_index + 3):
                    for row in range(row_index, row_index + 3):
                        num = board[row][col]

                        if num == ".":
                            continue
                        elif num in sqr_numbers:
                            return False
                        else:
                            sqr_numbers.add(num)

        return True