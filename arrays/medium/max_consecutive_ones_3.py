# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


#brute force solution
class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        ans = 0

        for i in range(n):
            zeros = 0

            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1

                if zeros <= k:
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(Solution().longestOnes(nums, k))
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(Solution().longestOnes(nums, k))
#output: 6, 10
#time complexity: O(n²) because we are using two nested loops to check all possible subarrays.
#space complexity: O(1) because we are using only a constant amount of extra space


