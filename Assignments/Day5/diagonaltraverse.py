class Solution(object):
    def findDiagonalOrder(self,mat):
        if not mat or not mat[0]: #check if there is no rows or columns 
            return []

        m, n = len(mat), len(mat[0]) #initializes rows by columns
        result = []

        for d in range(m + n - 1): #traverses through number of diagonals
            intermediate = []

            if d < n: #start diagonal in top row
                row = 0
                col = d
            else: #or start row in rightmost corner
                row = d - n + 1
                col = n - 1

            while row < m and col >= 0: #conditions to be inside matrix
                intermediate.append(mat[row][col])
                row += 1 #moving down and to the left
                col -= 1

            if d % 2 == 0: #diagonals on even numbers start left to right
                result.extend(intermediate[::-1]) #must reverse order
            else:
                result.extend(intermediate) #keeps order

        return result


