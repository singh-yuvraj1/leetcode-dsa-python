# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
 
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

#------------------------------Solution-------------------------------
# The idea is to use three pointers: one for the current position, one for the end of the red section, and one for the start of the blue section. We iterate through the array and swap elements as needed to ensure that all 0s are moved to the beginning, all 2s are moved to the end, and all 1s remain in the middle. 
class Solution(object):
    def sortColors(self, nums):
       
        low , mid , high = 0 ,0 , len(nums)-1
        while mid<= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
            
if __name__== "__main__":
    a = Solution()
    nums1 = [2,0,2,1,1,0]
    a.sortColors(nums1)
    print(nums1)  # [0,0,1,1,2,2]

    nums2 = [2,0,1]
    a.sortColors(nums2)
    print(nums2)  # [0,1,2]                 