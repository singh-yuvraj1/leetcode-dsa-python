# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

 

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

#---------------------------------Brute Force Solution-------------------------------
class Solution(object):
    def maxArea(self, height):
        max_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i+1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        
        return max_area
if __name__== "__main__":     
    a = Solution()
    height1 = [1,8,6,2,5,4,8,3,7]
    print(a.maxArea(height1))  # Output: 49

    height2 = [1,1]
    print(a.maxArea(height2))  # Output: 1

# time complexity: O(n^2) - We have two nested loops, each iterating through the height array.
# space complexity: O(1) - We are using a constant amount of extra space to store the max_area variable.