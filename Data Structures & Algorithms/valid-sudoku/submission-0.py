class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # row check

        for row in range(9):
            
            row_set = set()
            
            for col in range(9):
                digit = board[row][col]

                if digit == '.':
                    continue

                if digit in row_set:
                    return False
                else:
                    row_set.add(digit)

        # col check

        for col in range(9):

            col_set = set()
            
            for row in range(9):
                digit = board[row][col]

                if digit == '.':
                    continue

                if digit in col_set:
                    return False
                else:
                    col_set.add(digit)

        # sub-box check

        sub_box_to_set_map = {}

        for row in range(9):
            for col in range(9):
                
                digit = board[row][col]

                if digit == '.':
                    continue

                current_box = (row // 3, col // 3)

                if current_box not in sub_box_to_set_map:
                    sub_box_to_set_map[current_box] = set()

                if digit in sub_box_to_set_map[current_box]:
                    return False
                else:
                    sub_box_to_set_map[current_box].add(digit)

        return True