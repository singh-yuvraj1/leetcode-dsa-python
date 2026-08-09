# 287. Find the Duplicate Number
# Medium
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.
 

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?



#brute force solution (using set)  = O(n) time complexity and O(n) space complexity
def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)   
if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print(findDuplicate(nums))  # Output: 2


#time complexity = O(n)  because we are iterating through the array once
#space complexity = O(n)  because we are using a set to store the seen numbers, which can potentially store all n numbers in the worst case.



#optimized solution (Floyd's Tortoise and Hare) = O(n) time complexity and O(1) space complexity
def findDuplicate(nums):
    # Step 1: Find the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Step 2: Find the entrance to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
#time complexity = O(n)  because we are iterating through the array once
#space complexity = O(1)  because we are not using any extra space like an extra array or set or anything , just we use use variables .