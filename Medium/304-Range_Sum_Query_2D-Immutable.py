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