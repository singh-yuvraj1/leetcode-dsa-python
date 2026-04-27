# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


# Solution brute force
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        total_water = 0
        for i in range(1, len(height) - 1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            water_level = min(left_max, right_max)
            if water_level > height[i]:
                total_water += water_level - height[i]
        return total_water
if __name__== "__main__":
    a = Solution()
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(a.trap(height1))  # 6

    height2 = [4,2,0,3,2,5]
    print(a.trap(height2))  # 9
## Time Complexity: O(n^2) where n is the length of the input array. We have a loop that iterates through each index of the array, and for each index, we calculate the maximum height to the left and right, which takes O(n) time.
## Space Complexity: O(1) since we are not using any additional data structures that grow


# Solution optimal
class Solution1(object):
    def trap(self, height):
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += max(0, right_max - height[right])
        
        return total_water
if __name__== "__main__":
    a = Solution1()
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(a.trap(height1))  # 6

    height2 = [4,2,0,3,2,5]
    print(a.trap(height2))  # 9
## Time Complexity: O(n) where n is the length of the input array. We have a single loop that iterates through the array once.
## Space Complexity: O(1) since we are not using any additional data structures that grow with the input size. We are only using a constant amount of space for the pointers and variables. 