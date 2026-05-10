# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

 

# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)


# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)


# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 

# Constraints:

# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104


#--------------------brute force solution--------------------
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        
        return boats
if __name__== "__main__":
    a = Solution()
    people1 = [1,2]
    limit1 = 3
    print(a.numRescueBoats(people1, limit1))  # 1

    people2 = [3,2,2,1]
    limit2 = 3
    print(a.numRescueBoats(people2, limit2))  # 3

    people3 = [3,5,3,4]
    limit3 = 5
    print(a.numRescueBoats(people3, limit3))  # 4
## Time Complexity: O(n log n) due to the sorting step. The two-pointer traversal takes O(n) time.
## Space Complexity: O(1) if we ignore the space used for sorting. If the sorting algorithm used is not in-place, then the space complexity would be O(n) due to the additional space used for sorting.


