# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


# Example 2:
# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


#----------------------------------Brute Force Solution----------------------------------
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        missing_numbers = []
        
        for i in range(1, n + 1):
            if i not in nums:
                missing_numbers.append(i)
        
        return missing_numbers
if __name__== "__main__":
    a = Solution()
    nums1 = [4,3,2,7,8,2,3,1]
    print(a.findDisappearedNumbers(nums1))  # [5,6]

    nums2 = [1,1]
    print(a.findDisappearedNumbers(nums2))  # [2]

## Time Complexity: O(n^2) where n is the length of the input array nums. We have a loop that iterates through the numbers from 1 to n, and for each number, we check if it is present in the nums array using the "in" operator, which takes O(n) time in the worst case.
## Space Complexity: O(m) where m is the number of missing numbers in the range [1, n]. In the worst case, if all numbers from 1 to n are missing, we would need to store all n numbers in the missing_numbers list, resulting in O(n) space complexity.

