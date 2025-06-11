class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])  
        result = []
        visited = [[False] * n for _ in range(m)]#if seen or not

    
        directions = [(0,1), (1,0), (0,-1), (-1,0)] #right down left right
        dir_idx = 0  #start with right
    
        row, col = 0, 0  #first number started

        for _ in range(m * n): #want to iterate by size of matrix so all  the numbers
            result.append(matrix[row][col]) 
            visited[row][col] = True #if appended make visitied true

       
            next_row = row + directions[dir_idx][0] #make it by the direction so if it is right it will add 0 to row and 1 to col
            next_col = col + directions[dir_idx][1]

            if (0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]): #if within bounds and not visited then the new row and col will be appended
            
                row, col = next_row, next_col
            else:
            
                dir_idx = (dir_idx + 1) % 4 #if cannot move further then change direction by doing the next direction listed in directions
                row += directions[dir_idx][0] #add this new row and col in result
                col += directions[dir_idx][1]

        return result
