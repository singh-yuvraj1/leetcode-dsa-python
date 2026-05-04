# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

#solution 1: Brute Force Solution
class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = merged[-1]
            
            # Check if the current interval overlaps with the last merged interval
            if current[0] <= last_merged[1]:  # Overlapping intervals
                # Merge the intervals by updating the end time of the last merged interval
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval to the merged list
                merged.append(current)
        
        return merged
if __name__== "__main__":
    a = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(a.merge(intervals1))  # [[1,6],[8,10],[15,18]]

    intervals2 = [[1,4],[4,5]]
    print(a.merge(intervals2))  # [[1,5]]

    intervals3 = [[4,7],[1,4]]
    print(a.merge(intervals3))  # [[1,7]]

## Time Complexity: O(n log n) where n is the number of intervals. This is due to the sorting step, which takes O(n log n) time. The merging step takes O(n) time, resulting in an overall time complexity of O(n log n).
## Space Complexity: O(n) in the worst case, if all intervals are non-overlapping, we will have to store all intervals in the merged list. In the best case, if all intervals overlap, we will only store one interval in the merged list, resulting in O(1) space complexity. Therefore, the overall space complexity is O(n) in the worst case.
