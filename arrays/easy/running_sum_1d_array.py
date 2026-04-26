# 1480. Running Sum of 1d Array
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


# -----------------------------------solution 1: Brute Force Solution----------------------------------------------
class Solution(object):
    def runningSum(self, nums):
        running_sum = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        
        return running_sum
    
if __name__== "__main__":
    a = Solution()
    nums1 = [1,2,3,4]
    print(a.runningSum(nums1))  # [1,3,6,10]

    nums2 = [1,1,1,1,1]
    print(a.runningSum(nums2))  # [1,2,3,4,5]

    nums3 = [3,1,2,10,1]
    print(a.runningSum(nums3))  # [3,4,6,16,17]

## Time Complexity: O(n) where n is the length of the input array. We iterate through the array once to calculate the running sum.
## Space Complexity: O(n) since we are creating a new list to store the running sums, which can grow up to the size of the input array.



# ------------------------------------optimal solution-----------------------------------------------
# -----------------------------------solution 2: In-place Solution----------------------------------------------
class Solution1(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
if __name__== "__main__":
    a = Solution1()
    nums1 = [1,2,3,4]
    print(a.runningSum(nums1))  # [1,3,6,10]

    nums2 = [1,1,1,1,1]
    print(a.runningSum(nums2))  # [1,2,3,4,5]

    nums3 = [3,1,2,10,1]
    print(a.runningSum(nums3))  # [3,4,6,16,17]
## Time Complexity: O(n) where n is the length of the input array. We iterate through the array once to calculate the running sum.
## Space Complexity: O(1) since we are modifying the input array in place and not using any additional data structures that grow with the input size.