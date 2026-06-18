# 31. Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.


# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]


# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]


# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

#brute force of this question is not possible because we have to find the next permutation in place and use only constant extra memory.


#optimized solution
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Find the first element larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the elements
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements to the right of i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3]
    s.nextPermutation(nums1)
    print(nums1)  # Output: [1, 3, 2]

    nums2 = [3, 2, 1]
    s.nextPermutation(nums2)
    print(nums2)  # Output: [1, 2, 3]

    nums3 = [1, 1, 5]
    s.nextPermutation(nums3)
    print(nums3)  # Output: [1, 5, 1]
#time complexity: O(n) because we are iterating through the array of length n to find the first decreasing element and then again to find the first element larger than nums[i] and then again to reverse the elements to the right of i.
#space complexity: O(1) because we are using only constant extra memory.
