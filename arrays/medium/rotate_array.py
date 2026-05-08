# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


#SOlution 1: Using extra space ------brute force approach
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle cases where k is greater than n
        rotated = [0] * n
        
        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]
if __name__== "__main__":
    a = Solution()
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    a.rotate(nums1, k1)
    print(nums1)  # Output: [5,6,7,1,2,3,4]

    nums2 = [-1,-100,3,99]
    k2 = 2
    a.rotate(nums2, k2)
    print(nums2)  # Output: [3,99,-1,-100]
#time complexity: O(n), where n is the length of the input array nums. We iterate through the array twice: once to create the rotated array and once to copy it back to nums.
#space complexity: O(n), as we are using an additional array of the same size as nums to store the rotated elements.



