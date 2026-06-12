# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 
# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.



#brute force solution
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#time complexity: O(n) for getMin() and O(1) for push(), pop(), and top()   
# space complexity: O(n) for the stack. 


#optimized solution using 2 stacks

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#time complexity: O(1) for all operations (push, pop, top, getMin)
# space complexity: O(n) for the main stack and O(m) for the min stack, where m is the number of minimum values stored in the min stack. In the worst case, if all values are the same and are the minimum, then m can be equal to n, resulting in O(n) space complexity for both stacks.
