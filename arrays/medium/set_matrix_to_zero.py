# 73. Set Matrix Zeroes
# Hint
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

#----------------------------------Brute Force Solution----------------------------------
class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = []
        zero_cols = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

if __name__== "__main__":
    a = Solution()
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    a.setZeroes(matrix1)
    print(matrix1)  # [[1,0,1],[0,0,0],[1,0,1]]

    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    a.setZeroes(matrix2)
    print(matrix2)  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Time Complexity: O(mn) where m is the number of rows and n is the number of columns in the input matrix. We have two nested loops that iterate through the matrix to find the zero elements and set the corresponding rows and columns to zero.
## Space Complexity: O(m + n) since we are using two additional lists to store the indices of the rows and columns that need to be set to zero. In the worst case, if all elements in the matrix are zero, we would need to store all row and column indices, resulting in O(m + n) space complexity.



#----------------------------------Optimal Solution----------------------------------
class Solution1(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
if __name__== "__main__":
    a = Solution1()
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    a.setZeroes(matrix1)
    print(matrix1)  # [[1,0,1],[0,0,0],[1,0,1]]

    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    a.setZeroes(matrix2)
    print(matrix2)  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
## Time Complexity: O(mn) where m is the number of rows and n is the number of columns in the input matrix. We have two nested loops that iterate through the matrix to find the zero elements and set the corresponding rows and columns to zero.
## Space Complexity: O(1) since we are using only a constant amount of extra space to store the boolean variables for the first row and first column. We are modifying the input matrix in place without using any additional data structures that grow with the input size.
