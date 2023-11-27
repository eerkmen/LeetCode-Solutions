#calculate submatrix

#brute force
#pseudocode: for row1 to row2
#               for col1 to col2
#                 sum


#prefix sum
#calculate sum time complexity: O(n)
#bottom right corner of submatrix will store the sum of all submatrix
#first step:calculate prefix sum of the first row
#second step: add the above value and and left value to calculate the total sum of the submatrix
#edge case: if no row above, if no column left
#to get rid of it: make the matrix one unit larger and add have 0s in the new column and row
#prework for the matrix: O(n^2)
#every single call afterwards is O(1) time complexity
#memory: O(n^2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for c in range(ROWS + 1)]

        for r in range(ROWS):
            prefix= 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1

        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)