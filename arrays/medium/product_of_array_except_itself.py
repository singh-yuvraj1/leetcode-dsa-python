# 238. Product of Array Except Self

# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#---------------------------------Brute-Force Solution-------------------------------
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    answer[i] *= nums[j]
        
        return answer
if __name__== "__main__":
    a = Solution()
    nums1 = [1,2,3,4]
    print(a.productExceptSelf(nums1))  # [24,12,8,6]

    nums2 = [-1,1,0,-3,3]
    print(a.productExceptSelf(nums2))  # [0,0,9,0,0]
## Time Complexity: O(n^2) where n is the length of the input array. We have two nested loops, each iterating over the array.
## Space Complexity: O(n) where n is the length of the input array. We create a new array answer of the same length to store the results.   


#---------------------------------Two Pointer Solution-------------------------------
class Solution1(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
if __name__== "__main__":
    a = Solution1()
    nums1 = [1,2,3,4]
    print(a.productExceptSelf(nums1))  # [24,12,8,6]

    nums2 = [-1,1,0,-3,3]
    print(a.productExceptSelf(nums2))  # [0,0,9,0,0]
## Time Complexity: O(n) where n is the length of the input array. We traverse the array three times: once for the left products, once for the right products, and once to combine them.
## Space Complexity: O(n) where n is the length of the input array. We create a new array answer of the same length to store the results.


