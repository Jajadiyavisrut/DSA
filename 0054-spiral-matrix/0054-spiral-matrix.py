class Solution(object):
    def spiralOrder(self, matrix):
        
        add = []
        upper, lower = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while left<=right and upper<=lower:
            for col in range(left,right+1):
                add.append(matrix[upper][col])
            upper+=1
            for row in range(upper,lower+1):
                add.append(matrix[row][right])
            right-=1
            if upper<=lower:
                for col in range(right,left-1,-1):
                    add.append(matrix[lower][col])
                lower-=1
            if left<=right:
                for row in range(lower,upper-1,-1):
                    add.append(matrix[row][left])
                left+=1
        return add