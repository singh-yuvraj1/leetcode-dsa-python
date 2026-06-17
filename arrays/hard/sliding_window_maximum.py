# 239. Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.


# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 


# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

#brute force
from os import name


class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
    
        for i in range(len(nums) - k + 1):
            maxi = nums[i]

            for j in range(i, i + k):
                maxi = max(maxi, nums[j])

            ans.append(maxi)

        return ans
if name == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # return [3,3,5,5,6,7]
    print(s.maxSlidingWindow([1], 1))  # return [1]
#time complexity: O(n*k) beciause we are iterating through the array of length n and for each element, we are iterating through the next k elements to find the maximum.
#space complexity: O(n-k+1) for the output array, which can be simplified to O(n) in the worst case when k is small compared to n.



#optimized solution using deque
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []

        # Initialize the deque with the first k elements
        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # Process the remaining elements
        for i in range(k, len(nums)):
            ans.append(nums[dq[0]])

            # Remove the elements that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Add the current element to the deque
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # Append the maximum of the last window
        ans.append(nums[dq[0]])

        return ans
if name == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # return [3,3,5,5,6,7]
    print(s.maxSlidingWindow([1], 1))  # return [1]
#time complexity: O(n) because each element is added and removed from the deque at most once.
#space complexity: O(k) because the deque can hold at most k indices at any time, which corresponds to the size of the sliding window.  