# 2553. Separate the Digits in an Array
# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 

# Example 1:

# Input: nums = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.


# Example 2:

# Input: nums = [7,1,3,9]
# Output: [7,1,3,9]
# Explanation: The separation of each integer in nums is itself.
# answer = [7,1,3,9].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105

#--------------------brute force solution--------------------
class Solution(object):
    def separateDigits(self, nums):
        answer = []
        
        for num in nums:
            digits = list(str(num))
            answer.extend(int(digit) for digit in digits)
        
        return answer
if __name__== "__main__":
    a = Solution()
    nums1 = [13,25,83,77]
    print(a.separateDigits(nums1))  # [1,3,2,5,8,3,7,7]

    nums2 = [7,1,3,9]
    print(a.separateDigits(nums2))  # [7,1,3,9]
## Time Complexity: O(n * m) where n is the number of integers in the input array and m is the average number of digits in each integer. This is because we iterate through each integer and then through each digit of that integer.
## Space Complexity: O(n * m) in the worst case, where n is the number of integers in the input array and m is the average number of digits in each integer. This is because we are creating a new list to store the separated digits, which could potentially contain all the digits of all the integers in the input array.
