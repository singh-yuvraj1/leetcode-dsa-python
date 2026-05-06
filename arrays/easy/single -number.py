# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

 
# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

#solution 1: Using brute force
class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i
if __name__== "__main__":
    a = Solution()
    nums1 = [2,2,1]
    print(a.singleNumber(nums1))  # 1

    nums2 = [4,1,2,1,2]
    print(a.singleNumber(nums2))  # 4

    nums3 = [1]
    print(a.singleNumber(nums3))  # 1
#time complexity: O(n^2), where n is the length of the input array nums. In the worst case, we may have to check each element in the array against every other element to count its occurrences, leading to O(n
#space complexity: O(1), as we are using only a constant amount of extra space to store the count of occurrences.
