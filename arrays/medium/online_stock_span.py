# 901. Online Stock Span
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.
# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:
# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 

# Example 1:
# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]


# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
 


# Constraints:
# 1 <= price <= 105
# At most 104 calls will be made to next.


#brutee force

class StockSpanner(object):

    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)

        span = 1
        i = len(self.prices) - 2

        # Check previous prices one by one
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span
if __name__ == "__main__":
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))  # return 1
    print(stockSpanner.next(80))   # return 1
    print(stockSpanner.next(60))   # return 1
    print(stockSpanner.next(70))   # return 2
    print(stockSpanner.next(60))   # return 1
    print(stockSpanner.next(75))   # return 4
    print(stockSpanner.next(85))   # return 6
#time complexity: O(n) for each next call in the worst case, where n is the number of prices seen so far. In the worst case, we may have to check all previous prices to calculate the span.
#space complexity: O(n), where n is the number of prices seen so far. We store all the prices in a list, which requires O(n) space.


#optimized solution using stack
class StockSpanner(object):

    def __init__(self):
        # stack stores: (price, span)
        self.stack = []

    def next(self, price):
        span = 1

        # Merge smaller/equal prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span
if __name__ == "__main__":
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))  # return 1
    print(stockSpanner.next(80))   # return 1
    print(stockSpanner.next(60))   # return 1
    print(stockSpanner.next(70))   # return 2
    print(stockSpanner.next(60))   # return 1
    print(stockSpanner.next(75))   # return 4
    print(stockSpanner.next(85))   # return 6
#time complexity: O(1) for each next call on average. Each price is pushed and popped from the stack at most once, leading to an amortized time complexity of O(1) per next call.
#space complexity: O(n), where n is the number of prices seen so far. In the worst case, all prices are in decreasing order, and we store all of them in the stack, which requires O(n) space.
