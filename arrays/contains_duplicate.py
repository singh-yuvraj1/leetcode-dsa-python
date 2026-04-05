# Problem 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


#code

class Solution:
    def contains_duplicate(self,nums):
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num] = 1
        return False
 #time complexity ---->>>>O(n)


#  Optimized Way
class SolutionOptimized:
    def contains_duplicate(self,nums):
        return len(nums) != len(set(nums))
    
 #time complexity ---->>>>O(n)


if __name__== "__main__":
    s1 = Solution()
    print(s1.contains_duplicate([1,2,3,1]))

    s2=SolutionOptimized()
    print(s2.contains_duplicate([1,2,3,4]))