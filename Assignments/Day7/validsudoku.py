class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9): #goes by each row to check if repeated numbers
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        

        for j in range(9): #goes down by col
            seen = set()
            for i in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        for box_row in range(0, 9, 3): #grabs each box starting top left corner and then top middle box
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j] #traverses through each square in the 3x3 box
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True
