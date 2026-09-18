class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [row[:] for row in matrix]
        for i in range(1, len(matrix)):
            self.prefix[i][0] += self.prefix[i-1][0]
        for j in range(1, len(matrix[0])):
            self.prefix[0][j] += self.prefix[0][j-1]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefix[i][j] = matrix[i][j] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.prefix[row2][col2]
        if row1 != 0:
            bottom_right -= self.prefix[row1-1][col2] 
        if col1 != 0:
            bottom_right -= self.prefix[row2][col1-1]
        if row1 != 0 and col1 != 0:
            bottom_right += self.prefix[row1-1][col1-1]
        return bottom_right


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)