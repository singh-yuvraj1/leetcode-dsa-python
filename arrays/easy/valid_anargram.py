# 242. Valid Anagram 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

#---------------------------------Brute-Force Solution-------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
if __name__== "__main__":
    a = Solution()
    s1, t1 = "anagram", "nagaram"
    print(a.isAnagram(s1, t1))  # True

    s2, t2 = "rat", "car"
    print(a.isAnagram(s2, t2))  # False

## Time Complexity: O(n log n) where n is the length of the input strings. Sorting both strings takes O(n log n) time.
## Space Complexity: O(n) where n is the length of the input strings. Sorting creates new sorted lists, which require O(n) space.




#---------------------------------Two Pointer Solution-------------------------------

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        for char in t:
            count[ord(char) - ord('a')] -= 1
        
        return all(x == 0 for x in count)
    
if __name__== "__main__":
    a = Solution()
    s1, t1 = "anagram", "nagaram"
    print(a.isAnagram(s1, t1))  # True

    s2, t2 = "rat", "car"
    print(a.isAnagram(s2, t2))  # False 


## Time Complexity: O(n) where n is the length of the input strings. We traverse both strings once.
## Space Complexity: O(1) since we are using a fixed-size array of length 26 to count the occurrences of each character, which does not depend on the size of the input strings.
