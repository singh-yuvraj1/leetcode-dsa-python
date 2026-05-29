# 3300. Minimum Element After Replacement With Digit Sum
# Hint
# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.

# Return the minimum element in nums after all replacements.


# Example 1:
# Input: nums = [10,12,13,14]
# Output: 1
# Explanation:
# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.


# Example 2:
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation:
# nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.


# Example 3:
# Input: nums = [999,19,199]
# Output: 10
# Explanation:
# nums becomes [27, 10, 19] after all replacements, with minimum element 10.


# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 104


#solution 1--- Brute Force Solution --- Nested loops
class Solution(object):
    def minimumElementAfterReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minNum = float('inf')

        for num in nums:

            sumOfDigits = 0

            while num > 0:
                sumOfDigits += num % 10
                num //= 10

            minNum = min(minNum, sumOfDigits)

        return minNum
if __name__ == "__main__":
    nums = [10,12,13,14]
    print(Solution().minimumElementAfterReplacement(nums))
#output: 1
#time complexity: O(n * m) where n is the length of nums and m is the number of digits in the largest number in nums
#space complexity: O(1) bcoz we are using only a constant amount of extra space to store the minimum number and the sum of digits.


#optimized solution--- Using a helper function to calculate the sum of digits
class Solution(object):
    def sumOfDigits(self, num):
        sumOfDigits = 0

        while num > 0:
            sumOfDigits += num % 10
            num //= 10

        return sumOfDigits

    def minimumElementAfterReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minNum = float('inf')

        for num in nums:
            minNum = min(minNum, self.sumOfDigits(num))

        return minNum
if __name__ == "__main__":
    nums = [10,12,13,14]
    print(Solution().minimumElementAfterReplacement(nums))
#output: 1
#time complexity: O(n * m) where n is the length of nums and m is the number of digits in the largest number in nums
#space complexity: O(1) bcoz we are using only a constant amount of extra space to store the minimum number and the sum of digits.