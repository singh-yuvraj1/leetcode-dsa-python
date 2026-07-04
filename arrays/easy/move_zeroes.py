# 283. Move Zeroes
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# Example 2:
# Input: nums = [0]
# Output: [0]
 
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

#------------------------optimizeed solution (Two pointer)----------------------

def movezeroes(nums):
    r = 0 #pointer 1 that will read all array values 
    w = 0 #pointer 2 that will wirte non zero values

    for r in range(len(nums)):
        if nums[r] != 0 :
            nums[w] , nums[r] = nums[r] , nums[w]   # it will swap non zero with zero and place them at correct position
            w = w +1  # after getting non zero  move writig pointer by 1 
        

#theres nothing to return in this questiion because we are making in place changes 

# TIme complexity  = O(n)   because loop will iterate n number of times
#space complexity = O(1)    because we are not using any extra space like an extra array or set or anything , just we use use variables .