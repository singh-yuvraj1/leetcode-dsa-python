# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

#------------------------------Solution  brute force -------------------------------

class Solution1(object):
    def sortedSquares(self, nums):
        return sorted(x ** 2 for x in nums)

if __name__== "__main__":
    a = Solution1()
    nums1 = [-4,-1,0,3,10]
    print(a.sortedSquares(nums1))  # [0,1,9,16,100]
    
    b = Solution1()                     
    nums2 = [-7,-3,2,3,11]
    print(b.sortedSquares(nums2))  # [4,9,9,49,121]
    
#time complexity: O(n log n) - Sorting the array takes O(n log n) time, and generating the squared values takes O(n) time.
#space complexity: O(n) - We are creating a new array to store the squared values, which takes O(n) space. The sorting operation may also require O(n) space in the worst case, depending on the sorting algorithm used.



#---------------------------two pointer approach-------------------------------

class Solution2(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result
if __name__== "__main__":
    a = Solution2()
    nums1 = [-4,-1,0,3,10]
    print(a.sortedSquares(nums1))  # [0,1,9,16,100]
    
    b = Solution2()                     
    nums2 = [-7,-3,2,3,11]
    print(b.sortedSquares(nums2))  # [4,9,9,49,121]

# time complexity: O(n) - We traverse the nums array once with two pointers.
# space complexity: O(n) - We are using an additional array result to store the squared values.