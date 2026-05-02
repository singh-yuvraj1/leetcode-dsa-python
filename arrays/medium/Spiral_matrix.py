# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


#------------------------------------Brutre Force------------------------------------
def spiralOrder(matrix):
    res = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # 1. left → right
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1

        # 2. top → bottom
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        # 3. right → left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        # 4. bottom → top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1) if we don't consider the output list, otherwise O(m*n) for the output list.



#------------------------------------Optimal Solution [Using Directional Traversal]------------------------------------
def spiralOrder(matrix):
    res = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_index = 0
    row, col = 0, 0

    for _ in range(len(matrix) * len(matrix[0])):
        res.append(matrix[row][col])
        matrix[row][col] = None  # Mark as visited

        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]

        if (0 <= next_row < len(matrix) and
            0 <= next_col < len(matrix[0]) and
            matrix[next_row][next_col] is not None):
            row, col = next_row, next_col
        else:
            direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]

    return res
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1) if we don't consider the output list, otherwise O(m*n) for the output list.