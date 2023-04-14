class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.check_valid(row):
                return False
        
        # check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.check_valid(column):
                return False
        
        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                if not self.check_valid(sub_box):
                    return False
        
        return True
    
    def check_valid(self, lst: List[str]) -> bool:
        nums = [n for n in lst if n != '.']
        return len(set(nums)) == len(nums)