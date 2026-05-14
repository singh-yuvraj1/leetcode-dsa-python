# 1914. Cyclically Rotating a Grid
# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:
# Return the matrix after applying k cyclic rotations to it.

# Example 1:
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.


# Example 2:
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 


#solution 1: Brute Force Solution
class Solution(object):
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for _ in range(k):
            for layer in range(layers):
                top, left = layer, layer
                bottom, right = m - layer - 1, n - layer - 1
                
                # Save the top-left corner
                temp = grid[top][left]
                
                # Move left column up
                for i in range(top, bottom):
                    grid[i][left] = grid[i + 1][left]
                
                # Move bottom row left
                for j in range(left, right):
                    grid[bottom][j] = grid[bottom][j + 1]
                
                # Move right column down
                for i in range(bottom, top, -1):
                    grid[i][right] = grid[i - 1][right]
                
                # Move top row right
                for j in range(right, left + 1, -1):
                    grid[top][j] = grid[top][j - 1]
                
                # Place the saved value in the new position
                grid[top][left + 1] = temp
        
        return grid
if __name__== "__main__":
    a = Solution()
    grid1 = [[40,10],[30,20]]
    k1 = 1
    print(a.rotateGrid(grid1, k1))  # [[10,20],[40,30]]

    grid2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    k2 = 2
    print(a.rotateGrid(grid2, k2))  # [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
## Time Complexity: O(k * m * n) where k is the number of rotations, m is the number of rows, and n is the number of columns in the grid. We have a loop that iterates k times, and for each rotation, we iterate through each layer of the grid, which takes O(m * n) time.
## Space Complexity: O(1) since we are performing the rotations in place and not using any additional data structures that grow with the input size. We are only using a constant amount of space for temporary variables.


#solution 2: Optimized Solution
class Solution1(object):
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1
            
            # Extract the elements of the current layer
            elements = []
            for j in range(left, right + 1):
                elements.append(grid[top][j])
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])
            
            # Rotate the elements
            k_mod = k % len(elements)
            rotated_elements = elements[-k_mod:] + elements[:-k_mod]
            
            # Place the rotated elements back into the grid
            idx = 0
            for j in range(left, right + 1):
                grid[top][j] = rotated_elements[idx]
                idx += 1
            for i in range(top + 1, bottom + 1):
                grid[i][right] = rotated_elements[idx]
                idx += 1
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = rotated_elements[idx]
                idx += 1
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated_elements[idx]
                idx += 1
        
        return grid
if __name__== "__main__":
    a = Solution1()
    grid1 = [[40,10],[30,20]]
    k1 = 1
    print(a.rotateGrid(grid1, k1))  # [[10,20],[40,30]]

    grid2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    k2 = 2
    print(a.rotateGrid(grid2, k2))  # [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
## Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. We iterate through each layer of the grid, which takes O(m * n) time, and we perform a constant amount of work for each layer.
## Space Complexity: O(m * n) in the worst case, where m is the number of rows and n is the number of columns in the grid. We create a list to store the elements of each layer, which can take up to O(m * n) space in the worst case if the grid has only one layer. However, since we are rotating the elements in place, we do not use any additional space for the rotated elements, so the overall space complexity is O(m * n).
