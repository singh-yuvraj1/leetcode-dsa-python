# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
 
# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:   
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

# Constraints:
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
 
# Follow up: Could you do it in O(n) time and O(1) space?


# Solution brute force
class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
if __name__== "__main__":
    a = Solution()
    nums1 = [1,7,3,6,5,6]
    print(a.pivotIndex(nums1))  # 3

    nums2 = [1,2,3]
    print(a.pivotIndex(nums2))  # -1

    nums3 = [2,1,-1]
    print(a.pivotIndex(nums3))  # 0
## Time Complexity: O(n^2) where n is the length of the input array. We have a loop that iterates through each index of the array, and for each index, we calculate the sum of the left and right subarrays, which takes O(n) time.
## Space Complexity: O(1) since we are not using any additional data structures that grow
## with the input size. We are only using a constant amount of space for the loop variable and the return value.


# Solution optimal
class Solution1(object):    
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1   
if __name__== "__main__":
    a = Solution1()
    nums1 = [1,7,3,6,5,6]
    print(a.pivotIndex(nums1))  # 3

    nums2 = [1,2,3]
    print(a.pivotIndex(nums2))  # -1

    nums3 = [2,1,-1]
    print(a.pivotIndex(nums3))  # 0
## Time Complexity: O(n) where n is the length of the input array. We calculate the total sum of the array once, which takes O(n) time, and then we iterate through the array once to find the pivot index, which also takes O(n) time.
## Space Complexity: O(1) since we are using only a constant amount of space to store the total sum, left sum, and loop variables. We are not using any additional data structures that grow with the input size.   