# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

#------------------------------Solution-------------------------------
class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result
    
#------------------------------Another Way to solve------------------------------- but not good bcoz it takes O(n log n) time due to the sorting step, while the two-pointer approach takes O(n) time. The space complexity is O(n) for both approaches since we are creating a new array to store the squared values.
class Solution1(object):
    def sortedSquares(self, nums):
        return sorted(x ** 2 for x in nums)

if __name__== "__main__":
    a = Solution()
    nums1 = [-4,-1,0,3,10]
    print(a.sortedSquares(nums1))  # [0,1,9,16,100]
    
    b = Solution1()                     
    nums2 = [-7,-3,2,3,11]
    print(b.sortedSquares(nums2))  # [4,9,9,49,121]